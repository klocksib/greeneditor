class MapTile:

    def __init__(self, tset, t):
        self.id = 0
        if tset == "":
            self.tileset = "test"
        else:
            self.tileset = tset

        if t == "":
            self.tile = 0
        else:
            self.tile = t
            
        self.animaton = 0
