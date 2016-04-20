import logging
from pyglet import image

class TileSet:
    def __init__(self, name, path):
        self.name = name
        self.size = 64
        self.textures = []

        self.parse_tiles("%s/%s" % (path, self.name))

    def parse_tiles(self, name):
        logging.info("::reading tileset")

        img = image.load(name)
        w, h = img.width, img.height

        self.tiles_per_row = w / self.size
        self.tiles_per_column = h / self.size

        logging.info(":: tileset properties")
        logging.info("::  name: %s" % self.name)
        logging.info("::  dimensions: %ix%i" % (w, h))
        logging.info("::  tile size %i" % self.size)
        logging.info("::  tiles: %ix%i" % (self.tiles_per_row, self.tiles_per_column))

        self.img_grid = image.ImageGrid(img, self.tiles_per_row, self.tiles_per_column)
        self.textures = image.TextureGrid(self.img_grid)
        
    def return_texture(self, tile):
        return self.textures[tile]
