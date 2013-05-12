import os.path
import time
from math import sin, cos, pi

from cffi import FFI

from .resources import PebbleResources
from .font import PebbleFont
from .bitmap import PebbleBitmap
from .harness_hooks import PebbleHarnessBase


package_dir = os.path.dirname(__file__)

cdef_file = os.path.join(package_dir, 'claypellet_cdef.c')
h_file = os.path.join(package_dir, 'claypellet_harness.h')
c_file = os.path.join(package_dir, 'claypellet_harness.c')


ffi = FFI()
ffi.cdef('\n'.join(open(f).read() for f in (cdef_file, h_file)))


class PebbleHarness(PebbleHarnessBase):
    def __init__(self, app_lib, resources_file, include_dirs=None):
        self.resources_file = resources_file
        if '/' not in app_lib:
            app_lib = './' + app_lib
        self.app_lib = app_lib

        if include_dirs is None:
            include_dirs = [package_dir, './include']

        self.lib = ffi.verify(open(c_file).read(), include_dirs=include_dirs)
        print "Setting up callbacks..."
        self.setup_callbacks()
        self.load_app()

    def load_app(self, unload=False):
        if unload:
            self.lib.deinit_claypellet()

        print "Loading app..."
        if self.lib.init_claypellet(self.app_lib) != 0:
            raise Exception("Can't load app.")
        self.lib.call_setup_callbacks(*self._callbacks)
        print "App loaded."
        self.windows = {}
        self.window_stack = []
        self.layers = {}
        self.sublayers = {
            'text': {},
            'bitmap': {},
            'rot_bitmap': {},
            'rot_bitmap_pair': {},
        }
        self.resources = None
        self.resource_handles = {}
        self.custom_fonts = {}
        self.bitmaps = {}
        self.handlers = None
        self.last_tick = None

    @property
    def top_window(self):
        return self.windows[self.window_stack[-1]]

    def get_window(self, windowp):
        return self.windows[windowp[0]]

    def get_layer(self, layerp):
        return self.layers[layerp[0]]

    def get_inner_layer(self, somestruct):
        return self.layers[somestruct.layer]

    def get_sublayer(self, layer_type, sublayerp):
        return self.sublayers[layer_type][sublayerp[0]]

    def get_resource(self, resource_handle):
        handle = ffi.cast('struct ClayResourceHandle *', resource_handle)
        return self.resource_handles[handle.file_id]

    def get_custom_font(self, font_handle):
        handle = ffi.cast('struct ClayResourceHandle *', font_handle)
        return self.custom_fonts[handle.file_id]

    def get_bitmap(self, bitmap_handle):
        handle = ffi.cast('struct ClayResourceHandle *', bitmap_handle)
        return self.bitmaps[handle.file_id]

    def call_main(self):
        self.lib.call_main()

    def tick(self):
        self.remember = []  # Hang onto some cdatas until next tick.
        last_tick = self.last_tick
        self.last_tick = tick = time.localtime()

        if last_tick is None:
            if self.handlers['init_handler'] != ffi.NULL:
                self.handlers['init_handler'](ffi.NULL)
            return self.top_window.is_render_scheduled

        tick_handler = self.handlers['tick_info']['tick_handler']
        if tick_handler != ffi.NULL:
            timep = ffi.new('PblTm *')
            self.mkpbltm(tick, timep)

            units_changed = None
            if tick.tm_year > last_tick.tm_year:
                units_changed = self.lib.YEAR_UNIT
            elif tick.tm_mon > last_tick.tm_mon:
                units_changed = self.lib.MONTH_UNIT
            elif tick.tm_mday > last_tick.tm_mday:
                units_changed = self.lib.DAY_UNIT
            elif tick.tm_hour > last_tick.tm_hour:
                units_changed = self.lib.HOUR_UNIT
            elif tick.tm_min > last_tick.tm_min:
                units_changed = self.lib.MINUTE_UNIT
            elif tick.tm_sec > last_tick.tm_sec:
                units_changed = self.lib.SECOND_UNIT

            tick_units = self.handlers['tick_info']['tick_units']
            if units_changed is not None and units_changed >= tick_units:
                tick_eventp = ffi.new('PebbleTickEvent *', {
                    'units_changed': units_changed,
                    'tick_time': timep,
                })
                tick_handler(ffi.NULL, tick_eventp)

        # TODO: More events
        return self.top_window.is_render_scheduled

    def mkpbltm(self, time_tick, timep):
        timep.tm_sec = time_tick.tm_sec
        timep.tm_min = time_tick.tm_min
        timep.tm_hour = time_tick.tm_hour
        timep.tm_mday = time_tick.tm_mday
        timep.tm_mon = time_tick.tm_mon
        timep.tm_year = time_tick.tm_year - 1900
        timep.tm_wday = (time_tick.tm_wday + 1) % 7
        timep.tm_yday = time_tick.tm_yday
        timep.tm_isdst = time_tick.tm_isdst

    def render(self, gctx):
        self.graphics_contexts = {}
        self.graphics_context_handles = []
        self.top_window.render(gctx)

    def get_graphics_context(self, gctxp):
        handle = ffi.cast('struct ClayGraphicsContext *', gctxp)
        return self.graphics_contexts[handle[0].gctx_id]

    def get_gctx_handle(self, gctx):
        # TODO: Better mechanism for this.
        handle = ffi.new('struct ClayGraphicsContext *', {'gctx_id': 0})
        self.graphics_context_handles.append(handle)
        for k, v in self.graphics_contexts.iteritems():
            if v is gctx:
                handle.gctx_id = k
                return handle
        gctx_id = len(self.graphics_contexts)
        self.graphics_contexts[gctx_id] = gctx
        handle.gctx_id = gctx_id
        return ffi.cast('GContext *', handle)

    def init_inner_layer(self, somestruct, frame):
        layer = somestruct.layer
        self.layers[layer] = PebbleLayer(self, ffi.addressof(layer), frame)

    def _mkcallback(self, name):
        return ffi.callback('t_%s_cb' % name, getattr(self, name))

    # Animation

    # void animation_init(Animation *animation);
    # void animation_set_delay(Animation *animation, uint32_t delay_ms);
    # void animation_set_duration(Animation *animation, uint32_t duration_ms);
    # void animation_set_curve(Animation *animation, AnimationCurve curve);
    # void animation_set_handlers(
    #     Animation *animation, AnimationHandlers callbacks, void *context);
    # void animation_set_implementation(
    #     Animation *animation, const AnimationImplementation *implementation);
    # void *animation_get_context(Animation *animation);
    # void animation_schedule(Animation *animation);
    # void animation_unschedule(Animation *animation);
    # void animation_unschedule_all(void);
    # bool animation_is_scheduled(Animation *animation);

    # void property_animation_init_layer_frame(
    #    PropertyAnimation *property_animation, struct Layer *layer,
    #    GRect *from_frame, GRect *to_frame);

    # App

    def app_event_loop(self, app_task_ctx, handlers):
        self.handlers = {
            'init_handler': handlers.init_handler,
            # 'deinit_handler': handlers.deinit_handler,
            # 'render_handler': handlers.render_handler,
            # 'input_handlers': handlers.input_handlers,
            'tick_info': {
                'tick_handler': handlers.tick_info.tick_handler,
                'tick_units': handlers.tick_info.tick_units,
            },
            # 'timer_handler': handlers.timer_handler,
            # 'messaging_info': handlers.messaging_info,
        }

    # Graphics - Bitmaps

    def _bitmap_init(self, file_id, gbitmapp):
        if file_id not in self.resource_handles:
            resource_handle = PebbleResourceHandle(self, file_id)
            self.resource_handles[file_id] = resource_handle
        resource_handle = self.resource_handles[file_id]

        if file_id not in self.bitmaps:
            bitmap = PebbleBitmap(resource_handle.get_data())
            self.bitmaps[file_id] = bitmap
        bitmap = self.bitmaps[file_id]

        gbitmapp.addr = ffi.cast('void *', resource_handle.get_handle())
        gbitmapp.row_size_bytes = bitmap.row_size_bytes
        gbitmapp.info_flags = bitmap.info_flags
        gbitmapp.bounds = ffi.new('GRect *', bitmap.rect.get_grect_struct())[0]

    def bitmap_layer_init(self, imagep, frame):
        bmp_layer = PebbleBitmapLayer(self, imagep, frame)
        self.sublayers['bitmap'][imagep[0]] = bmp_layer

    def bitmap_layer_set_bitmap(self, imagep, gbitmapp):
        self.get_sublayer('bitmap', imagep).set_bitmap(gbitmapp)

    def bitmap_layer_set_compositing_mode(self, imagep, mode):
        self.get_sublayer('bitmap', imagep).set_compositing_mode(mode)

    def bmp_init_container(self, resource_id, containerp):
        gbitmapp = ffi.addressof(containerp.bmp)
        self._bitmap_init(resource_id, gbitmapp)
        imagep = ffi.addressof(containerp.layer)
        bmp_layer = PebbleBitmapLayer(self, imagep, gbitmapp.bounds)
        self.sublayers['bitmap'][imagep[0]] = bmp_layer
        bmp_layer.set_bitmap(gbitmapp)
        return True

    # void bmp_deinit_container(BmpContainer *c);

    def graphics_draw_bitmap_in_rect(self, gctxp, gbitmapp, grect):
        gctx = self.get_graphics_context(gctxp)
        bitmap = self.get_bitmap(gbitmapp.addr)
        gctx.draw_bitmap(bitmap, grect)

    # void rotbmp_deinit_container(RotBmpContainer *c);

    def rotbmp_init_container(self, resource_id, containerp):
        gbitmapp = ffi.addressof(containerp.bmp)
        self._bitmap_init(resource_id, gbitmapp)
        imagep = ffi.addressof(containerp.layer)
        rotbmp_layer = PebbleRotBitmapLayer(self, imagep, gbitmapp.bounds)
        self.sublayers['rot_bitmap'][imagep[0]] = rotbmp_layer
        rotbmp_layer.set_bitmap(gbitmapp)
        return True

    # void rotbmp_pair_deinit_container(RotBmpPairContainer *c);

    def rotbmp_pair_init_container(self, white_id, black_id, containerp):
        w_gbitmapp = ffi.addressof(containerp.white_bmp)
        self._bitmap_init(white_id, w_gbitmapp)
        b_gbitmapp = ffi.addressof(containerp.black_bmp)
        self._bitmap_init(black_id, b_gbitmapp)

        pairp = ffi.addressof(containerp.layer)
        layer = PebbleRotBmpPairLayer(self, pairp, w_gbitmapp.bounds)
        self.sublayers['rot_bitmap_pair'][pairp[0]] = layer

        w_imagep = ffi.addressof(pairp.white_layer)
        w_layer = PebbleRotBitmapLayer(self, w_imagep, w_gbitmapp.bounds)
        self.sublayers['rot_bitmap'][w_imagep[0]] = w_layer
        w_layer.set_bitmap(w_gbitmapp)
        w_layer.set_compositing_mode(self.lib.GCompOpOr)
        w_layer.set_corner_clip_color(self.lib.GColorBlack)
        self.layer_add_child(ffi.addressof(pairp.layer),
                             ffi.addressof(w_imagep.layer))

        b_imagep = ffi.addressof(pairp.black_layer)
        b_layer = PebbleRotBitmapLayer(self, b_imagep, b_gbitmapp.bounds)
        self.sublayers['rot_bitmap'][b_imagep[0]] = b_layer
        b_layer.set_bitmap(b_gbitmapp)
        b_layer.set_compositing_mode(self.lib.GCompOpClear)
        b_layer.set_corner_clip_color(self.lib.GColorWhite)
        self.layer_add_child(ffi.addressof(pairp.layer),
                             ffi.addressof(b_imagep.layer))

        return True

    # void rotbmp_pair_layer_set_src_ic(RotBmpPairLayer *pair, GPoint ic);
    # void rotbmp_pair_layer_set_angle(RotBmpPairLayer *pair, int32_t angle);

    # Graphics - Contexts

    # GContext *app_get_current_graphics_context(void);

    # Graphics - Drawing - Shapes

    # void graphics_draw_pixel(GContext *ctx, GPoint point);
    # void graphics_draw_line(GContext *ctx, GPoint p0, GPoint p1);

    def graphics_draw_line(self, gctxp, p0, p1):
        gctx = self.get_graphics_context(gctxp)
        gctx.draw_line(p0, p1)

    def graphics_fill_rect(self, gctxp, rect, radius, corner_mask):
        # TODO: corner_mask
        gctx = self.get_graphics_context(gctxp)
        gctx.draw_round_rect(rect, radius, gctx.fill_color, gctx.fill_color)

    def graphics_draw_circle(self, gctxp, point, radius):
        gctx = self.get_graphics_context(gctxp)
        gctx.draw_circle(point, radius, gctx.stroke_color, gctx.COLOR_CLEAR)

    def graphics_fill_circle(self, gctxp, point, radius):
        gctx = self.get_graphics_context(gctxp)
        gctx.draw_circle(point, radius, gctx.fill_color, gctx.fill_color)

    def graphics_draw_round_rect(self, gctxp, rect, radius):
        gctx = self.get_graphics_context(gctxp)
        gctx.draw_round_rect(rect, radius, gctx.stroke_color, gctx.COLOR_CLEAR)

    # Graphics - Drawing - Paths

    # void gpath_init(GPath *path, const GPathInfo *init);
    # void gpath_move_to(GPath *path, GPoint point);
    # void gpath_rotate_to(GPath *path, int32_t angle);
    # void gpath_draw_outline(GContext *ctx, GPath *path);
    # void gpath_draw_filled(GContext *ctx, GPath *path);

    # Graphics - Drawing - Style

    def _translate_color(self, gctx, color):
        return {
            self.lib.GColorClear: gctx.COLOR_CLEAR,
            self.lib.GColorBlack: gctx.COLOR_BLACK,
            self.lib.GColorWhite: gctx.COLOR_WHITE,
        }[color]

    def _translate_align(self, gctx, align):
        return {
            self.lib.GTextAlignmentLeft: gctx.ALIGN_LEFT,
            self.lib.GTextAlignmentCenter: gctx.ALIGN_CENTER,
            self.lib.GTextAlignmentRight: gctx.ALIGN_RIGHT,
        }[align]

    def _translate_comp_op(self, gctx, mode):
        return {
            self.lib.GCompOpAssign: gctx.COMP_ASSIGN,
            self.lib.GCompOpAssignInverted: gctx.COMP_ASSIGN_INVERTED,
            self.lib.GCompOpOr: gctx.COMP_OR,
            self.lib.GCompOpAnd: gctx.COMP_AND,
            self.lib.GCompOpClear: gctx.COMP_CLEAR,
        }[mode]

    def graphics_context_set_stroke_color(self, gctxp, color):
        gctx = self.get_graphics_context(gctxp)
        gctx.stroke_color = self._translate_color(gctx, color)

    def graphics_context_set_fill_color(self, gctxp, color):
        gctx = self.get_graphics_context(gctxp)
        gctx.fill_color = self._translate_color(gctx, color)

    def graphics_context_set_text_color(self, gctxp, color):
        gctx = self.get_graphics_context(gctxp)
        gctx.text_color = self._translate_color(gctx, color)

    def graphics_context_set_compositing_mode(self, gctxp, mode):
        gctx = self.get_graphics_context(gctxp)
        gctx.compositing_mode = self._translate_comp_op(gctx, mode)

    # void graphics_context_set_compositing_mode(GContext *ctx, GCompOp mode);

    # Graphics - Drawing - Text

    # void graphics_text_draw(
    #    GContext *ctx, const char *text, const GFont font, const GRect box,
    #    const GTextOverflowMode overflow_mode, const GTextAlignment alignment,
    #    const GTextLayoutCacheRef layout);
    def graphics_text_draw(self, gctxp, text, font, box, overflow_mode,
                           alignment, layout):
        gctx = self.get_graphics_context(gctxp)
        gctx.draw_text(ffi.string(text), self.get_custom_font(font), box,
                       self._translate_align(gctx, alignment))

    # Hardware - Backlight

    # void light_enable(bool enable);
    # void light_enable_interaction(void);

    # Hardware - Buttons

    # void window_set_click_config_provider(
    #    Window *window, ClickConfigProvider click_config_provider);

    # Hardware - Vibration

    # void vibes_double_pulse(void);
    # void vibes_enqueue_custom_pattern(VibePattern pattern);
    # void vibes_long_pulse(void);
    # void vibes_short_pulse(void);

    # Layers

    def layer_mark_dirty(self, layerp):
        self.get_layer(layerp).mark_dirty()

    def layer_remove_from_parent(self, childp):
        self.get_layer(childp).remove_from_parent()

    def layer_add_child(self, parentp, childp):
        self.get_layer(parentp).add_child(childp)

    def layer_get_frame(self, layerp):
        return self.get_layer(layerp).get_frame()

    def layer_set_frame(self, layerp, frame):
        self.get_layer(layerp).set_frame(frame)

    def layer_get_bounds(self, layerp):
        return self.get_layer(layerp).get_bounds()

    def layer_set_bounds(self, layerp, bounds):
        self.get_layer(layerp).set_bounds(bounds)

    def layer_set_hidden(self, layerp, hidden):
        self.get_layer(layerp).set_hidden(hidden)

    def layer_init(self, layerp, frame):
        self.layers[layerp[0]] = PebbleLayer(self, layerp, frame)

    # Math

    def cos_lookup(self, angle):
        rads = (angle * 2 * pi) / self.lib.TRIG_MAX_ANGLE
        return int(self.lib.TRIG_MAX_ANGLE * cos(rads))

    def sin_lookup(self, angle):
        rads = (angle * 2 * pi) / self.lib.TRIG_MAX_ANGLE
        return int(self.lib.TRIG_MAX_ANGLE * sin(rads))

    def grect_center_point(self, grect):
        gpoint = ffi.new('GPoint *', {
            'x': grect.origin.x + grect.size.w / 2,
            'y': grect.origin.y + grect.size.h / 2,
        })
        self.remember.append(gpoint)
        return gpoint[0]

    # Resources

    def resource_init_current_app(self, version):
        self.resources = PebbleResources(open(self.resources_file).read())
        try:
            self.resources.verify_data()
        except ImportError:
            print "Can't verify resources, module stm32_crc not found."
        except AssertionError:
            raise Exception("Resources corrupt.")

    def resource_get_handle(self, file_id):
        if file_id not in self.resource_handles:
            resource_handle = PebbleResourceHandle(self, file_id)
            self.resource_handles[file_id] = resource_handle
        return self.resource_handles[file_id].get_handle()

    # size_t resource_load(ResHandle h, uint8_t *buffer, size_t max_length);
    # size_t resource_load_byte_range(
    #    ResHandle h, uint32_t start_bytes, uint8_t *data, size_t num_bytes);
    # size_t resource_size(ResHandle h);

    # Text - Fonts

    # GFont fonts_get_system_font(const char *font_key);

    def fonts_load_custom_font(self, resourcep):
        resource_handle = self.get_resource(resourcep)
        if resource_handle.file_id not in self.custom_fonts:
            font = PebbleFont(resource_handle.get_data())
            self.custom_fonts[resource_handle.file_id] = font
        return resourcep

    # void fonts_unload_custom_font(GFont font);

    # Text - Layers

    def text_layer_init(self, text_layerp, frame):
        text_layer = PebbleTextLayer(self, text_layerp, frame)
        self.sublayers['text'][text_layerp[0]] = text_layer

    # const char *text_layer_get_text(TextLayer *text_layer);

    def text_layer_set_text(self, text_layerp, text):
        text_layer = self.get_sublayer('text', text_layerp)
        text_layer.set_text(text)

    def text_layer_set_background_color(self, text_layerp, color):
        self.get_sublayer('text', text_layerp).set_background_color(color)

    def text_layer_set_font(self, text_layerp, fontp):
        self.get_sublayer('text', text_layerp).set_font(fontp)

    def text_layer_set_text_alignment(self, text_layerp, text_alignment):
        self.get_sublayer('text', text_layerp).set_text_alignment(
            text_alignment)

    def text_layer_set_text_color(self, text_layerp, color):
        self.get_sublayer('text', text_layerp).set_text_color(color)

    # Time

    def clock_is_24h_style(self):
        # TODO: Make this option optional.
        return True

    def get_time(self, timep):
        now = time.localtime()
        self.mkpbltm(now, timep)

    def string_format_time(self, ptr, maxsize, fmt, timep):
        ts = (timep.tm_year + 1900, timep.tm_mon, timep.tm_mday, timep.tm_hour,
              timep.tm_min, timep.tm_sec, timep.tm_wday, timep.tm_yday,
              timep.tm_isdst)
        timestr = time.strftime(ffi.string(fmt), ts)[:maxsize]
        buf = ffi.buffer(ptr, maxsize)
        buf[:len(timestr)] = timestr
        buf[len(timestr)] = '\0'  # Is this necessary?

    # void string_format_time(
    #    char *ptr, size_t maxsize, const char *format, const PblTm *timeptr);

    # void psleep(int millis);

    # Timers

    # AppTimerHandle app_timer_send_event(
    #    AppContextRef app_ctx, uint32_t timeout_ms, uint32_t cookie);
    # bool app_timer_cancel_event(
    #    AppContextRef app_ctx_ref, AppTimerHandle handle);

    # Windows

    def window_init(self, windowp, debug_name):
        self.windows[windowp[0]] = PebbleWindow(self, windowp, debug_name)

    def window_stack_push(self, windowp, animated):
        # TODO: Animated.
        self.window_stack.append(windowp[0])

    def window_set_background_color(self, windowp, background_color):
        self.get_window(windowp).set_background_color(background_color)

    # void window_render(Window *window, GContext *ctx);
    # void window_set_fullscreen(Window *window, bool enabled);


