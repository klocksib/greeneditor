import logging
from ProjectSettings import ProjectSettings
from Map import Map
from TileSet import TileSet
from TileManager import TileManager
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
from math import ceil

class MapEditor:

    def __init__(self, config, width, height, x):
        logging.info(":: Initializing GreenEngine")
        logging.info(":: Reading settings")
        self.options = config
        self.width = width - x
        self.height = height
        self.tile_size = 32
        self.x_origin = x
        self.y_origin = 0
        self.render_grid = True

        ##self.x_pos = 0
        #self.y_pos = 0
        
        logging.info(":: Loading default map")
        self.worldmap = Map(self.options.map)
        self.tilemanager = TileManager()

        tilesets = self.worldmap.get_tilesets()
        logging.info("::  tilesets present: %s" % tilesets)

        for gfx in tilesets:
            logging.info(":: spooling: %s/assets/tilesets/%s" % (self.options.get_path(), gfx))
            self.tilemanager.append("%s" % gfx, "%s/assets/tilesets" % self.options.get_path())
            
    def save(self, filename):
        self.worldmap.save_map("%s/assets/maps/%s" % (self.options.get_path(), filename))

    def load(self, filename):
        self.worldmap.load_map("%s/assets/maps/%s" % (self.options.get_path(), filename))
            
    def draw(self):
        x_lim = (self.width / self.tile_size) + 1
        y_lim = (self.height / self.tile_size) + 1
        y_lim = y_lim + 1
        
        mapregion = self.worldmap.map_data
        #mapregion = self.worldmap.get_region(0, 0, 10, 10)
        
        vertex = []
        batch = pyglet.graphics.Batch()
        img_batch = pyglet.graphics.Batch()
        
        x_idx = 0
        y_idx = 0
        for row in mapregion:
            if y_idx == y_lim:
                break
            for tile in row:
                self.tilemanager.find_texture(tile.tileset, tile.tile).blit((x_idx*self.tile_size) + self.x_origin, (y_idx*self.tile_size) + self.y_origin, 0, self.tile_size, self.tile_size)
                x_idx = x_idx + 1
                if x_idx == x_lim:
                    y_idx = y_idx + 1
                    x_idx = 0
                    break
        
        if self.render_grid == True:
            for y in range(1, y_lim):
                vertex.append(batch.add(2, pyglet.gl.GL_LINES, None, ('v2i', (self.x_origin, (y*self.tile_size)+self.y_origin, self.width+self.x_origin, (y*self.tile_size)+self.y_origin))))
                for x in range(0, x_lim + 1):
                    vertex.append(batch.add(2, pyglet.gl.GL_LINES, None, ('v2i', ((x*self.tile_size) + self.x_origin, self.y_origin, (x*self.tile_size) + self.x_origin, self.height))))

        batch.draw()

    def horiz_scroll(self, val):
        self.x_origin = self.x_origin + val

    def vert_scroll(self, val):
        self.y_origin = self.y_origin + val
            
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        logging.info(":: Mouse:")
        logging.info("::  x: %s  y: %s" % (x, y))
        logging.info("::  button: %s" % button)
        logging.info("::  modifiers: %s" % modifiers)
        map_x = int(ceil((x - self.x_origin) / self.tile_size))
        map_y = int(ceil(y / self.tile_size))

        logging.info(":: map_x: %s  map_y: %s" % (map_x, map_y))
        logging.info(":: tile_size: %s" % self.tile_size)
        self.worldmap.set_tile(map_x, map_y, "zelda1.png", 20)

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def toggle_grid(self):
        self.render_grid = not self.render_grid

    def resize(self, w, h):
        self.width = w
        self.height = h
