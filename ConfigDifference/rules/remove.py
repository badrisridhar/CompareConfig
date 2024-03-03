# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:11:08 2024

@author: bathi
"""

from rules import rules as rm

class Remove(rm.Rules):
    
    def execute(self, jsonObj, attr, parent, env):
        del jsonObj[attr]
        return jsonObj
    