class PebbleWindow(object):

    background_color = None
    is_render_scheduled = False
    on_screen = False
    is_loaded = True
    overrides_back_button = False
    is_fullscreen = True

    def __init__(self, harness, windowp, debug_name):
        self._harness = harness
        self._windowp = windowp
        self._windowp.debug_name = debug_name
        wframe = ffi.new('GRect *', ((0, 0), (144, 168)))
        harness.init_inner_layer(windowp, wframe[0])
        windowp.layer.window = windowp
        self.background_color = self._harness.lib.GColorWhite

    @property
    def root_layer(self):
        return self._harness.get_inner_layer(self._windowp)

    def set_background_color(self, color):
        self.background_color = color

    def render(self, gctx):
        gctx.bgfill(self._harness._translate_color(gctx,
                                                   self.background_color))
        self.root_layer.render(gctx)
        self.is_render_scheduled = False


class PebbleLayer(object):
    def __init__(self, harness, layerp, frame):
        self._harness = harness
        self._layerp = layerp
        self.set_frame(frame)
        bounds = ffi.new('GRect *', {'origin': (0, 0), 'size': frame.size})[0]
        layerp.bounds = bounds
        layerp.window = ffi.NULL
        layerp.hidden = False

    def set_frame(self, frame):
        self._layerp.frame = frame
        if self._layerp.bounds.size.w < frame.size.w:
            self._layerp.bounds.size.w = frame.size.w
        if self._layerp.bounds.size.h < frame.size.h:
            self._layerp.bounds.size.h = frame.size.h

    def get_frame(self):
        return self._layerp.frame

    def set_bounds(self, bounds):
        self._layerp.bounds = bounds

    def get_bounds(self):
        return self._layerp.bounds

    def set_hidden(self, hidden):
        self._layerp.hidden = hidden

    def add_child(self, layerp):
        assert layerp.parent == ffi.NULL
        layerp.parent = self._layerp
        layerp.window = self._layerp.window
        if self._layerp.first_child == ffi.NULL:
            self._layerp.first_child = layerp
        else:
            childp = self._layerp.first_child
            while childp.next_sibling != ffi.NULL:
                childp = childp.next_sibling
            childp.next_sibling = layerp
        self.mark_dirty()

    def remove_from_parent(self):
        raise NotImplementedError("PebbleLayer.remove_from_parent")

    def get_window(self):
        return self._harness.get_window(self._layerp.window)

    def mark_dirty(self):
        if self._layerp.window != ffi.NULL:
            self.get_window().is_render_scheduled = True

    def render(self, gctx):
        if self._layerp.hidden:
            return
        my_gctx = gctx.get_child_context(self._layerp.frame)
        if self._layerp.update_proc != ffi.NULL:
            gctxp = self._harness.get_gctx_handle(my_gctx)
            self._layerp.update_proc(self._layerp, gctxp)
        if self._layerp.first_child != ffi.NULL:
            self._harness.get_layer(self._layerp.first_child).render(my_gctx)
        if self._layerp.next_sibling != ffi.NULL:
            self._harness.get_layer(self._layerp.next_sibling).render(gctx)


