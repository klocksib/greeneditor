import logging
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
from TitleBar import TitleBar

class TSetWindow:

    def __init__(self):
        self.title = "Tilesets"
        self.tileset = "Null"
        self.width = 700
        self.height = 400
        self.x_origin = 100
        self.y_origin = 100
        self.titlebar = TitleBar(self.title, 
                                 self.x_origin, 
                                 self.y_origin+self.height, 
                                 self.width, 
                                 25)
        self.active = False
        
    def draw(self):
        self.titlebar.draw()
        self.draw_window()

    def draw_contents(self):
        pass

    def draw_window(self):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i', (self.x_origin, self.y_origin, self.x_origin+self.width, self.y_origin))
        )

        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i', (self.x_origin+self.width, self.y_origin, self.x_origin+self.width, self.y_origin+self.height))
        )

        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i', (self.x_origin+self.width, self.y_origin+self.height, self.x_origin, self.y_origin+self.height))
        )

        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i', (self.x_origin, self.y_origin+self.height, self.x_origin, self.y_origin))
        )

    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if True:#is_in_titlebar(x, y):
            self.x_origin = self.x_origin + dx
            self.y_origin = self.y_origin - dy
            self.titlebar.update_location(dx, dy)
        else:
            pass
        
    def on_mouse_press(self, x, y, button, modifiers):
        pass
