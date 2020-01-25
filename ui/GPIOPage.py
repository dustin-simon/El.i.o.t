from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Builder.load_file("ui/gpio.kv")

class GPIOPage(TabbedPanelItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initGPIOList(self):

        self.gpio_list.bind(minimum_height=self.gpio_list.setter('height'))

        for i in range(100):

            label = Button(text="GPIO [ " + str(i) + " ]")
            label.size_hint_y = None
            label.height = 80

            self.gpio_list.add_widget(label)

