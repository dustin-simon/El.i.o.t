"""
========================================
El.i.o.t - Electronics Input Output Tool
========================================
"""
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

class Screensaver():

    def __init__(self, screen_manager, time=30):

        self.screen_manager = screen_manager
        self.time = time

        self.__create_screen()
        self.screen_manager.add_widget(self.screen)

        self.current_screen = None

        self.reset_timer()

    def reset_timer(self, *args):
        Clock.unschedule(self.show_screensaver)
        Clock.schedule_once(self.show_screensaver, self.time)

    def show_screensaver(self, delta_time):
        self.current_screen = self.screen_manager.get_screen(
            self.screen_manager.current
        )

        self.screen_manager.switch_to(self.screen)

    def hide_screensaver(self, *args):
        if self.current_screen is not None:
            self.screen_manager.switch_to(self.current_screen)

    def __create_screen(self):
        screen = Screen(name="screensaver")

        grid = GridLayout(cols=1)
        grid.add_widget(Image(source="resources/images/screensaver.png"))
        screen.add_widget(grid)

        screen.bind(on_touch_down=self.hide_screensaver)

        self.screen = screen

