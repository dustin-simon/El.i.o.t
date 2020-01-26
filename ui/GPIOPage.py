from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.lang import Builder
from kivy.uix.button import Button
from interface.GPIO import GPIOInterface

Builder.load_file("ui/gpio.kv")

class GPIOPage(TabbedPanelItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.gpio_interface = GPIOInterface()

    def initGPIOList(self):

        self.gpio_list.bind(minimum_height=self.gpio_list.setter('height'))

        gpios = self.gpio_interface.getGPIOList()

        for gpio in gpios:

            btn = Button(text=gpio["label"])
            btn.size_hint_y = None
            btn.height = 80

            self.gpio_list.add_widget(btn)
