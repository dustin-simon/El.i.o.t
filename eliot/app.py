"""
========================================
El.i.o.t - Electronics Input Output Tool
========================================
"""
import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from eliot.ui.popup import Shutdown as ShutdownPopup
from eliot.ui.menu import MainMenu, ModuleButton
from eliot.ui.screensaver import Screensaver

def reset_screensaver_timer(*args):
    EliotApp.screen_saver.reset_timer()

class EliotApp(App):

    screen_saver = None
    screen_manager = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.bind(on_touch_down=reset_screensaver_timer)

    def build(self):
        sm = ScreenManager()
        EliotApp.screen_manager = sm

        screen_main_menu = Screen(name="main_menu")
        screen_main_menu.add_widget(MainMenu())
        sm.add_widget(screen_main_menu)

        EliotApp.screen_saver = Screensaver(sm)

        return sm
    
    def on_power_btn_pressed(self):
        ShutdownPopup().open()

    def shutdown(self):
        os.system("shutdown now")

    def get_modules(self):
       return []

    def create_main_menu_buttons(self, main_menu):
        
        modules = self.get_modules()

        for data in modules:
            button = ModuleButton(data["name"])
    
            main_menu.add_widget(button)

        
