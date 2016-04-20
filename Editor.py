import logging
from ProjectSettings import ProjectSettings
from Map import Map
from TileSet import TileSet
from TileManager import TileManager
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
from math import ceil
from MapEditor import MapEditor
from ToolPane import ToolPane
from TSetWindow import TSetWindow

class Editor:

    def __init__(self, project, path):
        logging.info(":: Initializing Editor")
        logging.info(":: Reading settings")
        self.options = ProjectSettings(project, path)
        self.width = 1024
        self.height = 768

        logging.info(":: Starting windowing system")
        self.pyglet_window = pyglet.window.Window(self.width, self.height, resizable=True)
        self.pyglet_window.set_caption("Green Editor")
        self.pyglet_window.set_visible(True)
        
        # Set up event handlers
        self.keyboard = key.KeyStateHandler()
        #self.pyglet_window.push_handlers(self.keyboard)
        self.pyglet_window.push_handlers(self.on_key_press)
        self.pyglet_window.push_handlers(self.on_mouse_drag)
        self.pyglet_window.push_handlers(self.on_mouse_motion)
        self.pyglet_window.push_handlers(self.on_mouse_press)
        self.pyglet_window.push_handlers(self.on_resize)
        self.pyglet_window.push_handlers(self.on_draw)

        # Internal 'windows'
        self.tools_pane = ToolPane(150, self.height)
        self.mapeditor_pane = MapEditor(self.options, self.width, self.height, 150)
        self.tileset_window = TSetWindow()
        
        self.should_render = True
        self.input_timeout = 0
        #self.active_window = "MapEditor"
        self.active_window = "TileSet_Window"
        
        pyglet.clock.schedule(self.update)
        pyglet.app.run()

    def update(self, dt):
        pass

    def on_draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.mapeditor_pane.draw()
        self.tools_pane.draw()
        self.tileset_window.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.Q:
            quit(1)
        elif symbol == key.S:
            self.mapeditor_pane.save("test.yaml")
        elif symbol == key.L:
            self.mapeditor_pane.load("test.yaml")
        elif symbol == key.MINUS:
            self.tile_size = self.tile_size - 1
        elif symbol == key.PLUS:
            self.tile_size = self.tile_size + 1
        elif symbol == key.R:
            self.mapeditor_pane.toggle_grid()
        elif symbol == key.RIGHT:
            self.mapeditor_pane.horiz_scroll(-1)
        elif symbol == key.UP:
            self.mapeditor_pane.vert_scroll(-1)
        elif symbol == key.LEFT:
            self.mapeditor_pane.horiz_scroll(1)
        elif symbol == key.DOWN:
            self.mapeditor_pane.vert_scroll(1)
        
    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        print "on_mouse_drag:"
        print "  x: %s" % x
        print "  y: %s" % y
        print "  button: %s" % button
        
        if button & mouse.LEFT:
            if self.active_window == "TileSet_Window":
                self.tileset_window.on_mouse_drag(x, y, dx, dy, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        print "on_mouse_motion:"
        print "  x: %s" % x
        print "  y: %s" % y

    def on_mouse_press(self, x, y, button, modifiers):
        print "on_mouse_press"
        print "  x: %s" % x
        print "  y: %s" % y
        print "  button: %s" % button
        if self.active_window == "MapEditor":
            self.mapeditor_pane.on_mouse_press(x, y, button, modifiers)
        elif self.active_window == "TileSet_Window":
            self.tileset_window.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        print "on_mouse_release"
        print "  x: %s" % x
        print "  y: %s" % y
        print "  button: %s" % button

    def on_resize(self, w, h):
        logging.info("Resizing: %sx%s" % (w, h))
        self.width = w
        self.height = h
        self.mapeditor_pane.resize(self.width, self.height)
        self.tools_pane.resize(150, self.height)
