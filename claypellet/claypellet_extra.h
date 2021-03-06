/***************************************************************************
 * This file (claypellet_extra.h) is included as-is in claypellet.h when it
 * gets generated.
 ***************************************************************************/

void call_main(AppContextRef app_ctx);
void deinit_claypellet(void);
int init_claypellet(char *path);

struct ClayResourceHandle {
    uint32_t file_id;
};

struct ClayFontHandle {
    bool custom;
    uint32_t file_id;
};

struct ClayGraphicsContext {
    uint32_t gctx_id;
};