class PebbleTextLayer(object):

    background_color = None
    text_color = None
    text_alignment = None

    def __init__(self, harness, text_layerp, frame):
        self._harness = harness
        self._text_layerp = text_layerp
        harness.init_inner_layer(text_layerp, frame)
        self._update_proc = ffi.callback('LayerUpdateProc', self.update_proc)
        text_layerp.layer.update_proc = self._update_proc

    @property
    def layer(self):
        return self._harness.get_inner_layer(self._text_layerp)

    def set_text_color(self, color):
        self.text_color = color

    def set_background_color(self, color):
        self.background_color = color

    def set_text_alignment(self, text_alignment):
        self.text_alignment = text_alignment

    def set_font(self, fontp):
        self._text_layerp.font = fontp

    def set_text(self, text):
        self._text_layerp.text = text
        self.layer.mark_dirty()

    def update_proc(self, layerp, gctxp):
        h = self._harness
        tl = self._text_layerp

        if self.background_color != self._harness.lib.GColorClear:
            h.graphics_context_set_fill_color(gctxp, self.background_color)
            h.graphics_fill_rect(gctxp, layerp.bounds, 0, h.lib.GCornerNone)

        if (tl.text != ffi.NULL and len(ffi.string(tl.text)) > 0):
            h.graphics_context_set_text_color(gctxp, self.text_color)
            # TODO: Fix this.
            h.graphics_text_draw(gctxp, tl.text, tl.font, layerp.bounds,
                                 0, self.text_alignment, ffi.NULL)


