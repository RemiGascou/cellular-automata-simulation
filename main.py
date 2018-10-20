# -*- coding: utf-8 -*-

import os, sys
from lib import *


if __name__ == """__main__""":
    app = QApplication(sys.argv)
    ex = CellularAutomataSimulatorApp(38,20) #76,40
    sys.exit(app.exec_())

# Key_C to clear grid
# Key_Space to toggle running
# Key_R to regen grid
