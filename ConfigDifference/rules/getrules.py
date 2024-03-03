# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:10:45 2024

@author: bathi
"""

from rules import remove as rm
from rules import childobj as co
from rules import getFromParent as gfp

class GetRules:
    
    def getObject(self, rlname):
        if(rlname == 'remove'):
            return rm.Remove()
        if(rlname == 'childobj'):
            return co.ChildObj()
        if(rlname == 'getFromParent'):
            return gfp.GetFromParent()
        
        
        