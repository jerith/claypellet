/****************************************************************************
 * This is a bunch of type definitions from pebble_os.h modified to be usable
 * by `FFI.cdef()'.
 ****************************************************************************/


struct Layer;
struct AccelData;
struct Animation;
struct ScrollLayer;
struct MenuLayer;
struct NumberWindow;
struct GContext;
typedef struct GContext GContext;


typedef struct AccelData
{
  int16_t x;
  int16_t y;
  int16_t z;
} AccelData;
typedef struct ListNode
{
  struct ListNode *next;
  struct ListNode *prev;
} ListNode;
typedef enum {AnimationCurveLinear = 0, AnimationCurveEaseIn = 1, AnimationCurveEaseOut = 2, AnimationCurveEaseInOut = 3, NumAnimationCurve = 4} AnimationCurve;
typedef void (*AnimationSetupImplementation)(struct Animation *animation);
typedef void (*AnimationUpdateImplementation)(struct Animation *animation, const uint32_t time_normalized);
typedef void (*AnimationTeardownImplementation)(struct Animation *animation);
typedef struct AnimationImplementation
{
  AnimationSetupImplementation setup;
  AnimationUpdateImplementation update;
  AnimationTeardownImplementation teardown;
} AnimationImplementation;
typedef void (*AnimationStartedHandler)(struct Animation *animation, void *context);
typedef void (*AnimationStoppedHandler)(struct Animation *animation, bool finished, void *context);
typedef struct AnimationHandlers
{
  AnimationStartedHandler started;
  AnimationStoppedHandler stopped;
} AnimationHandlers;
typedef struct Animation
{
  ListNode list_node;
  const struct AnimationImplementation *implementation;
  AnimationHandlers handlers;
  void *context;
  uint32_t abs_start_time_ms;
  uint32_t delay_ms;
  uint32_t duration_ms;
  /* AnimationCurve curve : 3; */
  /* bool is_completed : 1; */
    ...;
} Animation;
typedef void *AppTaskContextRef;
typedef uint32_t AppTimerHandle;
typedef enum {BUTTON_ID_BACK = 0, BUTTON_ID_UP, BUTTON_ID_SELECT, BUTTON_ID_DOWN, NUM_BUTTONS} ButtonId;
typedef enum GColor {GColorClear = -1, GColorBlack = 0, GColorWhite = 1} GColor;
typedef struct GPoint
{
  int16_t x;
  int16_t y;
} GPoint;
typedef struct GPath
{
  int num_points;
  GPoint *points;
  int32_t rotation;
  GPoint offset;
} GPath;
typedef struct GPathInfo
{
  int num_points;
  GPoint *points;
} GPathInfo;
typedef struct GSize
{
  int16_t w;
  int16_t h;
} GSize;
typedef struct GRect
{
  GPoint origin;
  GSize size;
} GRect;
typedef struct GBitmap
{
  void *addr;
  uint16_t row_size_bytes;
  uint16_t info_flags;
  GRect bounds;
} GBitmap;
typedef enum {GCompOpAssign, GCompOpAssignInverted, GCompOpOr, GCompOpAnd, GCompOpClear} GCompOp;
typedef struct GDrawState
{
  GRect clip_box;
  GRect drawing_box;
  GColor stroke_color : 2;
  GColor fill_color : 2;
  GColor text_color : 2;
  GCompOp compositing_mode : 3;
} GDrawState;

// Modified for cdef
typedef enum {
    GCornerNone = 0,
    GCornerTopLeft = 1,
    GCornerTopRight = 2,
    GCornerBottomLeft = 4,
    GCornerBottomRight = 8,
    GCornersAll = 15,
    GCornersTop = 3,
    GCornersBottom = 12,
    GCornersLeft = 5,
    GCornersRight = 10
} GCornerMask;

typedef void *AppContextRef;
typedef struct 
{
  int tm_sec;
  int tm_min;
  int tm_hour;
  int tm_mday;
  int tm_mon;
  int tm_year;
  int tm_wday;
  int tm_yday;
  int tm_isdst;
} PblTm;

