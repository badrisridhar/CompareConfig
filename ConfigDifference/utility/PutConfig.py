# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:16:15 2024

@author: bathi
"""

import requests

class PutConfig:
    def __init__(self, jsonObj, readExcel, objectname, action):
        self.jsonObj = jsonObj
        self.readExcel = readExcel
        self.objectname = objectname
        self.action = action
        
    def postJaon(self):
        instance = self.readExcel.getInstData("target")
        header = {"apikey": instance["apikey"]}
        header["x-method-override"] = "SYNC"
        if(self.action == "Change"):
            header["patchtype"] = "MERGE"
        header["properties"] = "*"
        
        objstr = self.readExcel.getMapping(self.objectname)
        baseurl = instance["url"]
        url = baseurl+"/api/os/"+objstr+"?lean=1"
        response = requests.post(url, verify=False, headers=header, json=self.jsonObj)
        return response
    
    