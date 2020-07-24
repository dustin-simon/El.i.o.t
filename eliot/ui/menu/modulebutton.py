"""
========================================
El.i.o.t - Electronics Input Output Tool
========================================
"""
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file("eliot/ui/menu/modulebutton.kv")

class ModuleButton(ButtonBehavior, BoxLayout):

    def __init__(self, label, **kwargs):

        super(ModuleButton, self).__init__(**kwargs)

        self.name_label.text = "[b]"+label+"[/b]"
        self.module_icon.source = "resources/icons/modules/" + label + ".png"