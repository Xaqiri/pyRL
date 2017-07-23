import pygame as p

class FOV():
    def __init__(self, vision_range=5, level_width=0, level_height=0, fov_mode='unexplored'):
        self.RAYS = 360
        self.STEP = 3
        self.sintable = [
            0.00000, 0.01745, 0.03490, 0.05234, 0.06976, 0.08716, 0.10453,
            0.12187, 0.13917, 0.15643, 0.17365, 0.19081, 0.20791, 0.22495, 0.24192,
            0.25882, 0.27564, 0.29237, 0.30902, 0.32557, 0.34202, 0.35837, 0.37461,
            0.39073, 0.40674, 0.42262, 0.43837, 0.45399, 0.46947, 0.48481, 0.50000,
            0.51504, 0.52992, 0.54464, 0.55919, 0.57358, 0.58779, 0.60182, 0.61566,
            0.62932, 0.64279, 0.65606, 0.66913, 0.68200, 0.69466, 0.70711, 0.71934,
            0.73135, 0.74314, 0.75471, 0.76604, 0.77715, 0.78801, 0.79864, 0.80902,
            0.81915, 0.82904, 0.83867, 0.84805, 0.85717, 0.86603, 0.87462, 0.88295,
            0.89101, 0.89879, 0.90631, 0.91355, 0.92050, 0.92718, 0.93358, 0.93969,
            0.94552, 0.95106, 0.95630, 0.96126, 0.96593, 0.97030, 0.97437, 0.97815,
            0.98163, 0.98481, 0.98769, 0.99027, 0.99255, 0.99452, 0.99619, 0.99756,
            0.99863, 0.99939, 0.99985, 1.00000, 0.99985, 0.99939, 0.99863, 0.99756,
            0.99619, 0.99452, 0.99255, 0.99027, 0.98769, 0.98481, 0.98163, 0.97815,
            0.97437, 0.97030, 0.96593, 0.96126, 0.95630, 0.95106, 0.94552, 0.93969,
            0.93358, 0.92718, 0.92050, 0.91355, 0.90631, 0.89879, 0.89101, 0.88295,
            0.87462, 0.86603, 0.85717, 0.84805, 0.83867, 0.82904, 0.81915, 0.80902,
            0.79864, 0.78801, 0.77715, 0.76604, 0.75471, 0.74314, 0.73135, 0.71934,
            0.70711, 0.69466, 0.68200, 0.66913, 0.65606, 0.64279, 0.62932, 0.61566,
            0.60182, 0.58779, 0.57358, 0.55919, 0.54464, 0.52992, 0.51504, 0.50000,
            0.48481, 0.46947, 0.45399, 0.43837, 0.42262, 0.40674, 0.39073, 0.37461,
            0.35837, 0.34202, 0.32557, 0.30902, 0.29237, 0.27564, 0.25882, 0.24192,
            0.22495, 0.20791, 0.19081, 0.17365, 0.15643, 0.13917, 0.12187, 0.10453,
            0.08716, 0.06976, 0.05234, 0.03490, 0.01745, 0.00000, -0.01745, -0.03490,
            -0.05234, -0.06976, -0.08716, -0.10453, -0.12187, -0.13917, -0.15643,
            -0.17365, -0.19081, -0.20791, -0.22495, -0.24192, -0.25882, -0.27564,
            -0.29237, -0.30902, -0.32557, -0.34202, -0.35837, -0.37461, -0.39073,
            -0.40674, -0.42262, -0.43837, -0.45399, -0.46947, -0.48481, -0.50000,
            -0.51504, -0.52992, -0.54464, -0.55919, -0.57358, -0.58779, -0.60182,
            -0.61566, -0.62932, -0.64279, -0.65606, -0.66913, -0.68200, -0.69466,
            -0.70711, -0.71934, -0.73135, -0.74314, -0.75471, -0.76604, -0.77715,
            -0.78801, -0.79864, -0.80902, -0.81915, -0.82904, -0.83867, -0.84805,
            -0.85717, -0.86603, -0.87462, -0.88295, -0.89101, -0.89879, -0.90631,
            -0.91355, -0.92050, -0.92718, -0.93358, -0.93969, -0.94552, -0.95106,
            -0.95630, -0.96126, -0.96593, -0.97030, -0.97437, -0.97815, -0.98163,
            -0.98481, -0.98769, -0.99027, -0.99255, -0.99452, -0.99619, -0.99756,
            -0.99863, -0.99939, -0.99985, -1.00000, -0.99985, -0.99939, -0.99863,
            -0.99756, -0.99619, -0.99452, -0.99255, -0.99027, -0.98769, -0.98481,
            -0.98163, -0.97815, -0.97437, -0.97030, -0.96593, -0.96126, -0.95630,
            -0.95106, -0.94552, -0.93969, -0.93358, -0.92718, -0.92050, -0.91355,
            -0.90631, -0.89879, -0.89101, -0.88295, -0.87462, -0.86603, -0.85717,
            -0.84805, -0.83867, -0.82904, -0.81915, -0.80902, -0.79864, -0.78801,
            -0.77715, -0.76604, -0.75471, -0.74314, -0.73135, -0.71934, -0.70711,
            -0.69466, -0.68200, -0.66913, -0.65606, -0.64279, -0.62932, -0.61566,
            -0.60182, -0.58779, -0.57358, -0.55919, -0.54464, -0.52992, -0.51504,
            -0.50000, -0.48481, -0.46947, -0.45399, -0.43837, -0.42262, -0.40674,
            -0.39073, -0.37461, -0.35837, -0.34202, -0.32557, -0.30902, -0.29237,
            -0.27564, -0.25882, -0.24192, -0.22495, -0.20791, -0.19081, -0.17365,
            -0.15643, -0.13917, -0.12187, -0.10453, -0.08716, -0.06976, -0.05234,
            -0.03490, -0.01745, -0.00000
        ]
        self.costable = [
            1.00000, 0.99985, 0.99939, 0.99863, 0.99756, 0.99619, 0.99452,
            0.99255, 0.99027, 0.98769, 0.98481, 0.98163, 0.97815, 0.97437, 0.97030,
            0.96593, 0.96126, 0.95630, 0.95106, 0.94552, 0.93969, 0.93358, 0.92718,
            0.92050, 0.91355, 0.90631, 0.89879, 0.89101, 0.88295, 0.87462, 0.86603,
            0.85717, 0.84805, 0.83867, 0.82904, 0.81915, 0.80902, 0.79864, 0.78801,
            0.77715, 0.76604, 0.75471, 0.74314, 0.73135, 0.71934, 0.70711, 0.69466,
            0.68200, 0.66913, 0.65606, 0.64279, 0.62932, 0.61566, 0.60182, 0.58779,
            0.57358, 0.55919, 0.54464, 0.52992, 0.51504, 0.50000, 0.48481, 0.46947,
            0.45399, 0.43837, 0.42262, 0.40674, 0.39073, 0.37461, 0.35837, 0.34202,
            0.32557, 0.30902, 0.29237, 0.27564, 0.25882, 0.24192, 0.22495, 0.20791,
            0.19081, 0.17365, 0.15643, 0.13917, 0.12187, 0.10453, 0.08716, 0.06976,
            0.05234, 0.03490, 0.01745, 0.00000, -0.01745, -0.03490, -0.05234, -0.06976,
            -0.08716, -0.10453, -0.12187, -0.13917, -0.15643, -0.17365, -0.19081,
            -0.20791, -0.22495, -0.24192, -0.25882, -0.27564, -0.29237, -0.30902,
            -0.32557, -0.34202, -0.35837, -0.37461, -0.39073, -0.40674, -0.42262,
            -0.43837, -0.45399, -0.46947, -0.48481, -0.50000, -0.51504, -0.52992,
            -0.54464, -0.55919, -0.57358, -0.58779, -0.60182, -0.61566, -0.62932,
            -0.64279, -0.65606, -0.66913, -0.68200, -0.69466, -0.70711, -0.71934,
            -0.73135, -0.74314, -0.75471, -0.76604, -0.77715, -0.78801, -0.79864,
            -0.80902, -0.81915, -0.82904, -0.83867, -0.84805, -0.85717, -0.86603,
            -0.87462, -0.88295, -0.89101, -0.89879, -0.90631, -0.91355, -0.92050,
            -0.92718, -0.93358, -0.93969, -0.94552, -0.95106, -0.95630, -0.96126,
            -0.96593, -0.97030, -0.97437, -0.97815, -0.98163, -0.98481, -0.98769,
            -0.99027, -0.99255, -0.99452, -0.99619, -0.99756, -0.99863, -0.99939,
            -0.99985, -1.00000, -0.99985, -0.99939, -0.99863, -0.99756, -0.99619,
            -0.99452, -0.99255, -0.99027, -0.98769, -0.98481, -0.98163, -0.97815,
            -0.97437, -0.97030, -0.96593, -0.96126, -0.95630, -0.95106, -0.94552,
            -0.93969, -0.93358, -0.92718, -0.92050, -0.91355, -0.90631, -0.89879,
            -0.89101, -0.88295, -0.87462, -0.86603, -0.85717, -0.84805, -0.83867,
            -0.82904, -0.81915, -0.80902, -0.79864, -0.78801, -0.77715, -0.76604,
            -0.75471, -0.74314, -0.73135, -0.71934, -0.70711, -0.69466, -0.68200,
            -0.66913, -0.65606, -0.64279, -0.62932, -0.61566, -0.60182, -0.58779,
            -0.57358, -0.55919, -0.54464, -0.52992, -0.51504, -0.50000, -0.48481,
            -0.46947, -0.45399, -0.43837, -0.42262, -0.40674, -0.39073, -0.37461,
            -0.35837, -0.34202, -0.32557, -0.30902, -0.29237, -0.27564, -0.25882,
            -0.24192, -0.22495, -0.20791, -0.19081, -0.17365, -0.15643, -0.13917,
            -0.12187, -0.10453, -0.08716, -0.06976, -0.05234, -0.03490, -0.01745,
            -0.00000, 0.01745, 0.03490, 0.05234, 0.06976, 0.08716, 0.10453, 0.12187,
            0.13917, 0.15643, 0.17365, 0.19081, 0.20791, 0.22495, 0.24192, 0.25882,
            0.27564, 0.29237, 0.30902, 0.32557, 0.34202, 0.35837, 0.37461, 0.39073,
            0.40674, 0.42262, 0.43837, 0.45399, 0.46947, 0.48481, 0.50000, 0.51504,
            0.52992, 0.54464, 0.55919, 0.57358, 0.58779, 0.60182, 0.61566, 0.62932,
            0.64279, 0.65606, 0.66913, 0.68200, 0.69466, 0.70711, 0.71934, 0.73135,
            0.74314, 0.75471, 0.76604, 0.77715, 0.78801, 0.79864, 0.80902, 0.81915,
            0.82904, 0.83867, 0.84805, 0.85717, 0.86603, 0.87462, 0.88295, 0.89101,
            0.89879, 0.90631, 0.91355, 0.92050, 0.92718, 0.93358, 0.93969, 0.94552,
            0.95106, 0.95630, 0.96126, 0.96593, 0.97030, 0.97437, 0.97815, 0.98163,
            0.98481, 0.98769, 0.99027, 0.99255, 0.99452, 0.99619, 0.99756, 0.99863,
            0.99939, 0.99985, 1.00000
        ]
        self.level_dimensions = (level_width, level_height)
        self.fov_mode = fov_mode
        self.visible_tiles = []
        if fov_mode == 'unexplored':
            self.explored_tiles = [[0]*level_height for x in range(level_width)]
        elif fov_mode == 'explored':
            self.explored_tiles = [[1]*level_height for x in range(level_width)]
        else:
            print('Fov mode not set')
        self.visible_tiles = []
        self.explored_tiles = []
        self.vision_range = vision_range

    def update(self, entities=None, items=None, level=None):
        '''for i in self.visible_tiles:
            try:
                i.visible = False
            except:
                pass
        for i in self.explored_tiles:
            try:
                i.visible = False
            except:
                pass'''
        self.visible_tiles = []
        self.visible_tiles.append((entities[0].x, entities[0].y))
        #if level[entities[0].x][entities[0].y] not in self.explored_tiles:
        #    self.explored_tiles.append(level[entities[0].x][entities[0].y])
        for i in range(0, self.RAYS, self.STEP):
            angle_x = self.sintable[i]
            angle_y = self.costable[i]
            x = entities[0].x
            y = entities[0].y
            for z in range(self.vision_range):
                x += angle_x
                y += angle_y
                tile = int(round(x)),int(round(y))
                if tile not in self.visible_tiles:
                    self.visible_tiles.append(tile)


                try:
                    #tile = int(round(x)),int(round(y))
                    if tile not in self.explored_tiles and tile != (entities[0].x, entities[0].y):
                        self.explored_tiles.append(tile)
                except:
                    pass
                if level[int(round(x))][int(round(y))] == 1:
                    break
