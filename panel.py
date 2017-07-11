import pygame as p

class Panel():
    def __init__(self, origin=(0, 0), width=0, height=0, bg_color=None, fg_color=None, screen=None, visible=False, elements=[], name=''):
        self.origin = origin
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.screen = screen
        self.elements = elements
        self.center = (self.origin[0]+self.width//2, self.origin[1]+self.height//2)
        self.visible = visible
        self.name = name

    def render(self, font):
        if self.visible:
            p.draw.rect(self.screen, self.bg_color, (self.origin, self.size))
            self.screen.blit(font.render(self.name, 1, self.fg_color), self.origin)
