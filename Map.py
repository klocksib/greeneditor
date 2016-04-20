import logging
import random
import yaml
from MapTile import MapTile

class Map:

    def __init__(self, mapname):
        logging.info(":: Initializing simple map class")
        logging.info("::  name: %s" % mapname)
        self.title = mapname
        self.map_data = []
        self.generate_map()

    def generate_map(self):
        self.width = 60
        self.height = 70

        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                r = random.randint(0, 80)
                t = MapTile("zelda1.png", r)
                row.append(t)
            self.map_data.append(row)

    def get_region(self, x, y, w, h):
        submap = []

        count_y = 0
        for row in self.map_data:
            if count_y <= h:
                submap.append(row[x:x+w])
        return submap
        #for row in self.map_data:
        #    if count_x >= x:
        #        submap.append(row[y:y+h])
        #    count_x = count_x + 1
        #return submap

    def get_tilesets(self):
        manifest = []
        for y in self.map_data:
            for tile in y:
                if tile.tileset in manifest:
                    pass
                else:
                    manifest.append(tile.tileset)

        return manifest

    def set_tile(self, x, y, tileset, tilenum):        
        row_count = 0
        for row in self.map_data:
            if row_count == y:
                logging.info(":: row count: %s" % row_count)
                tile = row[x]
                tile.tileset = tileset
                tile.tile = tilenum
                row[x] = tile
                break
            else:
                row_count = row_count + 1
        
    def save_map(self, filename):
        logging.info(":: saving map: %s" % filename)
        stream = file(filename, 'w')
        yaml.dump(self.map_data, stream)
        logging.info(":: complete")
        
    def load_map(self, filename):
        logging.info(":: load map: %s" % filename)
        stream = file(filename, 'r')
        data = yaml.load(stream)
        self.map_data = data
        logging.info(":: complete")
