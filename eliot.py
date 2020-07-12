"""
========================================
El.i.o.t - Electronics Input Output Tool
========================================
"""
import time

import eliot

def print_title():
    nameLine = " El.i.o.t - Electronics Input Output Tool ( v" + eliot.__version__+" ) "
    separator = len(nameLine)*"="

    print("\n"+separator+"\n"+nameLine+"\n"+separator+"\n")

if __name__ == "__main__":
    print_title()

    # import EliotApp here because import of kivy causes output which should not occur before application title
    from eliot.app import EliotApp
    EliotApp().run()
    