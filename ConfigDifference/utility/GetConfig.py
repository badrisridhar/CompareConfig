# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:15:45 2024

@author: bathi
"""

import requests

class GetConfig:
    def __init__(self, objdetails, readExcel, env):
        #print (objdetails)
        self.objectname = objdetails[1]
        self.whereclause = objdetails[2]
        self.env = env
        self.readExcel = readExcel
        
    def getJson(self):
        instance = self.readExcel.getInstData(self.env)
        header = {"apikey": instance["apikey"]}
        objstr = self.readExcel.getMapping(self.objectname)
        baseurl=instance["url"]
        url=baseurl+"/api/os/"+objstr+"?lean=1"
        params={"oslc.where":self.whereclause,"oslc.select":"*"}
        response=requests.get(url,verify=False,headers=header,params=params)
        jsonresp=response.json()
        #print (jsonresp)
        return jsonresp