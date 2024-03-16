# # import gi
# # gi.require_version("Gtk", "4.0")
# # from gi.repository import Gtk

# # class TicTacToe(Gtk.Application):
# #     def __init__(self):
# #         super().__init__(application_id="com.example.GtkApplication")
# #         win = Gtk.ApplicationWindow()
# #         self.add_window(win)
# # # class TTTMainWindow(Gtk.ApplicationWindow):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.set_title(title="TicTacToe")
# # #         self.button = Gtk.Button(label="Hello World!")
# # #         self.add(self.button)

# # # def on_activate(win):
# # #     # win = Gtk.ApplicationWindow(application=app)
# # #     btn = Gtk.Button(label='Hello, World!')
# # #     btn.connect('clicked', lambda x: win.close())
# # #     win.set_child(btn)
# # #     win.present()

# # def activate(app):
# #     win = Gtk.ApplicationWindow()
# #     app.add_window(win)

# # app = TicTacToe()
# # app.activate()
# # # activate(app)
# # # app.add_window(win)
# # # app = TTTMainWindow()

# # app.run(None)

# #!/usr/bin/env python3

# import gi

# gi.require_version("Gtk", "3.0")
# from gi.repository import GLib, Gtk

# import requests
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas


# import matplotlib.style as mpl_style

# HOST_NAME_PREF = "localhost"
# PORT_NUMBER_PREF = 8000
# REFRESH_TIME_PREF = 1000
# MARGIN = 8


# class SensorsView(Gtk.Box):
#     """
#     Represents the view for displaying sensor data in a list format.
#     """

#     def __init__(self):
#         """
#         Initializes the SensorsView object.
#         """
#         Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

#         self.scrolled_window = Gtk.ScrolledWindow()
#         self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
#         self.list_store = Gtk.ListStore(str, float, str)
#         self.pack_start(self.scrolled_window, True, True, 0)

#         self.tree_view = Gtk.TreeView(model=self.list_store)

#         self.name_column = Gtk.TreeViewColumn("Name")
#         self.value_column = Gtk.TreeViewColumn("Value")
#         self.unit_column = Gtk.TreeViewColumn("Unit")

#         self.name_renderer = Gtk.CellRendererText()
#         self.value_renderer = Gtk.CellRendererText()
#         self.unit_renderer = Gtk.CellRendererText()

#         self.name_column.pack_start(self.name_renderer, True)
#         self.value_column.pack_start(self.value_renderer, True)
#         self.unit_column.pack_start(self.unit_renderer, True)

#         self.name_column.add_attribute(self.name_renderer, "text", 0)
#         self.value_column.add_attribute(self.value_renderer, "text", 1)
#         self.unit_column.add_attribute(self.unit_renderer, "text", 2)

#         self.tree_view.append_column(self.name_column)
#         self.tree_view.append_column(self.value_column)
#         self.tree_view.append_column(self.unit_column)

#         self.scrolled_window.add(self.tree_view)

#         # self.updateSensorsData()

#         GLib.timeout_add(REFRESH_TIME_PREF, self.updateSensorsData)

#     def updateSensorsData(self):
#         """
#         Updates the sensor data displayed in the view.
#         """
#         api_endpoint = (
#             "http://" + HOST_NAME_PREF + ":" + str(PORT_NUMBER_PREF) + "/sensors/all"
#         )
#         response = requests.get(api_endpoint)
#         if response.status_code == 200:
#             data = response.json()
#             self.list_store.clear()
#             for j_key, j_value in data.items():
#                 name = j_value["name"] if j_value["name"] else j_key
#                 value = j_value["value"]

#                 unit = j_value.get("unit", "-") or "-"
#                 self.list_store.append([name, value, unit])

#         return True


# class PlotsView(Gtk.Box):
#     """
#     Represents the view for displaying sensor data in plots.
#     """

#     def __init__(self):
#         """
#         Initializes the PlotsView object.
#         """
#         Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

#         self.set_margin_top(MARGIN)
#         self.set_margin_end(MARGIN)
#         self.set_margin_bottom(MARGIN)
#         self.set_margin_start(MARGIN)

#         native_theme = {
#             "text.color": "#454242",
#             "xtick.color": "#242424",
#             "ytick.color": "#454242",
#             "grid.color": "#454242",
#             "axes.facecolor": "#242424",
#             "axes.edgecolor": "#242424",
#             "axes.labelcolor": "#454242",
#             "figure.facecolor": "#242424",
#             "figure.edgecolor": "#242424",
#             "grid.linestyle": "--",
#         }

#         mpl_style.use(native_theme)

#         self.figure = Figure()
#         self.canvas = FigureCanvas(self.figure)
#         self.pack_start(self.canvas, True, True, 0)

#         self.x_data = []
#         self.temperature_data = []
#         self.pressure_data = []
#         self.humidity_data = []

#         self.axis = self.figure.add_subplot(1, 1, 1)
#         self.axis.set_title("Temperature [°C]", color="#D3D3D3")
#         self.line1 = self.axis.plot([], [], marker="o", color="#F66151")[0]
#         self.axis.grid(axis="y")
#         # self.figure.subplots_adjust(top=1, right=0.91, bottom=0.05, left=0.09)