// Modified for cdef
typedef enum {
    SECOND_UNIT = 1,
    MINUTE_UNIT = 2,
    HOUR_UNIT = 4,
    DAY_UNIT = 8,
    MONTH_UNIT = 16,
    YEAR_UNIT = 32
} TimeUnits;

typedef void *ClickRecognizerRef;
typedef void (*ClickHandler)(ClickRecognizerRef recognizer, void *context);
typedef enum {TUPLE_BYTE_ARRAY = 0, TUPLE_CSTRING = 1, TUPLE_UINT = 2, TUPLE_INT = 3} TupleType;
typedef struct 
{
  /* uint32_t key; */
  /* TupleType type : 8; */
  /* uint16_t length; */
  /* union  */
  /* { */
  /*   uint8_t data[0]; */
  /*   char cstring[0]; */
  /*   uint8_t uint8; */
  /*   uint16_t uint16; */
  /*   uint32_t uint32; */
  /*   int8_t int8; */
  /*   int16_t int16; */
  /*   int32_t int32; */
  /* } value[]; */
    ...;
} Tuple;
typedef struct Tuplet
{
  TupleType type;
  uint32_t key;
  union 
  {
    struct 
    {
      const uint8_t *data;
      const uint16_t length;
    } bytes;
    struct 
    {
      const char *data;
      const uint16_t length;
    } cstring;
    struct 
    {
      uint32_t storage;
      const uint16_t width;
    } integer;
  };
} Tuplet;
typedef struct 
{
  /* uint8_t count; */
  /* Tuple head[]; */
    ...;
} Dictionary;
typedef struct 
{
  Dictionary *dictionary;
  const void *end;
  Tuple *cursor;
} DictionaryIterator;

// Modified for cdef
typedef enum {
    APP_MSG_OK = 0,
    APP_MSG_SEND_TIMEOUT = 2,
    APP_MSG_SEND_REJECTED = 4,
    APP_MSG_NOT_CONNECTED = 8,
    APP_MSG_APP_NOT_RUNNING = 16,
    APP_MSG_INVALID_ARGS = 32,
    APP_MSG_BUSY = 64,
    APP_MSG_BUFFER_OVERFLOW = 128,
    APP_MSG_ALREADY_RELEASED = 512,
    APP_MSG_CALLBACK_ALREADY_REGISTERED = 1024,
    APP_MSG_CALLBACK_NOT_REGISTERED = 2048
} AppMessageResult;

