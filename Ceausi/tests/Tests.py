# -*- coding: utf-8 -*-

from tests.testcases import *

class TestController(object):
    """docstring for TestController."""
    def __init__(self, xdisplay):
        super(TestController, self).__init__()
        self.s_test_passed = "\x1b[1m\x1b[92mPASSED\x1b[0m"
        self.s_test_failed = "\x1b[1m\x1b[91mFAILED\x1b[0m"

        self.xdisplay = xdisplay

    def test(self, fname, f):
        maxlen = 65
        s = str("\x1b[1m[\x1b[93mTEST\x1b[0m\x1b[1m]\x1b[0m " + fname[:36]).ljust(maxlen, " ") + "... "
        print(s, end="")
        o = f()
        if o == True: print(self.s_test_passed)
        else : print(self.s_test_failed)


class Tests(object):
    """docstring for Tests."""
    def __init__(self, xdisplaycond):
        super(Tests, self).__init__()
        self.xdisplay = ('1' == xdisplaycond)
        self.tc       = TestController(self.xdisplay)

    def run_test(self):
        # Tests UI
        t = TestUI(self.tc)
        t.test()
