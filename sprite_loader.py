import pygame as p 

class SpriteLoader(object):
    ''' Loads a tile sheet and returns a specified number of sprites ''' 
    def __init__(self, sprite_sheet=None, tile_size=12, start=(0, 0), base_size=16, sprite_margin=1, col=1, rows=1): 
        self.sprites = [[0]*rows for x in range(col)] 
        self.start = (start[0]+sprite_margin, start[1]+sprite_margin)
        for j in range(rows): 
            for i in range(col): 
                location = (self.start[0]+base_size*i+sprite_margin*i, self.start[1]+base_size*j+sprite_margin*j) 
                self.sprites[i][j] = sprite_sheet.subsurface(p.Rect(location, (base_size, base_size))) 
                self.sprites[i][j] = p.transform.scale(self.sprites[i][j], (tile_size, tile_size)) 
        
    def sprite(self, x, y): 
        return self.frames[self.col*y+x] 
