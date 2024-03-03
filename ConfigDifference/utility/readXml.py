# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:16:44 2024

@author: bathi
"""

import xml.etree.ElementTree as ET

class ReadXml:
    rules = {}
    
    def __init__(self, objectname):
        self.filename="./configuration/"+objectname+".xml"
        self.objectname = objectname
        
    def getRule(self):
        if self.objectname in ReadXml.rules.keys():
            return ReadXml.rules[self.objectname]
        else:
            tree = ET.parse(self.filename)
            root = tree.getroot()
            name = root.attrib["name"]
            attr = []
            attrrule = {}
            attrkey = {}
            for item in root.findall('./attribute'):
                attr.append(item.attrib['name'])
                if 'rule' in item.keys():
                    attrrule[item.attrib['name']] = item.attrib['rule']
                if 'key' in item.keys():
                    attrkey[item.attrib['name']] = item.attrib['key']
                    
            ReadXml.rules[self.objectname] = [name, attr, attrrule,attrkey]
            return [name, attr, attrrule,attrkey]
        
        
            