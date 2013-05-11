import operator

from PIL import Image, ImageDraw


def pmap(op, p0, p1):
    return (op(p0[0], p1[0]), op(p0[1], p1[1]))


class PebbleGraphicsContext(object):
    COLOR_BLACK = (0, 255)
    COLOR_WHITE = (255, 255)
    COLOR_CLEAR = (192, 0)

    ALIGN_LEFT = 'left'
    ALIGN_CENTER = 'center'
    ALIGN_RIGHT = 'right'

    stroke_color = COLOR_BLACK
    fill_color = COLOR_BLACK
    text_color = COLOR_BLACK

    def __init__(self, display, size):
        self._display = display
        self.image = Image.new('LA', size, (0, 0))
        self._flattened = False
        self._children = []

    def get_image(self):
        if not self._flattened:
            for frame, child in self._children:
                self.paste_image(child.get_image(),
                                 (frame.origin.x, frame.origin.y))
            self._flattened = True
        return self.image

    def get_child_context(self, frame):
        child = PebbleGraphicsContext(self._display,
                                      (frame.size.w, frame.size.h))
        self._children.append((frame, child))
        return child

    def tempimage(self, size):
        return Image.new('LA', size, (0, 0))

    def paste_image(self, src, topleft, dst=None):
        if dst is None:
            dst = self.image
        dst.paste(src, topleft, src.split()[-1])

    def bgfill(self, color):
        self.image.paste(color, (0, 0, self.image.size[0], self.image.size[1]))

    def draw_line(self, gpoint0, gpoint1):
        draw = ImageDraw.Draw(self.image)
        p0 = (gpoint0.x, gpoint0.y)
        p1 = (gpoint1.x, gpoint1.y)
        draw.line((p0, p1), fill=self.stroke_color)

    def _draw_circle(self, draw, center, radius, color, fill=False):
        # PIL's circle algorithm is wrong, so I'm using a slightly modified
        # version of https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
        x0, y0 = center
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius
        x = 0
        y = radius

        if fill:
            draw.line(((x0 - radius, y0), (x0 + radius, y0)), fill=color)
            draw.line(((x0, y0 - radius), (x0, y0 + radius)), fill=color)
        else:
            draw.point((x0, y0 + radius), fill=color)
            draw.point((x0, y0 - radius), fill=color)
            draw.point((x0 + radius, y0), fill=color)
            draw.point((x0 - radius, y0), fill=color)

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x
            if fill:
                draw.line(((x0 - x, y0 - y), (x0 + x, y0 - y)), fill=color)
                draw.line(((x0 - x, y0 + y), (x0 + x, y0 + y)), fill=color)
                draw.line(((x0 - y, y0 - x), (x0 + y, y0 - x)), fill=color)
                draw.line(((x0 - y, y0 + x), (x0 + y, y0 + x)), fill=color)
            else:
                draw.point((x0 + x, y0 + y), fill=color)
                draw.point((x0 + x, y0 - y), fill=color)
                draw.point((x0 - x, y0 + y), fill=color)
                draw.point((x0 - x, y0 - y), fill=color)
                draw.point((x0 + y, y0 + x), fill=color)
                draw.point((x0 + y, y0 - x), fill=color)
                draw.point((x0 - y, y0 + x), fill=color)
                draw.point((x0 - y, y0 - x), fill=color)

    def draw_circle(self, gpoint, radius, outline_color, fill_color):
        draw = ImageDraw.Draw(self.image)
        center = (gpoint.x, gpoint.y)
        if fill_color != self.COLOR_CLEAR:
            self._draw_circle(draw, center, radius, fill_color, fill=True)
        self._draw_circle(draw, center, radius, outline_color, fill=False)

    def draw_round_rect(self, grect, radius, outline_color, fill_color):
        rect_box = ((0, 0), (grect.size.w - 1, grect.size.h - 1))
        rect_image = self.tempimage((grect.size.w, grect.size.h))
        rect_draw = ImageDraw.Draw(rect_image)
        rect_draw.rectangle(rect_box, outline=outline_color, fill=fill_color)

        circ_box = ((0, 0), (radius * 2 + 1, radius * 2 + 1))
        circ_image = self.tempimage(circ_box[1])
        circ_draw = ImageDraw.Draw(circ_image)
        center = (radius, radius)
        if fill_color != self.COLOR_CLEAR:
            self._draw_circle(circ_draw, center, radius, fill_color, fill=True)
        self._draw_circle(circ_draw, center, radius, outline_color, fill=False)

        def fix_corner(sx, sy, cx, cy):
            rect_image.paste((0, 0), (sx, sy, sx + radius, sy + radius))
            corner_image = circ_image.crop((cx, cy, cx + radius, cy + radius))
            self.paste_image(corner_image, (sx, sy), rect_image)

        fix_corner(0, 0, 0, 0)
        fix_corner(grect.size.w - radius, 0, radius + 1, 0)
        fix_corner(0, grect.size.h - radius, 0, radius + 1)
        fix_corner(grect.size.w - radius, grect.size.h - radius,
                   radius + 1, radius + 1)

        self.paste_image(rect_image, (grect.origin.x, grect.origin.y))

    def _draw_text_line(self, text, dfont, text_box, alignment):
        text_image = self.tempimage(
            pmap(operator.sub, text_box[1], text_box[0]))

        left = 0
        for ch in text:
            glyph = dfont.get_glyph(ch)
            glyph.paste_to(text_image, (left, 0), self.text_color)
            left += glyph.advance

        draw_image = text_image.crop((0, 0, left, text_image.size[1]))

        if alignment == self.ALIGN_LEFT:
            offset = 0
        elif alignment == self.ALIGN_CENTER:
            offset = (text_image.size[0] - left) / 2
        elif alignment == self.ALIGN_RIGHT:
            offset = text_image.size[0] - left

        self.paste_image(draw_image,
                         (text_box[0][0] + offset, text_box[0][1]))

    def draw_text(self, text, font, box, alignment):
        # TODO: overflow, layout(?)
        text_box = ((box.origin.x, box.origin.y),
                    (box.origin.x + box.size.w, box.origin.y + box.size.h))

        for i, line in enumerate(text.splitlines()):
            line_box = (
                (text_box[0][0], text_box[0][1] + i * font.max_height),
                text_box[1])
            self._draw_text_line(line, font, line_box, alignment)