class PebbleBitmapLayer(object):
    def __init__(self, harness, imagep, frame):
        self._harness = harness
        self._imagep = imagep
        harness.init_inner_layer(imagep, frame)
        imagep.bitmap = ffi.NULL
        imagep.compositing_mode = self._harness.lib.GCompOpAssign

        self._update_proc = ffi.callback('LayerUpdateProc', self.update_proc)
        imagep.layer.update_proc = self._update_proc

    @property
    def layer(self):
        return self._harness.get_inner_layer(self._imagep)

    def set_bitmap(self, gbitmapp):
        self._imagep.bitmap = gbitmapp

    def set_compositing_mode(self, mode):
        self._imagep.compositing_mode = mode

    def update_proc(self, layerp, gctxp):
        h = self._harness
        i = self._imagep
        h.graphics_context_set_compositing_mode(gctxp, i.compositing_mode)
        h.graphics_draw_bitmap_in_rect(gctxp, i.bitmap, i.layer.frame)


class PebbleRotBitmapLayer(object):
    def __init__(self, harness, imagep, frame):
        self._harness = harness
        self._imagep = imagep
        harness.init_inner_layer(imagep, frame)
        imagep.bitmap = ffi.NULL
        imagep.compositing_mode = self._harness.lib.GCompOpAssign

        self._update_proc = ffi.callback('LayerUpdateProc', self.update_proc)
        imagep.layer.update_proc = self._update_proc

    @property
    def layer(self):
        return self._harness.get_inner_layer(self._imagep)

    def set_bitmap(self, gbitmapp):
        self._imagep.bitmap = gbitmapp

    def set_compositing_mode(self, mode):
        self._imagep.compositing_mode = mode

    def set_corner_clip_color(self, gcolor):
        self._imagep.corner_clip_color = gcolor

    def update_proc(self, layerp, gctxp):
        h = self._harness
        i = self._imagep
        gctx = h.get_graphics_context(gctxp)
        bitmap = h.get_bitmap(i.bitmap.addr)
        angle = (360 * i.rotation) / h.lib.TRIG_MAX_ANGLE
        h.graphics_context_set_compositing_mode(gctxp, i.compositing_mode)
        gctx.draw_rotated_bitmap(bitmap, i.src_ic, i.dest_ic, angle)


class PebbleRotBmpPairLayer(object):
    def __init__(self, harness, pairp, frame):
        self._harness = harness
        self._pairp = pairp
        harness.init_inner_layer(pairp, frame)

        self._update_proc = ffi.callback('LayerUpdateProc', self.update_proc)
        pairp.layer.update_proc = self._update_proc

    @property
    def layer(self):
        return self._harness.get_inner_layer(self._imagep)

    def update_proc(self, layerp, gctxp):
        pass


class PebbleResourceHandle(object):
    def __init__(self, harness, file_id):
        self._harness = harness
        self.file_id = file_id
        self._handle = ffi.new(
            'struct ClayResourceHandle *', {'file_id': file_id})

    def get_handle(self):
        return self._handle

    def get_data(self):
        return self._harness.resources.get_chunk(self.file_id)
