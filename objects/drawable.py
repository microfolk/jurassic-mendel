import libtcodpy as libtcod

class DrawableObject:

    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y
    
    def draw(self):
        libtcod.console_put_char(0, self.x,  self.y, self.sprite, libtcod.BKGND_NONE)

    def clear(self):
        libtcod.console_put_char(0, self.x, self.y, ' ', libtcod.BKGND_NONE)
