from PIL import Image, ImageDraw

from .utils import Rect


class PebbleGraphicsContext(object):
    COLOR_BLACK = (0, 255)
    COLOR_WHITE = (255, 255)
    COLOR_CLEAR = (192, 0)

    COMP_ASSIGN = 'assign'
    COMP_ASSIGN_INVERTED = 'assign_inverted'
    COMP_OR = 'or'
    COMP_AND = 'and'
    COMP_CLEAR = 'clear'

    ALIGN_LEFT = 'left'
    ALIGN_CENTER = 'center'
    ALIGN_RIGHT = 'right'

    OVERFLOW_WORD_WRAP = 'word_wrap'
    OVERFLOW_ELLIPSIS = 'overflow_ellipsis'

    fill_color = COLOR_BLACK
    stroke_color = COLOR_WHITE
    text_color = COLOR_WHITE

    compositing_mode = COMP_ASSIGN

    def __init__(self, display, image, rect):
        if image is None:
            rect = Rect((0, 0), (144, 168))
            image = Image.new('LA', rect.size, (0, 0))
        self._display = display
        self.image = image
        self.rect = rect
        self._flattened = False
        self._children = []

    def get_child_context(self, grect):
        frame = Rect.from_grect(grect).move(self.rect.origin)
        child = PebbleGraphicsContext(self._display, self.image, frame)

        # Child inherits properties.
        child.fill_color = self.fill_color
        child.stroke_color = self.stroke_color
        child.text_color = self.text_color

        self._children.append(child)
        return child

    def get_image(self):
        return self.image

    def tempimage(self, size, color=(0, 0)):
        return Image.new('LA', size, color)

    def paste_image(self, src, origin, dst=None):
        if dst is None:
            dst = self.image
        dst.paste(src, origin, src.split()[-1])

    def _compose_assign(self, bg_pixel, im_pixel):
        if im_pixel[0]:
            return self.COLOR_WHITE
        else:
            return self.COLOR_BLACK

    def _compose_assign_inverted(self, bg_pixel, im_pixel):
        if im_pixel[0]:
            return self.COLOR_BLACK
        else:
            return self.COLOR_WHITE

    def _compose_or(self, bg_pixel, im_pixel):
        if im_pixel[0]:
            return self.COLOR_WHITE
        else:
            return bg_pixel

    def _compose_and(self, bg_pixel, im_pixel):
        print "I don't know how to do 'GCompOpAnd', and it seems broken."
        return bg_pixel

    def _compose_clear(self, bg_pixel, im_pixel):
        if im_pixel[0]:
            return self.COLOR_BLACK
        else:
            return bg_pixel

    def compose_image(self, image, rect):
        bg_image = self.image.crop(rect.get_box())

        comp_func = {
            self.COMP_ASSIGN: self._compose_assign,
            self.COMP_ASSIGN_INVERTED: self._compose_assign_inverted,
            self.COMP_OR: self._compose_or,
            self.COMP_AND: self._compose_and,
            self.COMP_CLEAR: self._compose_clear,
        }[self.compositing_mode]

        pixels = [comp_func(bg_px, im_px) if im_px[1] else bg_px
                  for bg_px, im_px in zip(bg_image.getdata(), image.getdata())]
        bg_image.putdata(pixels)
        self.paste_image(bg_image, rect.origin)

    def bgfill(self, color):
        self.image.paste(color, Rect((0, 0), self.image.size).get_box())

    def draw_line(self, gpoint0, gpoint1):
        draw = ImageDraw.Draw(self.image)
        p0 = self.rect.move((gpoint0.x, gpoint0.y)).origin
        p1 = self.rect.move((gpoint1.x, gpoint1.y)).origin
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
        center = self.rect.move((gpoint.x, gpoint.y)).origin
        if fill_color != self.COLOR_CLEAR:
            self._draw_circle(draw, center, radius, fill_color, fill=True)
        self._draw_circle(draw, center, radius, outline_color, fill=False)

    def draw_round_rect(self, grect, radius, outline_color, fill_color):
        rect = Rect.from_grect(grect).move(self.rect.origin)

        rect_box = Rect((0, 0), (rect.w - 1, rect.h - 1))
        rect_image = self.tempimage((rect.w, rect.h))
        rect_draw = ImageDraw.Draw(rect_image)
        rect_draw.rectangle(rect_box.get_box(),
                            outline=outline_color, fill=fill_color)

        circ_box = Rect((0, 0), (radius * 2 + 1, radius * 2 + 1))
        circ_image = self.tempimage(circ_box.size)
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
        fix_corner(rect.w - radius, 0, radius + 1, 0)
        fix_corner(0, rect.h - radius, 0, radius + 1)
        fix_corner(rect.w - radius, rect.h - radius, radius + 1, radius + 1)

        self.paste_image(rect_image, rect.origin)

    def _draw_text_line(self, text, dfont, text_box, alignment):
        text_image = self.tempimage(text_box.size)

        left = 0
        for ch in text:
            glyph = dfont.get_glyph(ch)
            glyph.paste_to(text_image, (left, 0), self.text_color)
            left += glyph.advance

        draw_box = Rect(text_box.origin, (left, text_box.h))
        draw_image = text_image.crop((0, 0, draw_box.w, draw_box.h))

        if alignment == self.ALIGN_LEFT:
            pass
        elif alignment == self.ALIGN_CENTER:
            draw_box = draw_box.move(((text_box.w - left) / 2, 0))
        elif alignment == self.ALIGN_RIGHT:
            draw_box = draw_box.move((text_box.w - left, 0))

        self.paste_image(draw_image, draw_box.origin)

    def draw_text(self, text, font, grect, overflow_mode, alignment):
        # TODO: overflow, layout(?)
        text_box = Rect.from_grect(grect).move(self.rect.origin)

        for i, line in enumerate(text.splitlines()):
            line_box = Rect((text_box.x, text_box.y + i * font.max_height),
                            (text_box.w, text_box.h - i * font.max_height))
            self._draw_text_line(line, font, line_box, alignment)

    def draw_bitmap(self, bitmap, grect_bmp, grect):
        bmp_rect = Rect.from_grect(grect_bmp)
        rect = Rect.from_grect(grect).move(self.rect.origin)
        image = self.tempimage(rect.size, self.COLOR_BLACK)
        bmp_image = bitmap.get_image().convert("LA")

        x = bmp_rect.x
        y = bmp_rect.y
        while y < rect.h:
            while x < rect.w:
                image.paste(bmp_image, (x, y))
                x += bmp_rect.x * 2 + bmp_rect.w
            x = bmp_rect.x
            y += bmp_rect.y * 2 + bmp_rect.h

        self.compose_image(image, rect)

    def draw_rotated_bitmap(self, bitmap, grect_bmp, src_ic, dest_ic, angle):
        angle = 360 - angle  # Pebble rotates CW, PIL rotates CCW.
        ic_offset = (dest_ic.x - src_ic.x, dest_ic.y - src_ic.y)
        image = self.tempimage(self.rect.size)
        image.paste(bitmap.get_image(), ic_offset)
        image = image.rotate(angle, Image.BILINEAR)
        self.compose_image(image, self.rect)
