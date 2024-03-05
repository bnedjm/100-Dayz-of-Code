import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk

MARGIN = 8

class TicTacToe(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="TicTacToe")
        self.set_default_size(800, 600)
        self.connect("destroy", Gtk.main_quit)

        # View stack
        self.stack = Gtk.Stack()
        
        # Navigation bar
        self.start_button = Gtk.Button(label="Start Game")
        self.start_button.connect("clicked", self.start_game)
        self.restart_button = Gtk.Button(label="Rematch")
        self.restart_button.connect("clicked", self.restart_game)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)
        self.navigation_bar = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=MARGIN
        )

        self.navigation_bar.set_margin_top(MARGIN)
        self.navigation_bar.set_margin_end(MARGIN)
        self.navigation_bar.set_margin_bottom(MARGIN)
        self.navigation_bar.set_margin_start(MARGIN)

        self.box.pack_start(self.navigation_bar, False, False, 0)

        self.navigation_bar.pack_start(self.start_button, True, True, 0)
        self.navigation_bar.pack_start(self.restart_button, True, True, 0)

        self.box.pack_start(self.stack, True, True, 0)

    def start_game(self):
        pass

    def restart_game(self):
        pass

win = TicTacToe()
win.show_all()
Gtk.main()