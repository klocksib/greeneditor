import logging
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

class TitleBar:

    def __init__(self, title, x, y, w, size):
        self.title = title
        self.x = x
        self.y = y
        self.width = w
        self.size = size
        self.label = pyglet.text.Label(self.title,
                                       font_name='Lucida Grande',
                                       font_size=12,
                                       x=self.x+(self.width/2), y=self.y+(self.size/2),
                                       color=(0, 0, 0, 255),
                                       anchor_x='center', anchor_y='center')
        
    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', (self.x, self.y, 
                                      self.x+self.width, self.y, 
                                      self.x+self.width, (self.y+self.size), 
                                      self.x, self.y+self.size)))
        self.label.draw()

    def update_location(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y - dy
        self.label.x = self.label.x + dx
        self.label.y = self.label.y - dy
