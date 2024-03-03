# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:07:36 2024

@author: bathi
"""

from rules import rules as rm



class GetFromParent(rm.Rules):
    
    def execute(self, jsonObj, attr, parent, env):
        jsonObj[attr] = parent[attr]
        return jsonObj