#         self.sample_counter = 0
#         # self.updateSensorsPlot()

#         # GLib.timeout_add(REFRESH_TIME_PREF, self.updateSensorsPlot)

#     def updateSensorsPlot(self):
#         """
#         Updates the sensor plot with new data.
#         """
#         api_endpoint = (
#             "http://" + HOST_NAME_PREF + ":" + str(PORT_NUMBER_PREF) + "/sensors/all"
#         )

#         self.response = requests.get(api_endpoint)

#         self.temperature = self.response.json()["temperature"]["value"]
#         self.pressure = self.response.json()["pressure"]["value"]
#         self.humidity = self.response.json()["humidity"]["value"]

#         self.sample_counter += 1
#         self.x_data.append(self.sample_counter)
#         self.temperature_data.append(self.temperature)
#         self.pressure_data.append(self.pressure)
#         self.humidity_data.append(self.humidity)

#         self.x_data = self.x_data[-10:]
#         self.temperature_data = self.temperature_data[-10:]
#         self.pressure_data = self.pressure_data[-10:]
#         self.humidity_data = self.humidity_data[-10:]

#         self.line1.set_data(self.x_data, self.temperature_data)

#         self.axis.relim()
#         self.axis.autoscale_view(True, True, True)

#         self.canvas.draw()

#         return True


# class ControlView(Gtk.Box):
#     """
#     Represents the view for controlling the LED strip.
#     """

#     def __init__(self):
#         """
#         Initializes the ControlView object.
#         """
#         Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

#         self.led_color = (0, 0, 0, 0)

#         self.set_margin_top(MARGIN * 10)
#         self.set_margin_end(MARGIN * 20)
#         self.set_margin_bottom(MARGIN * 10)
#         self.set_margin_start(MARGIN * 20)

#         self.grid = Gtk.Grid()
#         self.grid.set_column_homogeneous(True)
#         self.grid.set_row_spacing(MARGIN)
#         self.pack_start(self.grid, False, False, 0)

#         self.id_label = Gtk.Label(label="LED:")
#         self.id_spinbox = Gtk.SpinButton()
#         self.id_spinbox.set_range(0, 63)
#         self.id_spinbox.set_increments(1, 10)
#         self.id_spinbox.set_value(0)

#         self.color_label = Gtk.Label(label="Color:")
#         self.color_picker_button = Gtk.Button(label="Pick a Color")
#         self.color_picker_button.connect("clicked", self.open_color_picker)

#         self.apply_button = Gtk.Button(label="Apply")
#         self.apply_button.connect("clicked", self.set_led_grid)

#         self.grid.attach(self.create_aligned_label(self.id_label), 0, 0, 2, 1)
#         self.grid.attach(self.id_spinbox, 0, 1, 2, 1)
#         self.grid.attach(self.create_aligned_label(self.color_label), 0, 2, 2, 1)
#         self.grid.attach(self.color_picker_button, 0, 3, 2, 1)
#         self.pack_end(self.apply_button, False, False, 0)

#     def create_aligned_label(self, label):
#         """
#         Creates a label with left alignment.
#         """
#         hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
#         hbox.pack_start(label, False, False, 0)
#         return hbox

#     def open_color_picker(self, widget):
#         """
#         Opens a color picker dialog.
#         """
#         color_dialog = Gtk.ColorChooserDialog(title="Select a color", parent=window)
#         color_dialog.set_transient_for(window)

#         color_dialog.add_buttons(
#             Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
#         )

#         current_color = (
#             self.color_picker_button.get_style_context().get_background_color(
#                 Gtk.StateFlags.NORMAL
#             )
#         )

#         color_dialog.set_rgba(current_color)
#         response = color_dialog.run()

#         if response == Gtk.ResponseType.OK:
#             self.led_color = color_dialog.get_rgba()

#             self.color_picker_button.get_style_context().add_class("custom-button")
#             self.color_picker_button.get_style_context().save()
#             self.color_picker_button.override_background_color(
#                 Gtk.StateFlags.NORMAL, self.led_color
#             )

#         color_dialog.destroy()

#     def set_led_grid(self, widget):
#         """
#         Sets the color of the LED.
#         """
#         led_id = int(self.id_spinbox.get_value())
#         led_color = "{:02x}{:02x}{:02x}".format(
#             int(self.led_color.red * 255),
#             int(self.led_color.green * 255),
#             int(self.led_color.blue * 255),
#         )

#         api_endpoint = (
#             "http://"
#             + HOST_NAME_PREF
#             + ":"
#             + str(PORT_NUMBER_PREF)
#             + "/leds/set/"
#             + str(led_id)
#             + "?hex="
#             + str(led_color)
#         )

#         requests.get(api_endpoint)


# class SettingsView(Gtk.Box):
#     """
#     Represents the view for the settings.
#     """

#     def __init__(self):
#         """
#         Initializes the SettingsView object.
#         """
#         Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

