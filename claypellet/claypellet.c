#include "pebble_os.h"
#include "pebble_app.h"
#include "pebble_fonts.h"


typedef void (*t_app_event_loop_cb)(AppTaskContextRef app_task_ctx, PebbleAppHandlers *handlers);
typedef void (*t_window_init_cb)(Window *window, const char *debug_name);

t_app_event_loop_cb app_event_loop_cb;
t_window_init_cb window_init_cb;

void setup_callbacks(t_app_event_loop_cb app_event_loop, t_window_init_cb window_init) {
    app_event_loop_cb = app_event_loop;
    window_init_cb = window_init;
}


void animation_init(struct Animation *animation) {}
void animation_set_delay(struct Animation *animation, uint32_t delay_ms) {}
void animation_set_duration(struct Animation *animation, uint32_t duration_ms) {}
void animation_set_curve(struct Animation *animation, AnimationCurve curve) {}
void animation_set_handlers(struct Animation *animation, AnimationHandlers callbacks, void *context) {}
void animation_set_implementation(struct Animation *animation, const AnimationImplementation *implementation) {}
void *animation_get_context(struct Animation *animation) { return NULL; }
void animation_schedule(struct Animation *animation) {}
void animation_unschedule(struct Animation *animation) {}
void animation_unschedule_all(void) {}
bool animation_is_scheduled(struct Animation *animation) { return NULL; }
AppTimerHandle app_timer_send_event(AppContextRef app_ctx, uint32_t timeout_ms, uint32_t cookie) { return 0; }
bool app_timer_cancel_event(AppContextRef app_ctx_ref, AppTimerHandle handle) { return NULL; }
bool bmp_init_container(int resource_id, BmpContainer *c) { return NULL; }
void bmp_deinit_container(BmpContainer *c) {}
int32_t cos_lookup(int32_t angle) { return 0; }
GFont fonts_get_system_font(const char *font_key) { return NULL; }
GFont fonts_load_custom_font(ResHandle resource) { return NULL; }
void fonts_unload_custom_font(GFont font) {}
void graphics_context_set_stroke_color(GContext *ctx, GColor color) {}
void graphics_context_set_fill_color(GContext *ctx, GColor color) {}
void graphics_context_set_text_color(GContext *ctx, GColor color) {}
void graphics_context_set_compositing_mode(GContext *ctx, GCompOp mode) {}
void graphics_draw_pixel(GContext *ctx, GPoint point) {}
void graphics_draw_line(GContext *ctx, GPoint p0, GPoint p1) {}
void graphics_fill_rect(GContext *ctx, GRect rect, uint8_t corner_radius, GCornerMask corner_mask) {}
void graphics_draw_circle(GContext *ctx, GPoint p, int radius) {}
void graphics_fill_circle(GContext *ctx, GPoint p, int radius) {}
void graphics_draw_round_rect(GContext *ctx, GRect rect, int radius) {}
void get_time(PblTm *time) {}
void gpath_init(GPath *path, const GPathInfo *init) {}
void gpath_move_to(GPath *path, GPoint point) {}
void gpath_rotate_to(GPath *path, int32_t angle) {}
void gpath_draw_outline(GContext *ctx, GPath *path) {}
void gpath_draw_filled(GContext *ctx, GPath *path) {}
GPoint grect_center_point(GRect *rect) { return GPoint(0, 0); }
void layer_mark_dirty(Layer *layer) {}
void layer_remove_from_parent(Layer *child) {}
void layer_add_child(Layer *parent, Layer *child) {}
GRect layer_get_frame(Layer *layer) { return GRectZero; }
void layer_set_frame(Layer *layer, GRect frame) {}
void layer_set_hidden(Layer *layer, bool hidden) {}
void layer_init(Layer *layer, GRect frame) {}
void light_enable(bool enable) {}
void light_enable_interaction(void) {}
void psleep(int millis) {}
void resource_init_current_app(ResVersionHandle version) {}
ResHandle resource_get_handle(uint32_t file_id) { return NULL; }
size_t resource_load(ResHandle h, uint8_t *buffer, size_t max_length) { return 0; }
size_t resource_load_byte_range(ResHandle h, uint32_t start_bytes, uint8_t *data, size_t num_bytes) { return 0; }
size_t resource_size(ResHandle h) { return 0; }
void rotbmp_deinit_container(RotBmpContainer *c) {}
bool rotbmp_init_container(int resource_id, RotBmpContainer *c) { return NULL; }
void rotbmp_pair_deinit_container(RotBmpPairContainer *c) {}
bool rotbmp_pair_init_container(int white_resource_id, int black_resource_id, RotBmpPairContainer *c) { return NULL; }
void rotbmp_pair_layer_set_src_ic(RotBmpPairLayer *pair, GPoint ic) {}
void rotbmp_pair_layer_set_angle(RotBmpPairLayer *pair, int32_t angle) {}
void window_stack_push(Window *window, bool animated) {}
void window_set_click_config_provider(Window *window, ClickConfigProvider click_config_provider) {}
void window_set_background_color(Window *window, GColor background_color) {}
void window_render(Window *window, GContext *ctx) {}
void window_set_fullscreen(Window *window, bool enabled) {}
int32_t sin_lookup(int32_t angle) { return 0; }
void string_format_time(char *ptr, size_t maxsize, const char *format, const PblTm *timeptr) {}
void text_layer_init(TextLayer *text_layer, GRect frame) {}
const char *text_layer_get_text(TextLayer *text_layer) { return NULL; }
void text_layer_set_text(TextLayer *text_layer, const char *text) {}
void text_layer_set_font(TextLayer *text_layer, GFont font) {}
void text_layer_set_text_color(TextLayer *text_layer, GColor color) {}
void text_layer_set_background_color(TextLayer *text_layer, GColor color) {}
void vibes_double_pulse(void) {}
void vibes_enqueue_custom_pattern(VibePattern pattern) {}
void vibes_long_pulse(void) {}
void vibes_short_pulse(void) {}
GContext *app_get_current_graphics_context(void) { return NULL; }
bool clock_is_24h_style(void) { return NULL; }
void property_animation_init_layer_frame(struct PropertyAnimation *property_animation, struct Layer *layer, GRect *from_frame, GRect *to_frame) {}
void text_layer_set_text_alignment(TextLayer *text_layer, GTextAlignment text_alignment) {}
void graphics_draw_bitmap_in_rect(GContext *ctx, const GBitmap *bitmap, GRect rect) {}
void graphics_text_draw(GContext *ctx, const char *text, const GFont font, const GRect box, const GTextOverflowMode overflow_mode, const GTextAlignment alignment, const GTextLayoutCacheRef layout) {}
void layer_set_bounds(Layer *layer, GRect bounds) {}
GRect layer_get_bounds(Layer *layer) { return GRectZero; }
void layer_set_update_proc(Layer *layer, LayerUpdateProc update_proc) {}
struct Window *layer_get_window(Layer *layer) { return NULL; }
void layer_remove_child_layers(Layer *parent) {}
void layer_insert_below_sibling(Layer *layer_to_insert, Layer *below_sibling_layer) {}
void layer_insert_above_sibling(Layer *layer_to_insert, Layer *above_sibling_layer) {}
bool layer_get_hidden(Layer *layer) { return NULL; }
void layer_set_clips(Layer *layer, bool clips) {}
bool layer_get_clips(Layer *layer) { return NULL; }
GSize text_layer_get_max_used_size(GContext *ctx, TextLayer *text_layer) { return GSize(0, 0); }
void text_layer_set_size(TextLayer *text_layer, const GSize max_size) {}
void text_layer_set_overflow_mode(TextLayer *text_layer, GTextOverflowMode line_mode) {}
GSize graphics_text_layout_get_max_used_size(GContext *ctx, const char *text, const GFont font, const GRect box, const GTextOverflowMode overflow_mode, const GTextAlignment alignment, GTextLayoutCacheRef layout) { return GSize(0, 0); }
void inverter_layer_init(InverterLayer *inverter, GRect frame) {}
void bitmap_layer_init(BitmapLayer *image, GRect frame) {}
void bitmap_layer_set_bitmap(BitmapLayer *image, const GBitmap *bitmap) {}
void bitmap_layer_set_alignment(BitmapLayer *image, GAlign alignment) {}
void bitmap_layer_set_background_color(BitmapLayer *image, GColor color) {}
void bitmap_layer_set_compositing_mode(BitmapLayer *image, GCompOp mode) {}
bool heap_bitmap_init(HeapBitmap *hb, int resource_id) { return NULL; }
void heap_bitmap_deinit(HeapBitmap *hb) {}
ButtonId click_recognizer_get_button_id(ClickRecognizerRef recognizer) { return 0; }
uint8_t click_number_of_clicks_counted(ClickRecognizerRef recognizer) { return 0; }
void menu_cell_basic_draw(GContext *ctx, Layer *cell_layer, const char *title, const char *subtitle, GBitmap *icon) {}
void menu_cell_title_draw(GContext *ctx, Layer *cell_layer, const char *title) {}
void menu_cell_basic_header_draw(GContext *ctx, Layer *cell_layer, const char *title) {}
void menu_layer_init(MenuLayer *menu_layer, GRect frame) {}
Layer *menu_layer_get_layer(MenuLayer *menu_layer) { return NULL; }
void menu_layer_set_callbacks(MenuLayer *menu_layer, void *callback_context, MenuLayerCallbacks callbacks) {}
void menu_layer_set_click_config_onto_window(MenuLayer *menu_layer, struct Window *window) {}
void menu_layer_set_selected_next(MenuLayer *menu_layer, bool up, MenuRowAlign scroll_align, bool animated) {}
void menu_layer_set_selected_index(MenuLayer *menu_layer, MenuIndex index, MenuRowAlign scroll_align, bool animated) {}
void menu_layer_reload_data(MenuLayer *menu_layer) {}
int16_t menu_index_compare(MenuIndex *a, MenuIndex *b) { return 0; }
void scroll_layer_init(ScrollLayer *scroll_layer, GRect frame) {}
void scroll_layer_add_child(ScrollLayer *scroll_layer, Layer *child) {}
void scroll_layer_set_click_config_onto_window(ScrollLayer *scroll_layer, struct Window *window) {}
void scroll_layer_set_callbacks(ScrollLayer *scroll_layer, ScrollLayerCallbacks callbacks) {}
void scroll_layer_set_context(ScrollLayer *scroll_layer, void *context) {}
void scroll_layer_set_content_offset(ScrollLayer *scroll_layer, GPoint offset, bool animated) {}
GPoint scroll_layer_get_content_offset(ScrollLayer *scroll_layer) { return GPoint(0, 0); }
void scroll_layer_set_content_size(ScrollLayer *scroll_layer, GSize size) {}
GSize scroll_layer_get_content_size(ScrollLayer *scroll_layer) { return GSize(0, 0); }
void scroll_layer_set_frame(ScrollLayer *scroll_layer, GRect rect) {}
void scroll_layer_scroll_up_click_handler(ClickRecognizerRef recognizer, ScrollLayer *scroll_layer) {}
void scroll_layer_scroll_down_click_handler(ClickRecognizerRef recognizer, ScrollLayer *scroll_layer) {}
void simple_menu_layer_init(SimpleMenuLayer *simple_menu, GRect frame, Window *window, const SimpleMenuSection *sections, int num_sections, void *callback_context) {}
Layer *simple_menu_layer_get_layer(SimpleMenuLayer *simple_menu) { return NULL; }
int simple_menu_layer_get_selected_index(SimpleMenuLayer *simple_menu) { return 0; }
void simple_menu_layer_set_selected_index(SimpleMenuLayer *simple_menu, int index, bool animated) {}
void window_deinit(Window *window) {}
void window_set_click_config_provider_with_context(Window *window, ClickConfigProvider click_config_provider, void *context) {}
ClickConfigProvider window_get_click_config_provider(Window *window) { return NULL; }
void window_set_window_handlers(Window *window, WindowHandlers handlers) {}
struct Layer *window_get_root_layer(Window *window) { return NULL; }
bool window_get_fullscreen(Window *window) { return NULL; }
void window_set_status_bar_icon(Window *window, const GBitmap *icon) {}
bool window_is_loaded(Window *window) { return NULL; }
Window *window_stack_pop(bool animated) { return NULL; }
void window_stack_pop_all(const bool animated) {}
bool window_stack_contains_window(Window *window) { return NULL; }
Window *window_stack_get_top_window(void) { return NULL; }
Window *window_stack_remove(Window *window, bool animated) { return NULL; }
void property_animation_init(struct PropertyAnimation *property_animation, const struct PropertyAnimationImplementation *implementation, void *subject, void *from_value, void *to_value) {}
void property_animation_update_int16(struct PropertyAnimation *property_animation, const uint32_t time_normalized) {}
void property_animation_update_gpoint(struct PropertyAnimation *property_animation, const uint32_t time_normalized) {}
void property_animation_update_grect(struct PropertyAnimation *property_animation, const uint32_t time_normalized) {}
AppMessageResult app_message_register_callbacks(AppMessageCallbacksNode *callbacks_node) { return 0; }
AppMessageResult app_message_deregister_callbacks(AppMessageCallbacksNode *callbacks_node) { return 0; }
AppMessageResult app_message_out_get(DictionaryIterator **iter_out) { return 0; }
AppMessageResult app_message_out_send(void) { return 0; }
AppMessageResult app_message_out_release(void) { return 0; }
void app_sync_init(AppSync *s, uint8_t *buffer, const uint16_t buffer_size, const Tuplet * const keys_and_initial_values, const uint8_t count, AppSyncTupleChangedCallback tuple_changed_callback, AppSyncErrorCallback error_callback, void *context) {}
void app_sync_deinit(AppSync *s) {}
AppMessageResult app_sync_set(AppSync *s, const Tuplet * const keys_and_values_to_update, const uint8_t count) { return 0; }
const Tuple *app_sync_get(const AppSync *s, const uint32_t key) { return NULL; }
uint32_t dict_calc_buffer_size(const uint8_t tuple_count, ...) { return 0; }
DictionaryResult dict_write_begin(DictionaryIterator *iter, uint8_t * const buffer, const uint16_t size) { return 0; }
DictionaryResult dict_write_data(DictionaryIterator *iter, const uint32_t key, const uint8_t * const data, const uint16_t size) { return 0; }
DictionaryResult dict_write_cstring(DictionaryIterator *iter, const uint32_t key, const char * const cstring) { return 0; }
DictionaryResult dict_write_int(DictionaryIterator *iter, const uint32_t key, const void *integer, const uint8_t width_bytes, const bool is_signed) { return 0; }
DictionaryResult dict_write_uint8(DictionaryIterator *iter, const uint32_t key, const uint8_t value) { return 0; }
DictionaryResult dict_write_uint16(DictionaryIterator *iter, const uint32_t key, const uint16_t value) { return 0; }
DictionaryResult dict_write_uint32(DictionaryIterator *iter, const uint32_t key, const uint32_t value) { return 0; }
DictionaryResult dict_write_int8(DictionaryIterator *iter, const uint32_t key, const int8_t value) { return 0; }
DictionaryResult dict_write_int16(DictionaryIterator *iter, const uint32_t key, const int16_t value) { return 0; }
DictionaryResult dict_write_int32(DictionaryIterator *iter, const uint32_t key, const int32_t value) { return 0; }
uint32_t dict_write_end(DictionaryIterator *iter) { return 0; }
Tuple *dict_read_begin_from_buffer(DictionaryIterator *iter, const uint8_t * const buffer, const uint16_t size) { return NULL; }
Tuple *dict_read_next(DictionaryIterator *iter) { return NULL; }
Tuple *dict_read_first(DictionaryIterator *iter) { return NULL; }
DictionaryResult dict_serialize_tuplets(DictionarySerializeCallback callback, void *context, const uint8_t tuplets_count, const Tuplet * const tuplets) { return 0; }
DictionaryResult dict_serialize_tuplets_to_buffer(const uint8_t tuplets_count, const Tuplet * const tuplets, uint8_t *buffer, uint32_t *size_in_out) { return 0; }
DictionaryResult dict_serialize_tuplets_to_buffer_with_iter(const uint8_t tuplets_count, const Tuplet * const tuplets, DictionaryIterator *iter, uint8_t *buffer, uint32_t *size_in_out) { return 0; }
DictionaryResult dict_write_tuplet(DictionaryIterator *iter, const Tuplet * const tuplet) { return 0; }
uint32_t dict_calc_buffer_size_from_tuplets(const uint8_t tuplets_count, const Tuplet * const tuplets) { return 0; }
DictionaryResult dict_merge(DictionaryIterator *dest, uint32_t *dest_max_size_in_out, DictionaryIterator *source, const bool update_existing_keys_only, const DictionaryKeyUpdatedCallback key_callback, void *context) { return 0; }
Tuple *dict_find(const DictionaryIterator *iter, const uint32_t key) { return NULL; }
void action_bar_layer_init(ActionBarLayer *action_bar) {}
void action_bar_layer_set_context(ActionBarLayer *action_bar, void *context) {}
void action_bar_layer_set_click_config_provider(ActionBarLayer *action_bar, ClickConfigProvider click_config_provider) {}
void action_bar_layer_set_icon(ActionBarLayer *action_bar, ButtonId button_id, const GBitmap *icon) {}
void action_bar_layer_clear_icon(ActionBarLayer *action_bar, ButtonId button_id) {}
void action_bar_layer_add_to_window(ActionBarLayer *action_bar, struct Window *window) {}
void action_bar_layer_remove_from_window(ActionBarLayer *action_bar) {}
void action_bar_layer_set_background_color(ActionBarLayer *action_bar, GColor background_color) {}
void number_window_init(NumberWindow *numberwindow, const char *label, NumberWindowCallbacks callbacks, void *callback_context) {}
void number_window_set_label(NumberWindow *nw, const char *label) {}
void number_window_set_max(NumberWindow *numberwindow, int max) {}
void number_window_set_min(NumberWindow *numberwindow, int min) {}
void number_window_set_value(NumberWindow *numberwindow, int value) {}
void number_window_set_step_size(NumberWindow *numberwindow, int step) {}
int number_window_get_value(NumberWindow *numberwindow) { return 0; }
void clock_copy_time_string(char *buffer, uint8_t size) {}

void app_event_loop(AppTaskContextRef app_task_ctx, PebbleAppHandlers *handlers) {
    app_event_loop_cb(app_task_ctx, handlers);
}

void window_init(Window *window, const char *debug_name) {
    window_init_cb(window, debug_name);
}
