This is a bunch of notes concerning the operation of the Pebble.

Rendering
=========

Colors
------

The only colors available for drawing are `GColorWhite` and `GColorBlack`.
`GColorClear` appears to be a flag that disables drawing backgrounds and such.
Various structs reserve 2 bits for `GColor` fields, so there's a fourth
possible (but invalid?) color.

Any color that isn't `GColorBlack` is apparently drawn as white.

Defaults:
 * `fill_color` seems to be `GColorBlack`.
 * `stroke_color` seems to be `GColorWhite`.
 * `text_color` seems to be `GColorWhite`.

Colors are apparently inherited by child layers, but not sibling layers.

Compositing
-----------

It looks like compositing mode is only relevant for bitmap rendering operations.

 * `GCompOpAssign` is the default and it just draws opaque black and white
   pixels for the bitmap.
 * `GCompOpAssignInverted` is like `GCompOpAssign`, but it swaps black and
   white around.
 * `GCompOpClear` draws only the black portions of an image.
 * `GCompOpOr` draws only the white portions of an image.
 * `GCompOpAnd` seems to be broken.

