"""
========================================
El.i.o.t - Electronics Input Output Tool
========================================
"""
import os

from kivy.app import App

from eliot.ui.popup.shutdown import Shutdown as ShutdownPopup

class EliotApp(App):

    MAIN_COLOR = 0,0,0.5,1
    
    def on_power_btn_pressed(self):
        ShutdownPopup().open()

    def shutdown(self):
        os.system("sudo shutdown now")