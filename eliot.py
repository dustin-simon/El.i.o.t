"""
========================================
El.i.o.t - Electronics Input Output Tool
========================================
"""

import eliot

nameLine = " El.i.o.t - Electronics Input Output Tool ( v" + eliot.__version__+" ) "
separator = ""

for i in range(len(nameLine)):
    separator += "="

print("\n"+separator+"\n"+nameLine+"\n"+separator+"\n")
