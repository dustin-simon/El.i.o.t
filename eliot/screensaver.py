from kivy.clock import Clock

class Screensaver():

    def __init__(self):
        self.reset_timer()

    def reset_timer(self):
        Clock.unschedule(self.show_screensaver)
        Clock.schedule_once(self.show_screensaver, 30)

    def show_screensaver(self, delta_time):
        print("... showing screensaver")
        # TODO: show screen saver