#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimlator -> CeausiElement

Author: Remi GASCOU
Last edited: November 2018
"""

class CeausiElement(object):
    """docstring for CeausiElement."""
    def __init__(self):
        super(CeausiElement, self).__init__()
        self.name           = ""
        self.alias          = ""
        self.d_valueOn      = 1
        self.d_valueOff     = 0
        self.d_width        = 0
        self.d_height       = 0
        self.elementgrid    = []
        self.centercoords   = [0,0]
        
    def loadFromFile(self, path):
        if path.endswith(".caselem"):
            f = open(path,'r')
            jsondata = ''.join([e for e in f.readlines() if type(e) == str])
            f.close()
            d_in = json.loads(jsondata)
            self.d_valueOff   = d_in['element']['data']['valueOff']
            self.d_valueOn    = d_in['element']['data']['valueOn']
            self.elementgrid  = d_in['element']['grid'].copy()
            self.d_width      = len(self.elementgrid)
            self.d_height     = len(self.elementgrid[0])
            self.centercoords = [self.d_width//2,self.d_height//2]
            return 0
        else:
            return -1


    def saveToFile(self, path):
        if not path.endswith(".casgrid"):
            path += ".casgrid"
        jsondata = """{\n\t"grid_data": {\n\t\t"name": "Example Grid",\n\t\t"valueOff": """ + str(self.valueOff) + """,\n\t\t"valueOn": """ + str(self.valueOn) + """,\n\t\t"grid":""" + str(self.grid) + """\n\t}\n}"""
        f = open(path,'w+')
        f.write(jsondata)
        f.close()