typedef struct 
{
  ListNode node;
  void *context;
  struct 
  {
    void (*out_sent)(DictionaryIterator *sent, void *context);
    void (*out_failed)(DictionaryIterator *failed, AppMessageResult reason, void *context);
    void (*in_received)(DictionaryIterator *received, void *context);
    void (*in_dropped)(void *context, AppMessageResult reason);
  } callbacks;
} AppMessageCallbacksNode;
typedef struct 
{
  struct 
  {
    uint16_t inbound;
    uint16_t outbound;
  } buffer_sizes;
  AppMessageCallbacksNode default_callbacks;
} PebbleAppMessagingInfo;
typedef struct 
{
  void (*callback)(void *data);
  void *data;
} PebbleCallbackEvent;
typedef struct 
{
  PblTm *tick_time;
  TimeUnits units_changed;
} PebbleTickEvent;
typedef struct 
{
  struct Window *window;
  struct GContext *ctx;
} PebbleRenderEvent;
typedef struct 
{
  ButtonId button_id;
} PebbleButtonEvent;
typedef void (*PebbleAppInitEventHandler)(AppContextRef app_ctx);
typedef void (*PebbleAppButtonEventHandler)(AppContextRef app_ctx, PebbleButtonEvent *event);
typedef void (*PebbleAppRenderEventHandler)(AppContextRef app_ctx, PebbleRenderEvent *event);
typedef void (*PebbleAppDeinitEventHandler)(AppContextRef app_ctx);
typedef void (*PebbleAppTimerHandler)(AppContextRef app_ctx, AppTimerHandle handle, uint32_t cookie);
typedef void (*PebbleAppTickHandler)(AppContextRef app_ctx, PebbleTickEvent *event);
typedef struct 
{
  PebbleAppTickHandler tick_handler;
  TimeUnits tick_units;
} PebbleAppTickInfo;
typedef struct PebbleAppInputHandlers
{
  struct 
  {
    PebbleAppButtonEventHandler up;
    PebbleAppButtonEventHandler down;
  } buttons;
} PebbleAppInputHandlers;
typedef struct 
{
  PebbleAppInitEventHandler init_handler;
  PebbleAppDeinitEventHandler deinit_handler;
  PebbleAppRenderEventHandler render_handler;
  PebbleAppInputHandlers input_handlers;
  PebbleAppTickInfo tick_info;
  PebbleAppTimerHandler timer_handler;
  PebbleAppMessagingInfo messaging_info;
} PebbleAppHandlers;
typedef void (*LayerUpdateProc)(struct Layer *layer, GContext *ctx);
typedef struct Layer
{
  GRect bounds;
  GRect frame;
  bool clips : 1;
  bool hidden : 1;
  struct Layer *next_sibling;
  struct Layer *parent;
  struct Layer *first_child;
  struct Window *window;
  LayerUpdateProc update_proc;
} Layer;
typedef void *GFont;
typedef enum {GTextOverflowModeWordWrap, GTextOverflowModeTrailingEllipsis} GTextOverflowMode;
typedef enum {GTextAlignmentLeft, GTextAlignmentCenter, GTextAlignmentRight} GTextAlignment;
typedef enum GAlign {GAlignCenter, GAlignTopLeft, GAlignTopRight, GAlignTop, GAlignLeft, GAlignBottom, GAlignRight, GAlignBottomRight, GAlignBottomLeft} GAlign;
typedef void *GTextLayoutCacheRef;
typedef struct TextLayer
{
  Layer layer;
  const char *text;
  GFont font;
  GTextLayoutCacheRef layout_cache;
  /* GColor text_color : 2; */
  /* GColor background_color : 2; */
  /* GTextOverflowMode overflow_mode : 2; */
  /* GTextAlignment text_alignment : 2; */
  /* bool should_cache_layout : 1; */
    ...;
} TextLayer;
typedef void (*WindowButtonEventHandler)(AppContextRef app_ctx, struct Window *window, PebbleButtonEvent *event);
typedef struct WindowInputHandlers
{
  struct 
  {
    WindowButtonEventHandler up;
    WindowButtonEventHandler down;
  } buttons;
} WindowInputHandlers;
typedef void (*WindowHandler)(struct Window *window);
typedef struct WindowHandlers
{
  WindowHandler load;
  WindowHandler appear;
  WindowHandler disappear;
  WindowHandler unload;
} WindowHandlers;
typedef struct ClickConfig
{
  void *context;
  struct 
  {
    ClickHandler handler;
    uint16_t repeat_interval_ms;
  } click;
  struct 
  {
    uint8_t min;
    uint8_t max;
    bool last_click_only;
    ClickHandler handler;
    uint16_t timeout;
  } multi_click;
  struct 
  {
    uint16_t delay_ms;
    ClickHandler handler;
    ClickHandler release_handler;
  } long_click;
  struct 
  {
    ClickHandler up_handler;
    ClickHandler down_handler;
    void *context;
  } raw;
} ClickConfig;
typedef void (*ClickConfigProvider)(ClickConfig **array_of_ptrs_to_click_configs_to_setup, void *context);
typedef struct Window
{
  Layer layer;
  const GBitmap *status_bar_icon;
  WindowInputHandlers input_handlers;
  WindowHandlers window_handlers;
  ClickConfigProvider click_config_provider;
  void *click_config_context;
  void *user_data;
  /* GColor background_color : 2; */
  /* bool is_render_scheduled : 1; */
  /* bool on_screen : 1; */
  /* bool is_loaded : 1; */
  /* bool overrides_back_button : 1; */
  /* bool is_fullscreen : 1; */
  const char *debug_name;
    ...;
} Window;
typedef struct BitmapLayer
{
  Layer layer;
  const GBitmap *bitmap;
  GColor background_color : 2;
  GAlign alignment : 4;
  GCompOp compositing_mode : 3;
} BitmapLayer;
typedef struct 
{
  Layer layer;
  GBitmap *bitmap;
  GColor corner_clip_color;
  int32_t rotation;
  GPoint src_ic;
  GPoint dest_ic;
  GCompOp compositing_mode;
} RotBitmapLayer;
typedef struct 
{
  Layer layer;
  RotBitmapLayer white_layer;
  RotBitmapLayer black_layer;
} RotBmpPairLayer;
typedef struct 
{
  uint8_t *data;
  GBitmap bmp;
  BitmapLayer layer;
} BmpContainer;
typedef struct 
{
  uint8_t *data;
  GBitmap bmp;
  RotBitmapLayer layer;
} RotBmpContainer;
typedef struct 
{
  uint8_t *white_data;
  uint8_t *black_data;
  GBitmap white_bmp;
  GBitmap black_bmp;
  RotBmpPairLayer layer;
} RotBmpPairContainer;
typedef struct 
{
  uint32_t crc;
  uint32_t timestamp;
  char friendly_version[16];
} ResBankVersion;
typedef const ResBankVersion *ResVersionHandle;
typedef const void *ResHandle;
typedef struct 
{
  const uint32_t *durations;
  int num_segments;
} VibePattern;
typedef struct PropertyAnimation
{
  Animation animation;
  struct 
  {
    union 
    {
      GRect grect;
      GPoint gpoint;
      int16_t int16;
    } to;
    union 
    {
      GRect grect;
      GPoint gpoint;
      int16_t int16;
    } from;
  } values;
  void *subject;
} PropertyAnimation;
typedef struct InverterLayer
{
  Layer layer;
} InverterLayer;
typedef struct 
{
  uint8_t *data;
  GBitmap bmp;
} HeapBitmap;
typedef void (*ScrollLayerCallback)(struct ScrollLayer *scroll_layer, void *context);
typedef struct ScrollLayerCallbacks
{
  ClickConfigProvider click_config_provider;
  ScrollLayerCallback content_offset_changed_handler;
} ScrollLayerCallbacks;
typedef struct ScrollLayer
{
  Layer layer;
  Layer content_sublayer;
  Layer shadow_sublayer;
  PropertyAnimation animation;
  ScrollLayerCallbacks callbacks;
  void *context;
} ScrollLayer;
typedef struct MenuIndex
{
  uint16_t section;
  uint16_t row;
} MenuIndex;
typedef void (*MenuLayerSelectionChangedCallback)(struct MenuLayer *menu_layer, MenuIndex new_index, MenuIndex old_index, void *callback_context);
typedef void (*MenuLayerSelectCallback)(struct MenuLayer *menu_layer, MenuIndex *cell_index, void *callback_context);
typedef void (*MenuLayerDrawRowCallback)(GContext *ctx, Layer *cell_layer, MenuIndex *cell_index, void *callback_context);
typedef void (*MenuLayerDrawHeaderCallback)(GContext *ctx, Layer *cell_layer, uint16_t section_index, void *callback_context);
typedef int16_t (*MenuLayerGetHeaderHeightCallback)(struct MenuLayer *menu_layer, uint16_t section_index, void *callback_context);
typedef int16_t (*MenuLayerGetCellHeightCallback)(struct MenuLayer *menu_layer, MenuIndex *cell_index, void *callback_context);
typedef uint16_t (*MenuLayerGetNumberOfRowsInSectionsCallback)(struct MenuLayer *menu_layer, uint16_t section_index, void *callback_context);
typedef uint16_t (*MenuLayerGetNumberOfSectionsCallback)(struct MenuLayer *menu_layer, void *callback_context);
typedef struct MenuLayerCallbacks
{
  MenuLayerGetNumberOfSectionsCallback get_num_sections;
  MenuLayerGetNumberOfRowsInSectionsCallback get_num_rows;
  MenuLayerGetCellHeightCallback get_cell_height;
  MenuLayerGetHeaderHeightCallback get_header_height;
  MenuLayerDrawRowCallback draw_row;
  MenuLayerDrawHeaderCallback draw_header;
  MenuLayerSelectCallback select_click;
  MenuLayerSelectCallback select_long_click;
  MenuLayerSelectionChangedCallback selection_changed;
} MenuLayerCallbacks;
typedef struct MenuCellSpan
{
  int16_t y;
  int16_t h;
  MenuIndex index;
} MenuCellSpan;
typedef enum {MenuRowAlignNone, MenuRowAlignCenter, MenuRowAlignTop, MenuRowAlignBottom} MenuRowAlign;
typedef struct MenuLayer
{
  ScrollLayer scroll_layer;
  InverterLayer inverter;
  struct 
  {
    MenuCellSpan cursor;
  } cache;
  MenuCellSpan selection;
  MenuLayerCallbacks callbacks;
  void *callback_context;
} MenuLayer;
typedef void (*SimpleMenuLayerSelectCallback)(int index, void *context);
typedef struct 
{
  const char *title;
  const char *subtitle;
  GBitmap *icon;
  SimpleMenuLayerSelectCallback callback;
} SimpleMenuItem;
typedef struct 
{
  const char *title;
  const SimpleMenuItem *items;
  uint32_t num_items;
} SimpleMenuSection;
typedef struct 
{
  MenuLayer menu;
  const SimpleMenuSection *sections;
  int num_sections;
  void *callback_context;
} SimpleMenuLayer;
typedef int32_t (*AnimationTimingFunction)(uint32_t time_normalized);
typedef struct ActionBarLayer
{
  Layer layer;
  const struct GBitmap *icons[3];
  struct Window *window;
  void *context;
  ClickConfigProvider click_config_provider;
  unsigned is_highlighted : 3;
  GColor background_color : 2;
} ActionBarLayer;
typedef void (*NumberWindowCallback)(struct NumberWindow *number_window, void *context);
typedef struct 
{
  NumberWindowCallback incremented;
  NumberWindowCallback decremented;
  NumberWindowCallback selected;
} NumberWindowCallbacks;
typedef struct NumberWindow
{
  Window window;
  ActionBarLayer action_bar;
  TextLayer value_label;
  TextLayer value_output;
  char value_output_buffer[12];
  int value;
  int max_val;
  int min_val;
  int step_size;
  bool is_wrapping_enabled;
  NumberWindowCallbacks callbacks;
  void *callback_context;
} NumberWindow;
typedef GPoint GPointReturn;
typedef GRect GRectReturn;
typedef void (*Int16Setter)(void *subject, int16_t int16);
typedef void (*GPointSetter)(void *subject, GPoint gpoint);
typedef void (*GRectSetter)(void *subject, GRect grect);
typedef int16_t (*Int16Getter)(void *subject);
typedef GPointReturn (*GPointGetter)(void *subject);
typedef GRectReturn (*GRectGetter)(void *subject);
typedef struct PropertyAnimationAccessors
{
  union 
  {
    Int16Setter int16;
    GPointSetter gpoint;
    GRectSetter grect;
  } setter;
  union 
  {
    Int16Getter int16;
    GPointGetter gpoint;
    GRectGetter grect;
  } getter;
} PropertyAnimationAccessors;
typedef struct PropertyAnimationImplementation
{
  AnimationImplementation base;
  PropertyAnimationAccessors accessors;
} PropertyAnimationImplementation;

// Modified for cdef
typedef enum {
    DICT_OK = 0,
    DICT_NOT_ENOUGH_STORAGE = 2,
    DICT_INVALID_ARGS = 4,
    DICT_INTERNAL_INCONSISTENCY = 8
} DictionaryResult;

typedef void (*AppSyncTupleChangedCallback)(const uint32_t key, const Tuple *new_tuple, const Tuple *old_tuple, void *context);
typedef void (*AppSyncErrorCallback)(DictionaryResult dict_error, AppMessageResult app_message_error, void *context);
typedef struct AppSync
{
  DictionaryIterator current_iter;
  union 
  {
    Dictionary *current;
    uint8_t *buffer;
  };
  uint16_t buffer_size;
  struct 
  {
    AppSyncTupleChangedCallback value_changed;
    AppSyncErrorCallback error;
    void *context;
  } callback;
  AppMessageCallbacksNode app_message_cb_node;
} AppSync;
typedef void (*DictionarySerializeCallback)(const uint8_t * const data, const uint16_t size, void *context);
typedef void (*DictionaryKeyUpdatedCallback)(const uint32_t key, const Tuple *new_tuple, const Tuple *old_tuple, void *context);
