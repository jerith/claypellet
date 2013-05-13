/***************************************************************
 * This file is automatically generated.
 ***************************************************************/


typedef void (*t_animation_init_cb)(struct Animation *animation);
typedef void (*t_animation_set_delay_cb)(struct Animation *animation, uint32_t delay_ms);
typedef void (*t_animation_set_duration_cb)(struct Animation *animation, uint32_t duration_ms);
typedef void (*t_animation_set_curve_cb)(struct Animation *animation, AnimationCurve curve);
typedef void (*t_animation_set_handlers_cb)(struct Animation *animation, AnimationHandlers callbacks, void *context);
typedef void (*t_animation_set_implementation_cb)(struct Animation *animation, const AnimationImplementation *implementation);
typedef void *(*t_animation_get_context_cb)(struct Animation *animation);
typedef void (*t_animation_schedule_cb)(struct Animation *animation);
typedef void (*t_animation_unschedule_cb)(struct Animation *animation);
typedef void (*t_animation_unschedule_all_cb)(void);
typedef bool (*t_animation_is_scheduled_cb)(struct Animation *animation);
typedef AppTimerHandle (*t_app_timer_send_event_cb)(AppContextRef app_ctx, uint32_t timeout_ms, uint32_t cookie);
typedef bool (*t_app_timer_cancel_event_cb)(AppContextRef app_ctx_ref, AppTimerHandle handle);
typedef void (*t_app_event_loop_cb)(AppTaskContextRef app_task_ctx, PebbleAppHandlers *handlers);
typedef bool (*t_bmp_init_container_cb)(int resource_id, BmpContainer *c);
typedef void (*t_bmp_deinit_container_cb)(BmpContainer *c);
typedef int32_t (*t_cos_lookup_cb)(int32_t angle);
typedef GFont (*t_fonts_get_system_font_cb)(const char *font_key);
typedef GFont (*t_fonts_load_custom_font_cb)(ResHandle resource);
typedef void (*t_fonts_unload_custom_font_cb)(GFont font);
typedef void (*t_graphics_context_set_stroke_color_cb)(GContext *ctx, GColor color);
typedef void (*t_graphics_context_set_fill_color_cb)(GContext *ctx, GColor color);
typedef void (*t_graphics_context_set_text_color_cb)(GContext *ctx, GColor color);
typedef void (*t_graphics_context_set_compositing_mode_cb)(GContext *ctx, GCompOp mode);
typedef void (*t_graphics_draw_pixel_cb)(GContext *ctx, GPoint point);
typedef void (*t_graphics_draw_line_cb)(GContext *ctx, GPoint p0, GPoint p1);
typedef void (*t_graphics_fill_rect_cb)(GContext *ctx, GRect rect, uint8_t corner_radius, GCornerMask corner_mask);
typedef void (*t_graphics_draw_circle_cb)(GContext *ctx, GPoint p, int radius);
typedef void (*t_graphics_fill_circle_cb)(GContext *ctx, GPoint p, int radius);
typedef void (*t_graphics_draw_round_rect_cb)(GContext *ctx, GRect rect, int radius);
typedef void (*t_get_time_cb)(PblTm *time);
typedef void (*t_gpath_init_cb)(GPath *path, const GPathInfo *init);
typedef void (*t_gpath_move_to_cb)(GPath *path, GPoint point);
typedef void (*t_gpath_rotate_to_cb)(GPath *path, int32_t angle);
typedef void (*t_gpath_draw_outline_cb)(GContext *ctx, GPath *path);
typedef void (*t_gpath_draw_filled_cb)(GContext *ctx, GPath *path);
typedef GPoint (*t_grect_center_point_cb)(GRect *rect);
typedef void (*t_layer_mark_dirty_cb)(Layer *layer);
typedef void (*t_layer_remove_from_parent_cb)(Layer *child);
typedef void (*t_layer_add_child_cb)(Layer *parent, Layer *child);
typedef GRect (*t_layer_get_frame_cb)(Layer *layer);
typedef void (*t_layer_set_frame_cb)(Layer *layer, GRect frame);
typedef void (*t_layer_set_hidden_cb)(Layer *layer, bool hidden);
typedef void (*t_layer_init_cb)(Layer *layer, GRect frame);
typedef void (*t_light_enable_cb)(bool enable);
typedef void (*t_light_enable_interaction_cb)(void);
typedef void (*t_psleep_cb)(int millis);
typedef void (*t_resource_init_current_app_cb)(ResVersionHandle version);
typedef ResHandle (*t_resource_get_handle_cb)(uint32_t file_id);
typedef size_t (*t_resource_load_cb)(ResHandle h, uint8_t *buffer, size_t max_length);
typedef size_t (*t_resource_load_byte_range_cb)(ResHandle h, uint32_t start_bytes, uint8_t *data, size_t num_bytes);
typedef size_t (*t_resource_size_cb)(ResHandle h);
typedef void (*t_rotbmp_deinit_container_cb)(RotBmpContainer *c);
typedef bool (*t_rotbmp_init_container_cb)(int resource_id, RotBmpContainer *c);
typedef void (*t_rotbmp_pair_deinit_container_cb)(RotBmpPairContainer *c);
typedef bool (*t_rotbmp_pair_init_container_cb)(int white_resource_id, int black_resource_id, RotBmpPairContainer *c);
typedef void (*t_rotbmp_pair_layer_set_src_ic_cb)(RotBmpPairLayer *pair, GPoint ic);
typedef void (*t_rotbmp_pair_layer_set_angle_cb)(RotBmpPairLayer *pair, int32_t angle);
typedef void (*t_window_init_cb)(Window *window, const char *debug_name);
typedef void (*t_window_stack_push_cb)(Window *window, bool animated);
typedef void (*t_window_set_click_config_provider_cb)(Window *window, ClickConfigProvider click_config_provider);
typedef void (*t_window_set_background_color_cb)(Window *window, GColor background_color);
typedef void (*t_window_render_cb)(Window *window, GContext *ctx);
typedef void (*t_window_set_fullscreen_cb)(Window *window, bool enabled);
typedef int32_t (*t_sin_lookup_cb)(int32_t angle);
typedef void (*t_string_format_time_cb)(char *ptr, size_t maxsize, const char *format, const PblTm *timeptr);
typedef void (*t_text_layer_init_cb)(TextLayer *text_layer, GRect frame);
typedef const char *(*t_text_layer_get_text_cb)(TextLayer *text_layer);
typedef void (*t_text_layer_set_text_cb)(TextLayer *text_layer, const char *text);
typedef void (*t_text_layer_set_font_cb)(TextLayer *text_layer, GFont font);
typedef void (*t_text_layer_set_text_color_cb)(TextLayer *text_layer, GColor color);
typedef void (*t_text_layer_set_background_color_cb)(TextLayer *text_layer, GColor color);
typedef void (*t_vibes_double_pulse_cb)(void);
typedef void (*t_vibes_enqueue_custom_pattern_cb)(VibePattern pattern);
typedef void (*t_vibes_long_pulse_cb)(void);
typedef void (*t_vibes_short_pulse_cb)(void);
typedef GContext *(*t_app_get_current_graphics_context_cb)(void);
typedef bool (*t_clock_is_24h_style_cb)(void);
typedef void (*t_property_animation_init_layer_frame_cb)(struct PropertyAnimation *property_animation, struct Layer *layer, GRect *from_frame, GRect *to_frame);
typedef void (*t_text_layer_set_text_alignment_cb)(TextLayer *text_layer, GTextAlignment text_alignment);
typedef void (*t_graphics_draw_bitmap_in_rect_cb)(GContext *ctx, const GBitmap *bitmap, GRect rect);
typedef void (*t_graphics_text_draw_cb)(GContext *ctx, const char *text, const GFont font, const GRect box, const GTextOverflowMode overflow_mode, const GTextAlignment alignment, const GTextLayoutCacheRef layout);
typedef void (*t_layer_set_bounds_cb)(Layer *layer, GRect bounds);
typedef GRect (*t_layer_get_bounds_cb)(Layer *layer);
typedef void (*t_layer_set_update_proc_cb)(Layer *layer, LayerUpdateProc update_proc);
typedef struct Window *(*t_layer_get_window_cb)(Layer *layer);
typedef void (*t_layer_remove_child_layers_cb)(Layer *parent);
typedef void (*t_layer_insert_below_sibling_cb)(Layer *layer_to_insert, Layer *below_sibling_layer);
typedef void (*t_layer_insert_above_sibling_cb)(Layer *layer_to_insert, Layer *above_sibling_layer);
typedef bool (*t_layer_get_hidden_cb)(Layer *layer);
typedef void (*t_layer_set_clips_cb)(Layer *layer, bool clips);
typedef bool (*t_layer_get_clips_cb)(Layer *layer);
typedef GSize (*t_text_layer_get_max_used_size_cb)(GContext *ctx, TextLayer *text_layer);
typedef void (*t_text_layer_set_size_cb)(TextLayer *text_layer, const GSize max_size);
typedef void (*t_text_layer_set_overflow_mode_cb)(TextLayer *text_layer, GTextOverflowMode line_mode);
typedef GSize (*t_graphics_text_layout_get_max_used_size_cb)(GContext *ctx, const char *text, const GFont font, const GRect box, const GTextOverflowMode overflow_mode, const GTextAlignment alignment, GTextLayoutCacheRef layout);
typedef void (*t_inverter_layer_init_cb)(InverterLayer *inverter, GRect frame);
typedef void (*t_bitmap_layer_init_cb)(BitmapLayer *image, GRect frame);
typedef void (*t_bitmap_layer_set_bitmap_cb)(BitmapLayer *image, const GBitmap *bitmap);
typedef void (*t_bitmap_layer_set_alignment_cb)(BitmapLayer *image, GAlign alignment);
typedef void (*t_bitmap_layer_set_background_color_cb)(BitmapLayer *image, GColor color);
typedef void (*t_bitmap_layer_set_compositing_mode_cb)(BitmapLayer *image, GCompOp mode);
typedef bool (*t_heap_bitmap_init_cb)(HeapBitmap *hb, int resource_id);
typedef void (*t_heap_bitmap_deinit_cb)(HeapBitmap *hb);
typedef ButtonId (*t_click_recognizer_get_button_id_cb)(ClickRecognizerRef recognizer);
typedef uint8_t (*t_click_number_of_clicks_counted_cb)(ClickRecognizerRef recognizer);
typedef void (*t_menu_cell_basic_draw_cb)(GContext *ctx, Layer *cell_layer, const char *title, const char *subtitle, GBitmap *icon);
typedef void (*t_menu_cell_title_draw_cb)(GContext *ctx, Layer *cell_layer, const char *title);
typedef void (*t_menu_cell_basic_header_draw_cb)(GContext *ctx, Layer *cell_layer, const char *title);
typedef void (*t_menu_layer_init_cb)(MenuLayer *menu_layer, GRect frame);
typedef Layer *(*t_menu_layer_get_layer_cb)(MenuLayer *menu_layer);
typedef void (*t_menu_layer_set_callbacks_cb)(MenuLayer *menu_layer, void *callback_context, MenuLayerCallbacks callbacks);
typedef void (*t_menu_layer_set_click_config_onto_window_cb)(MenuLayer *menu_layer, struct Window *window);
typedef void (*t_menu_layer_set_selected_next_cb)(MenuLayer *menu_layer, bool up, MenuRowAlign scroll_align, bool animated);
typedef void (*t_menu_layer_set_selected_index_cb)(MenuLayer *menu_layer, MenuIndex index, MenuRowAlign scroll_align, bool animated);
typedef void (*t_menu_layer_reload_data_cb)(MenuLayer *menu_layer);
typedef int16_t (*t_menu_index_compare_cb)(MenuIndex *a, MenuIndex *b);
typedef void (*t_scroll_layer_init_cb)(ScrollLayer *scroll_layer, GRect frame);
typedef void (*t_scroll_layer_add_child_cb)(ScrollLayer *scroll_layer, Layer *child);
typedef void (*t_scroll_layer_set_click_config_onto_window_cb)(ScrollLayer *scroll_layer, struct Window *window);
typedef void (*t_scroll_layer_set_callbacks_cb)(ScrollLayer *scroll_layer, ScrollLayerCallbacks callbacks);
typedef void (*t_scroll_layer_set_context_cb)(ScrollLayer *scroll_layer, void *context);
typedef void (*t_scroll_layer_set_content_offset_cb)(ScrollLayer *scroll_layer, GPoint offset, bool animated);
typedef GPoint (*t_scroll_layer_get_content_offset_cb)(ScrollLayer *scroll_layer);
typedef void (*t_scroll_layer_set_content_size_cb)(ScrollLayer *scroll_layer, GSize size);
typedef GSize (*t_scroll_layer_get_content_size_cb)(ScrollLayer *scroll_layer);
typedef void (*t_scroll_layer_set_frame_cb)(ScrollLayer *scroll_layer, GRect rect);
typedef void (*t_scroll_layer_scroll_up_click_handler_cb)(ClickRecognizerRef recognizer, ScrollLayer *scroll_layer);
typedef void (*t_scroll_layer_scroll_down_click_handler_cb)(ClickRecognizerRef recognizer, ScrollLayer *scroll_layer);
typedef void (*t_simple_menu_layer_init_cb)(SimpleMenuLayer *simple_menu, GRect frame, Window *window, const SimpleMenuSection *sections, int num_sections, void *callback_context);
typedef Layer *(*t_simple_menu_layer_get_layer_cb)(SimpleMenuLayer *simple_menu);
typedef int (*t_simple_menu_layer_get_selected_index_cb)(SimpleMenuLayer *simple_menu);
typedef void (*t_simple_menu_layer_set_selected_index_cb)(SimpleMenuLayer *simple_menu, int index, bool animated);
typedef void (*t_window_deinit_cb)(Window *window);
typedef void (*t_window_set_click_config_provider_with_context_cb)(Window *window, ClickConfigProvider click_config_provider, void *context);
typedef ClickConfigProvider (*t_window_get_click_config_provider_cb)(Window *window);
typedef void (*t_window_set_window_handlers_cb)(Window *window, WindowHandlers handlers);
typedef struct Layer *(*t_window_get_root_layer_cb)(Window *window);
typedef bool (*t_window_get_fullscreen_cb)(Window *window);
typedef void (*t_window_set_status_bar_icon_cb)(Window *window, const GBitmap *icon);
typedef bool (*t_window_is_loaded_cb)(Window *window);
typedef Window *(*t_window_stack_pop_cb)(bool animated);
typedef void (*t_window_stack_pop_all_cb)(const bool animated);
typedef bool (*t_window_stack_contains_window_cb)(Window *window);
typedef Window *(*t_window_stack_get_top_window_cb)(void);
typedef Window *(*t_window_stack_remove_cb)(Window *window, bool animated);
typedef void (*t_property_animation_init_cb)(struct PropertyAnimation *property_animation, const struct PropertyAnimationImplementation *implementation, void *subject, void *from_value, void *to_value);
typedef void (*t_property_animation_update_int16_cb)(struct PropertyAnimation *property_animation, const uint32_t time_normalized);
typedef void (*t_property_animation_update_gpoint_cb)(struct PropertyAnimation *property_animation, const uint32_t time_normalized);
typedef void (*t_property_animation_update_grect_cb)(struct PropertyAnimation *property_animation, const uint32_t time_normalized);
typedef AppMessageResult (*t_app_message_register_callbacks_cb)(AppMessageCallbacksNode *callbacks_node);
typedef AppMessageResult (*t_app_message_deregister_callbacks_cb)(AppMessageCallbacksNode *callbacks_node);
typedef AppMessageResult (*t_app_message_out_get_cb)(DictionaryIterator **iter_out);
typedef AppMessageResult (*t_app_message_out_send_cb)(void);
typedef AppMessageResult (*t_app_message_out_release_cb)(void);
typedef void (*t_app_sync_init_cb)(AppSync *s, uint8_t *buffer, const uint16_t buffer_size, const Tuplet * const keys_and_initial_values, const uint8_t count, AppSyncTupleChangedCallback tuple_changed_callback, AppSyncErrorCallback error_callback, void *context);
typedef void (*t_app_sync_deinit_cb)(AppSync *s);
typedef AppMessageResult (*t_app_sync_set_cb)(AppSync *s, const Tuplet * const keys_and_values_to_update, const uint8_t count);
typedef const Tuple *(*t_app_sync_get_cb)(const AppSync *s, const uint32_t key);
typedef DictionaryResult (*t_dict_write_begin_cb)(DictionaryIterator *iter, uint8_t * const buffer, const uint16_t size);
typedef DictionaryResult (*t_dict_write_data_cb)(DictionaryIterator *iter, const uint32_t key, const uint8_t * const data, const uint16_t size);
typedef DictionaryResult (*t_dict_write_cstring_cb)(DictionaryIterator *iter, const uint32_t key, const char * const cstring);
typedef DictionaryResult (*t_dict_write_int_cb)(DictionaryIterator *iter, const uint32_t key, const void *integer, const uint8_t width_bytes, const bool is_signed);
typedef DictionaryResult (*t_dict_write_uint8_cb)(DictionaryIterator *iter, const uint32_t key, const uint8_t value);
typedef DictionaryResult (*t_dict_write_uint16_cb)(DictionaryIterator *iter, const uint32_t key, const uint16_t value);
typedef DictionaryResult (*t_dict_write_uint32_cb)(DictionaryIterator *iter, const uint32_t key, const uint32_t value);
typedef DictionaryResult (*t_dict_write_int8_cb)(DictionaryIterator *iter, const uint32_t key, const int8_t value);
typedef DictionaryResult (*t_dict_write_int16_cb)(DictionaryIterator *iter, const uint32_t key, const int16_t value);
typedef DictionaryResult (*t_dict_write_int32_cb)(DictionaryIterator *iter, const uint32_t key, const int32_t value);
typedef uint32_t (*t_dict_write_end_cb)(DictionaryIterator *iter);
typedef Tuple *(*t_dict_read_begin_from_buffer_cb)(DictionaryIterator *iter, const uint8_t * const buffer, const uint16_t size);
typedef Tuple *(*t_dict_read_next_cb)(DictionaryIterator *iter);
typedef Tuple *(*t_dict_read_first_cb)(DictionaryIterator *iter);
typedef DictionaryResult (*t_dict_serialize_tuplets_cb)(DictionarySerializeCallback callback, void *context, const uint8_t tuplets_count, const Tuplet * const tuplets);
typedef DictionaryResult (*t_dict_serialize_tuplets_to_buffer_cb)(const uint8_t tuplets_count, const Tuplet * const tuplets, uint8_t *buffer, uint32_t *size_in_out);
typedef DictionaryResult (*t_dict_serialize_tuplets_to_buffer_with_iter_cb)(const uint8_t tuplets_count, const Tuplet * const tuplets, DictionaryIterator *iter, uint8_t *buffer, uint32_t *size_in_out);
typedef DictionaryResult (*t_dict_write_tuplet_cb)(DictionaryIterator *iter, const Tuplet * const tuplet);
typedef uint32_t (*t_dict_calc_buffer_size_from_tuplets_cb)(const uint8_t tuplets_count, const Tuplet * const tuplets);
typedef DictionaryResult (*t_dict_merge_cb)(DictionaryIterator *dest, uint32_t *dest_max_size_in_out, DictionaryIterator *source, const bool update_existing_keys_only, const DictionaryKeyUpdatedCallback key_callback, void *context);
typedef Tuple *(*t_dict_find_cb)(const DictionaryIterator *iter, const uint32_t key);
typedef void (*t_action_bar_layer_init_cb)(ActionBarLayer *action_bar);
typedef void (*t_action_bar_layer_set_context_cb)(ActionBarLayer *action_bar, void *context);
typedef void (*t_action_bar_layer_set_click_config_provider_cb)(ActionBarLayer *action_bar, ClickConfigProvider click_config_provider);
typedef void (*t_action_bar_layer_set_icon_cb)(ActionBarLayer *action_bar, ButtonId button_id, const GBitmap *icon);
typedef void (*t_action_bar_layer_clear_icon_cb)(ActionBarLayer *action_bar, ButtonId button_id);
typedef void (*t_action_bar_layer_add_to_window_cb)(ActionBarLayer *action_bar, struct Window *window);
typedef void (*t_action_bar_layer_remove_from_window_cb)(ActionBarLayer *action_bar);
typedef void (*t_action_bar_layer_set_background_color_cb)(ActionBarLayer *action_bar, GColor background_color);
typedef void (*t_number_window_init_cb)(NumberWindow *numberwindow, const char *label, NumberWindowCallbacks callbacks, void *callback_context);
typedef void (*t_number_window_set_label_cb)(NumberWindow *nw, const char *label);
typedef void (*t_number_window_set_max_cb)(NumberWindow *numberwindow, int max);
typedef void (*t_number_window_set_min_cb)(NumberWindow *numberwindow, int min);
typedef void (*t_number_window_set_value_cb)(NumberWindow *numberwindow, int value);
typedef void (*t_number_window_set_step_size_cb)(NumberWindow *numberwindow, int step);
typedef int (*t_number_window_get_value_cb)(NumberWindow *numberwindow);
typedef void (*t_clock_copy_time_string_cb)(char *buffer, uint8_t size);

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

struct ClayGraphicsContext {
    uint32_t gctx_id;
};
