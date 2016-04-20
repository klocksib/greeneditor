import logging
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

class ToolPane:

    def __init__(self, tw, sh):
        self.toolbar_width = tw
        self.screen_height = sh

    def resize(self, tw, sh):
        self.toolbar_width = tw
        self.screen_height = sh
        
    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', 
                              (0, 0, 
                               self.toolbar_width, 0, 
                               self.toolbar_width, self.screen_height, 
                               0, self.screen_height)))
