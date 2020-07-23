"""
========================================
El.i.o.t - Electronics Input Output Tool
========================================
"""
import os

from kivy.app import App

from eliot.ui.popup.shutdown import Shutdown as ShutdownPopup
from eliot.ui.menu.module_button import ModuleButton

class EliotApp(App):
    
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

        
