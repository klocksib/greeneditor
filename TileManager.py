import logging
from TileSet import TileSet

class TileManager:

    def __init__(self):
        self.tilesets = []

    def append(self, tileset, path):
        logging.info(":: TileManager Loading: %s" % tileset)

        ts = TileSet("%s" % tileset, "%s" % path)
        self.tilesets.append(ts)

    def find_texture(self, tileset, idx):
        for t in self.tilesets:
            if t.name == tileset:
                return t.return_texture(idx)
