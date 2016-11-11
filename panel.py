import pygame as p 

class Panel(): 
    def __init__(self, top_x=0, top_y=0, width=0, height=0, bg_color=None, screen=None, visible=False, elements=[]): 
        self.top_x = top_x 
        self.top_y = top_y 
        self.origin = [self.top_x, self.top_y] 
        self.width = width 
        self.height = height 
        self.size = (self.width, self.height) 
        self.bg_color = bg_color 
        self.screen = screen 
        self.elements = elements 
        self.center = (self.top_x+self.width//2, self.top_y+self.height//2) 
        self.visible = visible 

    def render(self): 
        if self.visible: 
            p.draw.rect(self.screen, self.bg_color, (self.origin, self.size)) 