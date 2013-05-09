#################################################################
# This file is automatically generated.
#################################################################


class PebbleHarnessBase(object):
    def setup_callbacks(self):
        self._callbacks = [
            self._mkcallback('animation_init'),
            self._mkcallback('animation_set_delay'),
            self._mkcallback('animation_set_duration'),
            self._mkcallback('animation_set_curve'),
            self._mkcallback('animation_set_handlers'),
            self._mkcallback('animation_set_implementation'),
            self._mkcallback('animation_get_context'),
            self._mkcallback('animation_schedule'),
            self._mkcallback('animation_unschedule'),
            self._mkcallback('animation_unschedule_all'),
            self._mkcallback('animation_is_scheduled'),
            self._mkcallback('app_timer_send_event'),
            self._mkcallback('app_timer_cancel_event'),
            self._mkcallback('app_event_loop'),
            self._mkcallback('bmp_init_container'),
            self._mkcallback('bmp_deinit_container'),
            self._mkcallback('cos_lookup'),
            self._mkcallback('fonts_get_system_font'),
            self._mkcallback('fonts_load_custom_font'),
            self._mkcallback('fonts_unload_custom_font'),
            self._mkcallback('graphics_context_set_stroke_color'),
            self._mkcallback('graphics_context_set_fill_color'),
            self._mkcallback('graphics_context_set_text_color'),
            self._mkcallback('graphics_context_set_compositing_mode'),
            self._mkcallback('graphics_draw_pixel'),
            self._mkcallback('graphics_draw_line'),
            self._mkcallback('graphics_fill_rect'),
            self._mkcallback('graphics_draw_circle'),
            self._mkcallback('graphics_fill_circle'),
            self._mkcallback('graphics_draw_round_rect'),
            self._mkcallback('get_time'),
            self._mkcallback('gpath_init'),
            self._mkcallback('gpath_move_to'),
            self._mkcallback('gpath_rotate_to'),
            self._mkcallback('gpath_draw_outline'),
            self._mkcallback('gpath_draw_filled'),
            self._mkcallback('grect_center_point'),
            self._mkcallback('layer_mark_dirty'),
            self._mkcallback('layer_remove_from_parent'),
            self._mkcallback('layer_add_child'),
            self._mkcallback('layer_get_frame'),
            self._mkcallback('layer_set_frame'),
            self._mkcallback('layer_set_hidden'),
            self._mkcallback('layer_init'),
            self._mkcallback('light_enable'),
            self._mkcallback('light_enable_interaction'),
            self._mkcallback('psleep'),
            self._mkcallback('resource_init_current_app'),
            self._mkcallback('resource_get_handle'),
            self._mkcallback('resource_load'),
            self._mkcallback('resource_load_byte_range'),
            self._mkcallback('resource_size'),
            self._mkcallback('rotbmp_deinit_container'),
            self._mkcallback('rotbmp_init_container'),
            self._mkcallback('rotbmp_pair_deinit_container'),
            self._mkcallback('rotbmp_pair_init_container'),
            self._mkcallback('rotbmp_pair_layer_set_src_ic'),
            self._mkcallback('rotbmp_pair_layer_set_angle'),
            self._mkcallback('window_init'),
            self._mkcallback('window_stack_push'),
            self._mkcallback('window_set_click_config_provider'),
            self._mkcallback('window_set_background_color'),
            self._mkcallback('window_render'),
            self._mkcallback('window_set_fullscreen'),
            self._mkcallback('sin_lookup'),
            self._mkcallback('string_format_time'),
            self._mkcallback('text_layer_init'),
            self._mkcallback('text_layer_get_text'),
            self._mkcallback('text_layer_set_text'),
            self._mkcallback('text_layer_set_font'),
            self._mkcallback('text_layer_set_text_color'),
            self._mkcallback('text_layer_set_background_color'),
            self._mkcallback('vibes_double_pulse'),
            self._mkcallback('vibes_enqueue_custom_pattern'),
            self._mkcallback('vibes_long_pulse'),
            self._mkcallback('vibes_short_pulse'),
            self._mkcallback('app_get_current_graphics_context'),
            self._mkcallback('clock_is_24h_style'),
            self._mkcallback('property_animation_init_layer_frame'),
            self._mkcallback('text_layer_set_text_alignment'),
            self._mkcallback('graphics_draw_bitmap_in_rect'),
            self._mkcallback('graphics_text_draw'),
            self._mkcallback('layer_set_bounds'),
            self._mkcallback('layer_get_bounds'),
            self._mkcallback('layer_set_update_proc'),
            self._mkcallback('layer_get_window'),
            self._mkcallback('layer_remove_child_layers'),
            self._mkcallback('layer_insert_below_sibling'),
            self._mkcallback('layer_insert_above_sibling'),
            self._mkcallback('layer_get_hidden'),
            self._mkcallback('layer_set_clips'),
            self._mkcallback('layer_get_clips'),
            self._mkcallback('text_layer_get_max_used_size'),
            self._mkcallback('text_layer_set_size'),
            self._mkcallback('text_layer_set_overflow_mode'),
            self._mkcallback('graphics_text_layout_get_max_used_size'),
            self._mkcallback('inverter_layer_init'),
            self._mkcallback('bitmap_layer_init'),
            self._mkcallback('bitmap_layer_set_bitmap'),
            self._mkcallback('bitmap_layer_set_alignment'),
            self._mkcallback('bitmap_layer_set_background_color'),
            self._mkcallback('bitmap_layer_set_compositing_mode'),
            self._mkcallback('heap_bitmap_init'),
            self._mkcallback('heap_bitmap_deinit'),
            self._mkcallback('click_recognizer_get_button_id'),
            self._mkcallback('click_number_of_clicks_counted'),
            self._mkcallback('menu_cell_basic_draw'),
            self._mkcallback('menu_cell_title_draw'),
            self._mkcallback('menu_cell_basic_header_draw'),
            self._mkcallback('menu_layer_init'),
            self._mkcallback('menu_layer_get_layer'),
            self._mkcallback('menu_layer_set_callbacks'),
            self._mkcallback('menu_layer_set_click_config_onto_window'),
            self._mkcallback('menu_layer_set_selected_next'),
            self._mkcallback('menu_layer_set_selected_index'),
            self._mkcallback('menu_layer_reload_data'),
            self._mkcallback('menu_index_compare'),
            self._mkcallback('scroll_layer_init'),
            self._mkcallback('scroll_layer_add_child'),
            self._mkcallback('scroll_layer_set_click_config_onto_window'),
            self._mkcallback('scroll_layer_set_callbacks'),
            self._mkcallback('scroll_layer_set_context'),
            self._mkcallback('scroll_layer_set_content_offset'),
            self._mkcallback('scroll_layer_get_content_offset'),
            self._mkcallback('scroll_layer_set_content_size'),
            self._mkcallback('scroll_layer_get_content_size'),
            self._mkcallback('scroll_layer_set_frame'),
            self._mkcallback('scroll_layer_scroll_up_click_handler'),
            self._mkcallback('scroll_layer_scroll_down_click_handler'),
            self._mkcallback('simple_menu_layer_init'),
            self._mkcallback('simple_menu_layer_get_layer'),
            self._mkcallback('simple_menu_layer_get_selected_index'),
            self._mkcallback('simple_menu_layer_set_selected_index'),
            self._mkcallback('window_deinit'),
            self._mkcallback('window_set_click_config_provider_with_context'),
            self._mkcallback('window_get_click_config_provider'),
            self._mkcallback('window_set_window_handlers'),
            self._mkcallback('window_get_root_layer'),
            self._mkcallback('window_get_fullscreen'),
            self._mkcallback('window_set_status_bar_icon'),
            self._mkcallback('window_is_loaded'),
            self._mkcallback('window_stack_pop'),
            self._mkcallback('window_stack_pop_all'),
            self._mkcallback('window_stack_contains_window'),
            self._mkcallback('window_stack_get_top_window'),
            self._mkcallback('window_stack_remove'),
            self._mkcallback('property_animation_init'),
            self._mkcallback('property_animation_update_int16'),
            self._mkcallback('property_animation_update_gpoint'),
            self._mkcallback('property_animation_update_grect'),
            self._mkcallback('app_message_register_callbacks'),
            self._mkcallback('app_message_deregister_callbacks'),
            self._mkcallback('app_message_out_get'),
            self._mkcallback('app_message_out_send'),
            self._mkcallback('app_message_out_release'),
            self._mkcallback('app_sync_init'),
            self._mkcallback('app_sync_deinit'),
            self._mkcallback('app_sync_set'),
            self._mkcallback('app_sync_get'),
            self._mkcallback('dict_write_begin'),
            self._mkcallback('dict_write_data'),
            self._mkcallback('dict_write_cstring'),
            self._mkcallback('dict_write_int'),
            self._mkcallback('dict_write_uint8'),
            self._mkcallback('dict_write_uint16'),
            self._mkcallback('dict_write_uint32'),
            self._mkcallback('dict_write_int8'),
            self._mkcallback('dict_write_int16'),
            self._mkcallback('dict_write_int32'),
            self._mkcallback('dict_write_end'),
            self._mkcallback('dict_read_begin_from_buffer'),
            self._mkcallback('dict_read_next'),
            self._mkcallback('dict_read_first'),
            self._mkcallback('dict_serialize_tuplets'),
            self._mkcallback('dict_serialize_tuplets_to_buffer'),
            self._mkcallback('dict_serialize_tuplets_to_buffer_with_iter'),
            self._mkcallback('dict_write_tuplet'),
            self._mkcallback('dict_calc_buffer_size_from_tuplets'),
            self._mkcallback('dict_merge'),
            self._mkcallback('dict_find'),
            self._mkcallback('action_bar_layer_init'),
            self._mkcallback('action_bar_layer_set_context'),
            self._mkcallback('action_bar_layer_set_click_config_provider'),
            self._mkcallback('action_bar_layer_set_icon'),
            self._mkcallback('action_bar_layer_clear_icon'),
            self._mkcallback('action_bar_layer_add_to_window'),
            self._mkcallback('action_bar_layer_remove_from_window'),
            self._mkcallback('action_bar_layer_set_background_color'),
            self._mkcallback('number_window_init'),
            self._mkcallback('number_window_set_label'),
            self._mkcallback('number_window_set_max'),
            self._mkcallback('number_window_set_min'),
            self._mkcallback('number_window_set_value'),
            self._mkcallback('number_window_set_step_size'),
            self._mkcallback('number_window_get_value'),
            self._mkcallback('clock_copy_time_string'),
        ]

    def animation_init(self, animation):
        raise NotImplementedError("animation_init")

    def animation_set_delay(self, animation, delay_ms):
        raise NotImplementedError("animation_set_delay")

    def animation_set_duration(self, animation, duration_ms):
        raise NotImplementedError("animation_set_duration")

    def animation_set_curve(self, animation, curve):
        raise NotImplementedError("animation_set_curve")

    def animation_set_handlers(self, animation, callbacks, context):
        raise NotImplementedError("animation_set_handlers")

    def animation_set_implementation(self, animation, implementation):
        raise NotImplementedError("animation_set_implementation")

    def animation_get_context(self, animation):
        raise NotImplementedError("animation_get_context")

    def animation_schedule(self, animation):
        raise NotImplementedError("animation_schedule")

    def animation_unschedule(self, animation):
        raise NotImplementedError("animation_unschedule")

    def animation_unschedule_all(self):
        raise NotImplementedError("animation_unschedule_all")

    def animation_is_scheduled(self, animation):
        raise NotImplementedError("animation_is_scheduled")

    def app_timer_send_event(self, app_ctx, timeout_ms, cookie):
        raise NotImplementedError("app_timer_send_event")

    def app_timer_cancel_event(self, app_ctx_ref, handle):
        raise NotImplementedError("app_timer_cancel_event")

    def app_event_loop(self, app_task_ctx, handlers):
        raise NotImplementedError("app_event_loop")

    def bmp_init_container(self, resource_id, c):
        raise NotImplementedError("bmp_init_container")

    def bmp_deinit_container(self, c):
        raise NotImplementedError("bmp_deinit_container")

    def cos_lookup(self, angle):
        raise NotImplementedError("cos_lookup")

    def fonts_get_system_font(self, font_key):
        raise NotImplementedError("fonts_get_system_font")

    def fonts_load_custom_font(self, resource):
        raise NotImplementedError("fonts_load_custom_font")

    def fonts_unload_custom_font(self, font):
        raise NotImplementedError("fonts_unload_custom_font")

    def graphics_context_set_stroke_color(self, ctx, color):
        raise NotImplementedError("graphics_context_set_stroke_color")

    def graphics_context_set_fill_color(self, ctx, color):
        raise NotImplementedError("graphics_context_set_fill_color")

    def graphics_context_set_text_color(self, ctx, color):
        raise NotImplementedError("graphics_context_set_text_color")

    def graphics_context_set_compositing_mode(self, ctx, mode):
        raise NotImplementedError("graphics_context_set_compositing_mode")

    def graphics_draw_pixel(self, ctx, point):
        raise NotImplementedError("graphics_draw_pixel")

    def graphics_draw_line(self, ctx, p0, p1):
        raise NotImplementedError("graphics_draw_line")

    def graphics_fill_rect(self, ctx, rect, corner_radius, corner_mask):
        raise NotImplementedError("graphics_fill_rect")

    def graphics_draw_circle(self, ctx, p, radius):
        raise NotImplementedError("graphics_draw_circle")

    def graphics_fill_circle(self, ctx, p, radius):
        raise NotImplementedError("graphics_fill_circle")

    def graphics_draw_round_rect(self, ctx, rect, radius):
        raise NotImplementedError("graphics_draw_round_rect")

    def get_time(self, time):
        raise NotImplementedError("get_time")

    def gpath_init(self, path, init):
        raise NotImplementedError("gpath_init")

    def gpath_move_to(self, path, point):
        raise NotImplementedError("gpath_move_to")

    def gpath_rotate_to(self, path, angle):
        raise NotImplementedError("gpath_rotate_to")

    def gpath_draw_outline(self, ctx, path):
        raise NotImplementedError("gpath_draw_outline")

    def gpath_draw_filled(self, ctx, path):
        raise NotImplementedError("gpath_draw_filled")

    def grect_center_point(self, rect):
        raise NotImplementedError("grect_center_point")

    def layer_mark_dirty(self, layer):
        raise NotImplementedError("layer_mark_dirty")

    def layer_remove_from_parent(self, child):
        raise NotImplementedError("layer_remove_from_parent")

    def layer_add_child(self, parent, child):
        raise NotImplementedError("layer_add_child")

    def layer_get_frame(self, layer):
        raise NotImplementedError("layer_get_frame")

    def layer_set_frame(self, layer, frame):
        raise NotImplementedError("layer_set_frame")

    def layer_set_hidden(self, layer, hidden):
        raise NotImplementedError("layer_set_hidden")

    def layer_init(self, layer, frame):
        raise NotImplementedError("layer_init")

    def light_enable(self, enable):
        raise NotImplementedError("light_enable")

    def light_enable_interaction(self):
        raise NotImplementedError("light_enable_interaction")

    def psleep(self, millis):
        raise NotImplementedError("psleep")

    def resource_init_current_app(self, version):
        raise NotImplementedError("resource_init_current_app")

    def resource_get_handle(self, file_id):
        raise NotImplementedError("resource_get_handle")

    def resource_load(self, h, buffer, max_length):
        raise NotImplementedError("resource_load")

    def resource_load_byte_range(self, h, start_bytes, data, num_bytes):
        raise NotImplementedError("resource_load_byte_range")

    def resource_size(self, h):
        raise NotImplementedError("resource_size")

    def rotbmp_deinit_container(self, c):
        raise NotImplementedError("rotbmp_deinit_container")

    def rotbmp_init_container(self, resource_id, c):
        raise NotImplementedError("rotbmp_init_container")

    def rotbmp_pair_deinit_container(self, c):
        raise NotImplementedError("rotbmp_pair_deinit_container")

    def rotbmp_pair_init_container(self, white_resource_id, black_resource_id, c):
        raise NotImplementedError("rotbmp_pair_init_container")

    def rotbmp_pair_layer_set_src_ic(self, pair, ic):
        raise NotImplementedError("rotbmp_pair_layer_set_src_ic")

    def rotbmp_pair_layer_set_angle(self, pair, angle):
        raise NotImplementedError("rotbmp_pair_layer_set_angle")

    def window_init(self, window, debug_name):
        raise NotImplementedError("window_init")

    def window_stack_push(self, window, animated):
        raise NotImplementedError("window_stack_push")

    def window_set_click_config_provider(self, window, click_config_provider):
        raise NotImplementedError("window_set_click_config_provider")

    def window_set_background_color(self, window, background_color):
        raise NotImplementedError("window_set_background_color")

    def window_render(self, window, ctx):
        raise NotImplementedError("window_render")

    def window_set_fullscreen(self, window, enabled):
        raise NotImplementedError("window_set_fullscreen")

    def sin_lookup(self, angle):
        raise NotImplementedError("sin_lookup")

    def string_format_time(self, ptr, maxsize, format, timeptr):
        raise NotImplementedError("string_format_time")

    def text_layer_init(self, text_layer, frame):
        raise NotImplementedError("text_layer_init")

    def text_layer_get_text(self, text_layer):
        raise NotImplementedError("text_layer_get_text")

    def text_layer_set_text(self, text_layer, text):
        raise NotImplementedError("text_layer_set_text")

    def text_layer_set_font(self, text_layer, font):
        raise NotImplementedError("text_layer_set_font")

    def text_layer_set_text_color(self, text_layer, color):
        raise NotImplementedError("text_layer_set_text_color")

    def text_layer_set_background_color(self, text_layer, color):
        raise NotImplementedError("text_layer_set_background_color")

    def vibes_double_pulse(self):
        raise NotImplementedError("vibes_double_pulse")

    def vibes_enqueue_custom_pattern(self, pattern):
        raise NotImplementedError("vibes_enqueue_custom_pattern")

    def vibes_long_pulse(self):
        raise NotImplementedError("vibes_long_pulse")

    def vibes_short_pulse(self):
        raise NotImplementedError("vibes_short_pulse")

    def app_get_current_graphics_context(self):
        raise NotImplementedError("app_get_current_graphics_context")

    def clock_is_24h_style(self):
        raise NotImplementedError("clock_is_24h_style")

    def property_animation_init_layer_frame(self, property_animation, layer, from_frame, to_frame):
        raise NotImplementedError("property_animation_init_layer_frame")

    def text_layer_set_text_alignment(self, text_layer, text_alignment):
        raise NotImplementedError("text_layer_set_text_alignment")

    def graphics_draw_bitmap_in_rect(self, ctx, bitmap, rect):
        raise NotImplementedError("graphics_draw_bitmap_in_rect")

    def graphics_text_draw(self, ctx, text, font, box, overflow_mode, alignment, layout):
        raise NotImplementedError("graphics_text_draw")

    def layer_set_bounds(self, layer, bounds):
        raise NotImplementedError("layer_set_bounds")

    def layer_get_bounds(self, layer):
        raise NotImplementedError("layer_get_bounds")

    def layer_set_update_proc(self, layer, update_proc):
        raise NotImplementedError("layer_set_update_proc")

    def layer_get_window(self, layer):
        raise NotImplementedError("layer_get_window")

    def layer_remove_child_layers(self, parent):
        raise NotImplementedError("layer_remove_child_layers")

    def layer_insert_below_sibling(self, layer_to_insert, below_sibling_layer):
        raise NotImplementedError("layer_insert_below_sibling")

    def layer_insert_above_sibling(self, layer_to_insert, above_sibling_layer):
        raise NotImplementedError("layer_insert_above_sibling")

    def layer_get_hidden(self, layer):
        raise NotImplementedError("layer_get_hidden")

    def layer_set_clips(self, layer, clips):
        raise NotImplementedError("layer_set_clips")

    def layer_get_clips(self, layer):
        raise NotImplementedError("layer_get_clips")

    def text_layer_get_max_used_size(self, ctx, text_layer):
        raise NotImplementedError("text_layer_get_max_used_size")

    def text_layer_set_size(self, text_layer, max_size):
        raise NotImplementedError("text_layer_set_size")

    def text_layer_set_overflow_mode(self, text_layer, line_mode):
        raise NotImplementedError("text_layer_set_overflow_mode")

    def graphics_text_layout_get_max_used_size(self, ctx, text, font, box, overflow_mode, alignment, layout):
        raise NotImplementedError("graphics_text_layout_get_max_used_size")

    def inverter_layer_init(self, inverter, frame):
        raise NotImplementedError("inverter_layer_init")

    def bitmap_layer_init(self, image, frame):
        raise NotImplementedError("bitmap_layer_init")

    def bitmap_layer_set_bitmap(self, image, bitmap):
        raise NotImplementedError("bitmap_layer_set_bitmap")

    def bitmap_layer_set_alignment(self, image, alignment):
        raise NotImplementedError("bitmap_layer_set_alignment")

    def bitmap_layer_set_background_color(self, image, color):
        raise NotImplementedError("bitmap_layer_set_background_color")

    def bitmap_layer_set_compositing_mode(self, image, mode):
        raise NotImplementedError("bitmap_layer_set_compositing_mode")

    def heap_bitmap_init(self, hb, resource_id):
        raise NotImplementedError("heap_bitmap_init")

    def heap_bitmap_deinit(self, hb):
        raise NotImplementedError("heap_bitmap_deinit")

    def click_recognizer_get_button_id(self, recognizer):
        raise NotImplementedError("click_recognizer_get_button_id")

    def click_number_of_clicks_counted(self, recognizer):
        raise NotImplementedError("click_number_of_clicks_counted")

    def menu_cell_basic_draw(self, ctx, cell_layer, title, subtitle, icon):
        raise NotImplementedError("menu_cell_basic_draw")

    def menu_cell_title_draw(self, ctx, cell_layer, title):
        raise NotImplementedError("menu_cell_title_draw")

    def menu_cell_basic_header_draw(self, ctx, cell_layer, title):
        raise NotImplementedError("menu_cell_basic_header_draw")

    def menu_layer_init(self, menu_layer, frame):
        raise NotImplementedError("menu_layer_init")

    def menu_layer_get_layer(self, menu_layer):
        raise NotImplementedError("menu_layer_get_layer")

    def menu_layer_set_callbacks(self, menu_layer, callback_context, callbacks):
        raise NotImplementedError("menu_layer_set_callbacks")

    def menu_layer_set_click_config_onto_window(self, menu_layer, window):
        raise NotImplementedError("menu_layer_set_click_config_onto_window")

    def menu_layer_set_selected_next(self, menu_layer, up, scroll_align, animated):
        raise NotImplementedError("menu_layer_set_selected_next")

    def menu_layer_set_selected_index(self, menu_layer, index, scroll_align, animated):
        raise NotImplementedError("menu_layer_set_selected_index")

    def menu_layer_reload_data(self, menu_layer):
        raise NotImplementedError("menu_layer_reload_data")

    def menu_index_compare(self, a, b):
        raise NotImplementedError("menu_index_compare")

    def scroll_layer_init(self, scroll_layer, frame):
        raise NotImplementedError("scroll_layer_init")

    def scroll_layer_add_child(self, scroll_layer, child):
        raise NotImplementedError("scroll_layer_add_child")

    def scroll_layer_set_click_config_onto_window(self, scroll_layer, window):
        raise NotImplementedError("scroll_layer_set_click_config_onto_window")

    def scroll_layer_set_callbacks(self, scroll_layer, callbacks):
        raise NotImplementedError("scroll_layer_set_callbacks")

    def scroll_layer_set_context(self, scroll_layer, context):
        raise NotImplementedError("scroll_layer_set_context")

    def scroll_layer_set_content_offset(self, scroll_layer, offset, animated):
        raise NotImplementedError("scroll_layer_set_content_offset")

    def scroll_layer_get_content_offset(self, scroll_layer):
        raise NotImplementedError("scroll_layer_get_content_offset")

    def scroll_layer_set_content_size(self, scroll_layer, size):
        raise NotImplementedError("scroll_layer_set_content_size")

    def scroll_layer_get_content_size(self, scroll_layer):
        raise NotImplementedError("scroll_layer_get_content_size")

    def scroll_layer_set_frame(self, scroll_layer, rect):
        raise NotImplementedError("scroll_layer_set_frame")

    def scroll_layer_scroll_up_click_handler(self, recognizer, scroll_layer):
        raise NotImplementedError("scroll_layer_scroll_up_click_handler")

    def scroll_layer_scroll_down_click_handler(self, recognizer, scroll_layer):
        raise NotImplementedError("scroll_layer_scroll_down_click_handler")

    def simple_menu_layer_init(self, simple_menu, frame, window, sections, num_sections, callback_context):
        raise NotImplementedError("simple_menu_layer_init")

    def simple_menu_layer_get_layer(self, simple_menu):
        raise NotImplementedError("simple_menu_layer_get_layer")

    def simple_menu_layer_get_selected_index(self, simple_menu):
        raise NotImplementedError("simple_menu_layer_get_selected_index")

    def simple_menu_layer_set_selected_index(self, simple_menu, index, animated):
        raise NotImplementedError("simple_menu_layer_set_selected_index")

    def window_deinit(self, window):
        raise NotImplementedError("window_deinit")

    def window_set_click_config_provider_with_context(self, window, click_config_provider, context):
        raise NotImplementedError("window_set_click_config_provider_with_context")

    def window_get_click_config_provider(self, window):
        raise NotImplementedError("window_get_click_config_provider")

    def window_set_window_handlers(self, window, handlers):
        raise NotImplementedError("window_set_window_handlers")

    def window_get_root_layer(self, window):
        raise NotImplementedError("window_get_root_layer")

    def window_get_fullscreen(self, window):
        raise NotImplementedError("window_get_fullscreen")

    def window_set_status_bar_icon(self, window, icon):
        raise NotImplementedError("window_set_status_bar_icon")

    def window_is_loaded(self, window):
        raise NotImplementedError("window_is_loaded")

    def window_stack_pop(self, animated):
        raise NotImplementedError("window_stack_pop")

    def window_stack_pop_all(self, animated):
        raise NotImplementedError("window_stack_pop_all")

    def window_stack_contains_window(self, window):
        raise NotImplementedError("window_stack_contains_window")

    def window_stack_get_top_window(self):
        raise NotImplementedError("window_stack_get_top_window")

    def window_stack_remove(self, window, animated):
        raise NotImplementedError("window_stack_remove")

    def property_animation_init(self, property_animation, implementation, subject, from_value, to_value):
        raise NotImplementedError("property_animation_init")

    def property_animation_update_int16(self, property_animation, time_normalized):
        raise NotImplementedError("property_animation_update_int16")

    def property_animation_update_gpoint(self, property_animation, time_normalized):
        raise NotImplementedError("property_animation_update_gpoint")

    def property_animation_update_grect(self, property_animation, time_normalized):
        raise NotImplementedError("property_animation_update_grect")

    def app_message_register_callbacks(self, callbacks_node):
        raise NotImplementedError("app_message_register_callbacks")

    def app_message_deregister_callbacks(self, callbacks_node):
        raise NotImplementedError("app_message_deregister_callbacks")

    def app_message_out_get(self, iter_out):
        raise NotImplementedError("app_message_out_get")

    def app_message_out_send(self):
        raise NotImplementedError("app_message_out_send")

    def app_message_out_release(self):
        raise NotImplementedError("app_message_out_release")

    def app_sync_init(self, s, buffer, buffer_size, keys_and_initial_values, count, tuple_changed_callback, error_callback, context):
        raise NotImplementedError("app_sync_init")

    def app_sync_deinit(self, s):
        raise NotImplementedError("app_sync_deinit")

    def app_sync_set(self, s, keys_and_values_to_update, count):
        raise NotImplementedError("app_sync_set")

    def app_sync_get(self, s, key):
        raise NotImplementedError("app_sync_get")

    def dict_write_begin(self, iter, buffer, size):
        raise NotImplementedError("dict_write_begin")

    def dict_write_data(self, iter, key, data, size):
        raise NotImplementedError("dict_write_data")

    def dict_write_cstring(self, iter, key, cstring):
        raise NotImplementedError("dict_write_cstring")

    def dict_write_int(self, iter, key, integer, width_bytes, is_signed):
        raise NotImplementedError("dict_write_int")

    def dict_write_uint8(self, iter, key, value):
        raise NotImplementedError("dict_write_uint8")

    def dict_write_uint16(self, iter, key, value):
        raise NotImplementedError("dict_write_uint16")

    def dict_write_uint32(self, iter, key, value):
        raise NotImplementedError("dict_write_uint32")

    def dict_write_int8(self, iter, key, value):
        raise NotImplementedError("dict_write_int8")

    def dict_write_int16(self, iter, key, value):
        raise NotImplementedError("dict_write_int16")

    def dict_write_int32(self, iter, key, value):
        raise NotImplementedError("dict_write_int32")

    def dict_write_end(self, iter):
        raise NotImplementedError("dict_write_end")

    def dict_read_begin_from_buffer(self, iter, buffer, size):
        raise NotImplementedError("dict_read_begin_from_buffer")

    def dict_read_next(self, iter):
        raise NotImplementedError("dict_read_next")

    def dict_read_first(self, iter):
        raise NotImplementedError("dict_read_first")

    def dict_serialize_tuplets(self, callback, context, tuplets_count, tuplets):
        raise NotImplementedError("dict_serialize_tuplets")

    def dict_serialize_tuplets_to_buffer(self, tuplets_count, tuplets, buffer, size_in_out):
        raise NotImplementedError("dict_serialize_tuplets_to_buffer")

    def dict_serialize_tuplets_to_buffer_with_iter(self, tuplets_count, tuplets, iter, buffer, size_in_out):
        raise NotImplementedError("dict_serialize_tuplets_to_buffer_with_iter")

    def dict_write_tuplet(self, iter, tuplet):
        raise NotImplementedError("dict_write_tuplet")

    def dict_calc_buffer_size_from_tuplets(self, tuplets_count, tuplets):
        raise NotImplementedError("dict_calc_buffer_size_from_tuplets")

    def dict_merge(self, dest, dest_max_size_in_out, source, update_existing_keys_only, key_callback, context):
        raise NotImplementedError("dict_merge")

    def dict_find(self, iter, key):
        raise NotImplementedError("dict_find")

    def action_bar_layer_init(self, action_bar):
        raise NotImplementedError("action_bar_layer_init")

    def action_bar_layer_set_context(self, action_bar, context):
        raise NotImplementedError("action_bar_layer_set_context")

    def action_bar_layer_set_click_config_provider(self, action_bar, click_config_provider):
        raise NotImplementedError("action_bar_layer_set_click_config_provider")

    def action_bar_layer_set_icon(self, action_bar, button_id, icon):
        raise NotImplementedError("action_bar_layer_set_icon")

    def action_bar_layer_clear_icon(self, action_bar, button_id):
        raise NotImplementedError("action_bar_layer_clear_icon")

    def action_bar_layer_add_to_window(self, action_bar, window):
        raise NotImplementedError("action_bar_layer_add_to_window")

    def action_bar_layer_remove_from_window(self, action_bar):
        raise NotImplementedError("action_bar_layer_remove_from_window")

    def action_bar_layer_set_background_color(self, action_bar, background_color):
        raise NotImplementedError("action_bar_layer_set_background_color")

    def number_window_init(self, numberwindow, label, callbacks, callback_context):
        raise NotImplementedError("number_window_init")

    def number_window_set_label(self, nw, label):
        raise NotImplementedError("number_window_set_label")

    def number_window_set_max(self, numberwindow, max):
        raise NotImplementedError("number_window_set_max")

    def number_window_set_min(self, numberwindow, min):
        raise NotImplementedError("number_window_set_min")

    def number_window_set_value(self, numberwindow, value):
        raise NotImplementedError("number_window_set_value")

    def number_window_set_step_size(self, numberwindow, step):
        raise NotImplementedError("number_window_set_step_size")

    def number_window_get_value(self, numberwindow):
        raise NotImplementedError("number_window_get_value")

    def clock_copy_time_string(self, buffer, size):
        raise NotImplementedError("clock_copy_time_string")
