import os.path

from cffi import FFI


cdef_file = os.path.join(os.path.dirname(__file__), 'claypellet_cdef.c')
c_file = os.path.join(os.path.dirname(__file__), 'claypellet.c')


ffi = FFI()
ffi.cdef(open(cdef_file).read())


class PebbleHarness(object):
    def __init__(self, app_lib, include_dirs=None, library_dirs=None):
        if include_dirs is None:
            include_dirs = ['./include', './build']
        if library_dirs is None:
            library_dirs = ['.']
        self.lib = ffi.verify(
            open(c_file).read(), include_dirs=include_dirs,
            library_dirs=library_dirs, libraries=[app_lib])
        self.setup_callbacks()

    def run(self):
        self.lib.pbl_main(ffi.NULL)

    def setup_callbacks(self):
        self.callbacks = [
            ffi.callback('void(*)(AppTaskContextRef, PebbleAppHandlers*)',
                         self.app_event_loop),
            ffi.callback('void(Window *, const char *)',
                         self.window_init),
            ]
        self.lib.setup_callbacks(*self.callbacks)

    def app_event_loop(self, app_task_ctx, handlers):
        if handlers.init_handler != ffi.NULL:
            handlers.init_handler(ffi.NULL)

    def window_init(self, window, debug_name):
        print ffi.string(debug_name)
