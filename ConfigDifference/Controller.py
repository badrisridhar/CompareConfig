# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:53:46 2024

@author: bathi
"""

from utility import ReadExcel as re
from utility import GetConfig as gc
from utility import ProcessInput as pi
from utility import DataDict as dd
from utility import Compare as comp
import pandas as pd
import datetime

import warnings

ts = datetime.datetime.now()
print("Start Time: ", ts)

readExcel = re.ReadExcel(filename = './input/Input.xlsx')
inputData = readExcel.getInputData()
#print(inputData)
rownum = 4
for input1 in inputData:
    success = 0
    error = 0
    errormsg = ""
    payload = ""
    
    print("Working on object: "+input1[1])
    print("Reading config from Source")
    getConfig = gc.GetConfig(input1, readExcel, "Source")
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        data = getConfig.getJson()
    #print(data)
    processInp = pi.ProcessInput()
    processInp.processinp(data,input1[1],"Source")
    
    #print(dd.DataDict.getDataAll("Source"))
    
    
    #print("Data fetched from source for "+input1[1]+" with where clause: "+input1[2])
    #print(dd.DataDict.getDataAll("Source"))
    print("Reading config from Target")
    getConfig = gc.GetConfig(input1, readExcel, "Target")
    with warnings.catch_warnings():
        
        warnings.simplefilter("ignore")
        data = getConfig.getJson()
    #print(data)
    processInp = pi.ProcessInput()
    processInp.processinp(data,input1[1],"Target")    
    
    #print (json.dumps(out))
    #print("Data fetched from Target for "+input1[1]+" with where clause: "+input1[2])
    #print(dd.DataDict.getDataAll("Target"))
    sourceDF = {}
    targetDF = {}
    sourceDD = dd.DataDict.getDataAll("Source")
    #print(sourceDD)
    for key in sourceDD.keys():
        #print (sourceDD[key])
        sourceDF[key] = pd.DataFrame(sourceDD[key])
    
    targetDD = dd.DataDict.getDataAll("Target")
    for key in targetDD.keys():
        targetDF[key] = pd.DataFrame(targetDD[key])
        
    #print("Source: ")
    #for key in sourceDF.keys():

        #print(sourceDF[key])

    #print("target: ")    
    
    #for key in targetDF.keys():
        #print(targetDF[key])
    
    #print("Target: ")
    #dd.DataDict.getDataAll("Target"))
    
    print("Starting Comparison")
    
    comp.Compare().initCompare(sourceDF, targetDF)
    
    
    dd.DataDict.clearData()
    
    print("Comparison Completed")
    
te = datetime.datetime.now()
print("End Time: ", te)
    
    
    #print(json.dumps(out[0]))
   
          