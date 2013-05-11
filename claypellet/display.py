from datetime import datetime

import pygame
import pygame.mask
import pygame.draw
import pygame.event
import pygame.display
import pygame.time
import pygame.image
from pygame.locals import SWSURFACE, QUIT, KEYDOWN, K_ESCAPE, K_q, K_r, K_s


from claypellet.render import PebbleGraphicsContext


class PebbleDisplay(object):
    def __init__(self, harness):
        self.harness = harness
        self.display = self.setup_display((154, 178))
        self.display.fill((127, 127, 127))
        self.fonts = {}

    def setup_display(self, screen_size):
        pygame.display.init()
        return pygame.display.set_mode(screen_size, SWSURFACE)

    def run(self):
        clock = pygame.time.Clock()
        self.harness.call_main()
        while True:
            events = pygame.event.get()
            for ev in events:
                if ev.type == QUIT:
                    return
                elif ev.type == KEYDOWN:
                    if ev.key in (K_q, K_ESCAPE):
                        return
                    elif ev.key == K_r:
                        self.harness.load_app(unload=True)
                        self.harness.call_main()
                    elif ev.key == K_s:
                        self.screenshot()
            should_render = self.harness.tick()
            if should_render:
                self.render()
                pygame.display.flip()
            clock.tick(25)

    def get_screen_rect(self):
        rect = pygame.Rect(0, 0, 144, 168)
        rect.center = self.display.get_rect().center
        return rect

    def render(self):
        screen_rect = self.get_screen_rect()
        gctx = PebbleGraphicsContext(self, screen_rect.size)
        self.harness.render(gctx)
        image = gctx.get_image()
        surface = pygame.image.fromstring(
            image.convert("RGBA").tostring(), image.size, "RGBA")
        self.display.blit(surface.convert_alpha(self.display), screen_rect)

    def screenshot(self):
        filename = "claypellet-screenshot-%s.png" % datetime.now().isoformat()
        surface = self.display.subsurface(self.get_screen_rect())
        pygame.image.save(surface, filename)
        print "Screenshot: %s" % filename