#         self.set_margin_top(MARGIN * 10)
#         self.set_margin_end(MARGIN * 20)
#         self.set_margin_bottom(MARGIN * 10)
#         self.set_margin_start(MARGIN * 20)

#         self.grid = Gtk.Grid()
#         self.grid.set_column_homogeneous(True)
#         self.grid.set_row_spacing(MARGIN)
#         self.pack_start(self.grid, False, False, 0)

#         self.host_name_label = Gtk.Label(label="Host:")
#         self.port_number_label = Gtk.Label(label="Port:")
#         self.refresh_time_label = Gtk.Label(label="Sampling Time:")

#         self.host_entry = Gtk.Entry()
#         self.port_entry = Gtk.Entry()
#         self.refresh_time_entry = Gtk.Entry()

#         self.save_button = Gtk.Button(label="Save")
#         self.save_button.connect("clicked", self.save_settings)

#         self.grid.attach(self.create_aligned_label(self.host_name_label), 0, 0, 2, 1)
#         self.grid.attach(self.host_entry, 0, 1, 2, 1)
#         self.grid.attach(self.create_aligned_label(self.port_number_label), 0, 2, 2, 1)
#         self.grid.attach(self.port_entry, 0, 3, 2, 1)
#         self.grid.attach(self.create_aligned_label(self.refresh_time_label), 0, 4, 2, 1)
#         self.grid.attach(self.refresh_time_entry, 0, 5, 2, 1)
#         self.pack_end(self.save_button, False, False, 0)

#         # self.restore_settings()

#     def create_aligned_label(self, label):
#         """
#         Creates a label with left alignment.
#         """
#         hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
#         hbox.pack_start(label, False, False, 0)
#         return hbox

#     def save_settings(self, widget):
#         """
#         Saves the settings.
#         """
#         global HOST_NAME_PREF, PORT_NUMBER_PREF, REFRESH_TIME_PREF
#         HOST_NAME_PREF = self.host_entry.get_text()
#         PORT_NUMBER_PREF = self.port_entry.get_text()
#         REFRESH_TIME_PREF = self.refresh_time_entry.get_text()

#     def restore_settings(self):
#         """
#         Restores the settings.
#         """
#         self.host_entry.set_text(HOST_NAME_PREF)
#         self.port_entry.set_text(str(PORT_NUMBER_PREF))
#         self.refresh_time_entry.set_text(str(REFRESH_TIME_PREF))


# class SixthSense(Gtk.Window):
#     """
#     Represents the main window.
#     """

#     def __init__(self):
#         """
#         Initializes the main window.
#         """
#         Gtk.Window.__init__(self, title="SixthSense")
#         self.set_default_size(800, 600)
#         self.connect("destroy", Gtk.main_quit)

#         # View stack
#         self.stack = Gtk.Stack()
#         self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
#         self.stack.set_transition_duration(100)

#         self.sensors_view = SensorsView()
#         self.plots_view = PlotsView()
#         # self.control_view = ControlView()
#         # self.settings_view = SettingsView()

#         self.stack.add_named(self.sensors_view, "Sensors")
#         self.stack.add_named(self.plots_view, "Plots")
#         # self.stack.add_named(self.control_view, "Control")
#         # self.stack.add_named(self.settings_view, "Settings")

#         # Navigation bar
#         self.sensors_view_button = Gtk.Button(label="Sensors")
#         self.sensors_view_button.connect("clicked", self.switch_view, "Sensors")
#         self.plots_view_button = Gtk.Button(label="Plots")
#         self.plots_view_button.connect("clicked", self.switch_view, "Plots")
#         # self.control_view_button = Gtk.Button(label="Control")
#         # self.control_view_button.connect("clicked", self.switch_view, "Control")
#         # self.settings_view_button = Gtk.Button(label="Settings")
#         # self.settings_view_button.connect("clicked", self.switch_view, "Settings")

#         self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
#         self.add(self.box)
#         self.navigation_bar = Gtk.Box(
#             orientation=Gtk.Orientation.HORIZONTAL, spacing=MARGIN
#         )

#         self.navigation_bar.set_margin_top(MARGIN)
#         self.navigation_bar.set_margin_end(MARGIN)
#         self.navigation_bar.set_margin_bottom(MARGIN)
#         self.navigation_bar.set_margin_start(MARGIN)

#         self.box.pack_start(self.navigation_bar, False, False, 0)

#         self.navigation_bar.pack_start(self.sensors_view_button, True, True, 0)
#         self.navigation_bar.pack_start(self.plots_view_button, True, True, 0)
#         # self.navigation_bar.pack_start(self.control_view_button, True, True, 0)
#         # self.navigation_bar.pack_start(self.settings_view_button, True, True, 0)

#         self.box.pack_start(self.stack, True, True, 0)

#     def switch_view(self, widget, view_name):
#         """
#         Switches the view.
#         """
#         self.stack.set_visible_child_name(view_name)


# """
# The main function.
# """
# window = SixthSense()

# """
# Shows the window.
# """
# window.show_all()

# """
# Starts the Gtk main loop.
# """
# Gtk.main()