# -*- coding: utf-8 -*-

import os, sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib import *

class TestUI(object):
    """docstring for TestUI."""
    def __init__(self, tc):
        super(TestUI, self).__init__()
        self.tc = tc

    def test(self):
        print("\x1b[1m" + " Testing UI ".center(80, "-") + "\x1b[0m")
        if self.tc.xdisplay :
            self.tc.test("Ceausi main UI", self._test_AppUI)
            self.tc.test("AboutWindow", self._test_AboutWindow)
            self.tc.test("AddRuleWindow", self._test_AddRuleWindow)
            self.tc.test("DebugWindow", self._test_DebugWindow)
            self.tc.test("EditRuleWindow", self._test_EditRuleWindow)
            self.tc.test("ErrorWindow", self._test_ErrorWindow)
            self.tc.test("RulesWindow", self._test_RulesWindow)
            self.tc.test("SettingsWindow", self._test_SettingsWindow)



        else :
            self.tc.test("No X display found", self._test_pass)

    def _test_AppUI(self):
        passed = True
        # try :
        #     app = QApplication(sys.argv)
        #     ex = PyChatApp()
        #     ex.close()
        # except Exception:
        #     passed = False
        return passed

    def _test_AboutWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = AboutWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_DebugWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = DebugWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_AddRuleWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = AddRuleWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_EditRuleWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = EditRuleWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_RulesWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = RulesWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_SettingsWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = SettingsWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_ErrorWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = ErrorWindow()
            ex.close()
        except Exception:
            passed = False
        return passed





    def _test_pass(self):
        passed = True
        return passed
