/****************************************************************************
 * C side of the pebble application harness. All this does is load a pebble
 * app compiled with claypellet and provide access to the setup and main
 * functions from the Python code.
 ****************************************************************************/

#include <dlfcn.h>
#include "pebble_os.h"

// Undefine some macros so our typedefs don't get confused.
#undef GPoint(x, y)
#undef GSize(w, h)
#undef GRect(x, y, w, h)

#include "claypellet_harness.h"

typedef void (*pbl_main_t)(void *);

static void *app_lib;
static setup_callbacks_t setup_callbacks_func;
static pbl_main_t pbl_main_func;


void call_main(void) {
    pbl_main_func(NULL);
}

void deinit_claypellet(void) {
    dlclose(app_lib);
}

// Include our huge generated call_setup_callbacks() function.
#include "claypellet_harness_gen.c"

void init_claypellet(char *path) {
    void *func;

    app_lib = dlopen(path, RTLD_NOW);
    if (app_lib == NULL) {
        printf("Can't open library.\n");
        return;
    }

    func = dlsym(app_lib, "pbl_main");
    if (func == NULL) {
        printf("Can't load pbl_main.\n");
    } else {
        pbl_main_func = (pbl_main_t)func;
    }

    func = dlsym(app_lib, "setup_callbacks");
    if (func == NULL) {
        printf("Can't load setup_callbacks.\n");
    } else {
        setup_callbacks_func = (setup_callbacks_t)func;
    }
}
