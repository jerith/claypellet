import pygame
import pygame.mask
import pygame.draw
import pygame.event
import pygame.display
import pygame.time
import pygame.image
from pygame.locals import SWSURFACE, QUIT, KEYDOWN, K_ESCAPE, BLEND_MIN


class PebbleDisplay(object):
    def __init__(self, harness):
        self.harness = harness
        pygame.init()
        surface = pygame.display.set_mode((154, 178), SWSURFACE)
        surface.fill((127, 127, 127))
        self.fonts = {}

    def run(self):
        clock = pygame.time.Clock()
        self.harness.call_main()
        while True:
            events = pygame.event.get()
            for ev in events:
                if ev.type == QUIT:
                    return
                elif ev.type == KEYDOWN:
                    if ev.key == K_ESCAPE:
                        return
            should_render = self.harness.tick()
            if should_render:
                self.render()
                pygame.display.flip()
            clock.tick(25)

    def render(self):
        dsurface = pygame.display.get_surface()
        surface = pygame.Surface((144, 168)).convert_alpha()
        gctx = PebbleGraphicsContext(self, surface)
        self.harness.render(gctx)
        dsurface.blit(surface, pygame.Rect(5, 5, 144, 168))


def mkrect(grect):
    return pygame.Rect(grect.origin.x, grect.origin.y,
                       grect.size.w, grect.size.h)


class PebbleGraphicsContext(object):
    COLOR_BLACK = (0, 0, 0, 255)
    COLOR_WHITE = (255, 255, 255, 255)
    COLOR_CLEAR = (255, 127, 0, 0)

    ALIGN_LEFT = 'left'
    ALIGN_CENTER = 'center'
    ALIGN_RIGHT = 'right'

    stroke_color = COLOR_BLACK
    fill_color = COLOR_BLACK
    text_color = COLOR_BLACK

    def __init__(self, disp, surface):
        self._disp = disp
        self.surface = surface

    def get_dfont(self, font):
        if font not in self._disp.fonts:
            self._disp.fonts[font] = PebbleDisplayFont(font)
        return self._disp.fonts[font]

    def get_child_context(self, frame):
        surface = self.surface.subsurface(mkrect(frame))
        return PebbleGraphicsContext(self._disp, surface)

    def tempsurface(self, size):
        surface = pygame.Surface(size).convert_alpha()
        surface.fill((0, 0, 0, 0))
        return surface

    def draw_round_rect(self, grect, radius, color, width=0):
        rect = mkrect(grect)

        surface = self.tempsurface(rect.size)
        pygame.draw.rect(surface, color, surface.get_rect(), width)

        corners = self.tempsurface((radius * 2, radius * 2))
        pygame.draw.ellipse(corners, color, corners.get_rect(), width)

        def fix_corner(sx, sy, cx, cy):
            surface.fill((0, 0, 0, 0), (sx, sy, radius, radius))
            surface.blit(corners, (sx, sy), (cx, cy, radius, radius))

        fix_corner(0, 0, 0, 0)
        fix_corner(rect.width - radius, 0, radius, 0)
        fix_corner(0, rect.height - radius, 0, radius)
        fix_corner(rect.width - radius, rect.height - radius, radius, radius)

        self.surface.blit(surface, rect.topleft)

    def draw_text(self, text, font, box, alignment):
        # TODO: overflow, alignment, layout(?)
        rect = mkrect(box)
        text_surface = self.tempsurface(rect.size)
        dfont = self.get_dfont(font)
        left, top, width = 0, 0, 0

        for ch in text:
            glyph = dfont.get_glyph(ch)
            glyph.blit_to(text_surface, (left, top), self.text_color)
            left += glyph.advance

        text_rect = text_surface.get_rect()
        text_rect.width = left

        if alignment == self.ALIGN_LEFT:
            text_rect.topleft = rect.topleft
        elif alignment == self.ALIGN_CENTER:
            text_rect.midtop = rect.midtop
        elif alignment == self.ALIGN_RIGHT:
            text_rect.topright = rect.topright

        self.surface.blit(text_surface, text_rect)


class PebbleDisplayFont(object):
    def __init__(self, font):
        self._font = font
        self.glyphs = {}

    def get_glyph(self, ch):
        if ch not in self.glyphs:
            codepoint = ord(ch)
            glyph_data = self._font.get_glyph(codepoint)
            self.glyphs[ch] = PebbleDisplayGlyph(codepoint, glyph_data)
        return self.glyphs[ch]


class PebbleDisplayGlyph(object):
    def __init__(self, codepoint, glyph_data):
        self.codepoint = codepoint
        self._glyph_data = glyph_data
        self.rect = pygame.Rect(
            glyph_data['offset_left'], glyph_data['offset_top'],
            glyph_data['width'], glyph_data['height'])
        self.surface = pygame.image.fromstring(
            glyph_data['data_string'], self.rect.size, 'RGBA')
        self.advance = glyph_data['advance']

    def blit_to(self, surface, position, color):
        tempsurface = self.surface.copy()
        tempsurface.fill(color, special_flags=BLEND_MIN)
        surface.blit(tempsurface, self.rect.move(position))
