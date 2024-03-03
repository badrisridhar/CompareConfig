# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:48:39 2024

@author: bathi
"""

class DataDict:
    source={}
    target={}
    def addRecord(object, dataSet, env):
        if(env == "Source"):
            if (object in DataDict.source.keys()):
                for data in dataSet:
                    DataDict.source[object].append(data)                    
                              
            else:
                Dataarr = []
                for data in dataSet:
                    Dataarr.append(data)
                DataDict.source[object]=Dataarr
        if(env == "Target"):
            if (object in DataDict.target.keys()):
                for data in dataSet:
                    DataDict.target[object].append(data)                    
                              
            else:
                Dataarr = []
                for data in dataSet:    
                    Dataarr.append(data)
                DataDict.target[object]=Dataarr
                
    def getDataarr(object, env):
        if(env == "Source"):
            return DataDict.source[object]
            
        if(env == "Target"):
            return DataDict.target[object]
        
    def getDataAll(env):
        if(env == "Source"):
            return DataDict.source
            
        if(env == "Target"):
            return DataDict.target
    
    def clearData():
        DataDict.source.clear()
        DataDict.target.clear()
        
                                            
        
        