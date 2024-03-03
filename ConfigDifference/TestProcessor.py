# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:02:50 2024

@author: bathi
"""
import json
from utility import ProcessInput as pi


f = open('D:/Badri/accelarator/ConfigMigrator/json.txt')
data = json.load(f)
processInp = pi.ProcessInput()
print (data)
out = processInp.processinp(data,"domain")
print (out)

