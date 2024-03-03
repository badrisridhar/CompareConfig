# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:16:34 2024

@author: bathi
"""

import xlwings as xw

class ReadExcel:
    mapping = {}
    instData = {}
    
    def __init__(self, filename):
        self.wb = xw.Book(filename)
        self.setMapping()
        self.setInstData()
        
    def setInstData(self):
        ws = self.wb.sheets['Setup']
        
        source = {"url": ws.range('B3').value,"apikey": ws.range('B4').value}
        target = {"url": ws.range('B6').value,"apikey": ws.range('B7').value}
        ReadExcel.instData["Source"] = source
        ReadExcel.instData["Target"] = target
        
    def getInstData(self, environment):
        return ReadExcel.instData[environment]
    
    def getInputData(self):
        ws = self.wb.sheets["Input"]
        data = ws.range('A3').expand().value
        rownum = 0
        data1 = []
        for row in data:
            if(rownum != 0):
                data1.append(row)
            rownum = rownum + 1    
        
        return data1
    
    def setMapping(self):
        ws = self.wb.sheets['Mapping']
        data = ws.range('A3').expand().value
        rownum = 0
        for row in data:
            if(rownum != 0):
                ReadExcel.mapping[row[0]] = row[1]
            rownum = rownum + 1    
        
            
    def getMapping(self, object):
        return ReadExcel.mapping[object]
    
    def updateCell(self,cell,value):
        ws = self.wb.sheets["Input"]
        ws.range(cell).value = value
        
        
    
    