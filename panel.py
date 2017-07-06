import pygame as p

class Panel():
    def __init__(self, origin=(0, 0), width=0, height=0, bg_color=None, screen=None, visible=False, elements=[]):
        self.origin = origin
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.bg_color = bg_color
        self.screen = screen
        self.elements = elements
        self.center = (self.origin[0]+self.width//2, self.origin[1]+self.height//2)
        self.visible = visible

    def render(self):
        if self.visible:
            p.draw.rect(self.screen, self.bg_color, (self.origin, self.size))
