# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:13:37 2024

@author: bathi
"""

from rules import rules as rm
from utility import ProcessInput as pi


class ChildObj(rm.Rules):
    
    def execute(self, jsonObj, attr, parent, env):
        childobj = jsonObj[attr]
        processInp = pi.ProcessInput()
        processInp.processinpchild(childobj,attr, env, jsonObj)
        del jsonObj[attr]    
        return jsonObj
        