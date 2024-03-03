# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:33:50 2024

@author: bathi
"""

from utility import readXml as rx
from utility import DataDict as dd
 
from deepdiff import DeepDiff

from openpyxl import Workbook
import json

class Compare:
   def initCompare(self, sourceDF, targetDF):
       for key in sourceDF.keys():
           ReadXml = rx.ReadXml(key)
           rule = ReadXml.getRule()
           keyfld = rule[3]
               
           #print (key)
           insource = []
           intarget = []
           notmatching = []
           sdf = sourceDF[key]
           tdf = targetDF[key]
           #print ("Source: ",sdf)
           #print ("Target: ",tdf)
           for index, row in sdf.iterrows():
               iter = 0
               cond = None
               #print (keyfld)
               for keyfld1 in keyfld.keys():
                   #print (keyfld1)
                   #print (keyfld)
                   #print(type(tdf[keyfld1]==row[keyfld1]))
                   if(iter == 0):
                       cond = tdf[keyfld1]==row[keyfld1]
                   else:
                       cond = cond & tdf[keyfld1]==row[keyfld1]
                   iter = iter + 1
               t_df = tdf.loc[cond]
               iter = 0
               for keyfld1 in keyfld.keys():
                   if(iter == 0):
                       cond = sdf[keyfld1]==row[keyfld1]
                   else:
                       cond = cond & sdf[keyfld1]==row[keyfld1]
                   iter = iter + 1
               s_df = sdf.loc[cond]
               #print("source: ",s_df)
               s_dict = s_df.to_dict('records')
               t_dict = t_df.to_dict('records')
               
               
               #print('s_dict:',s_dict)
               #print('t_dict:',t_dict)
               if not not t_dict: 
                   diff = DeepDiff(t_dict[0],s_dict[0], ignore_nan_inequality=True)
                   #print(diff)
                   if('values_changed' in diff.keys()):
                       difference = json.dumps(diff['values_changed'])
                   #print("deepdiff: ",diff)
                         #print(s_dict)
                       keyfield = ""
                       for keyfld1 in keyfld.keys():
                           if(keyfield == ""):
                               keyfield = keyfield + s_dict[0][keyfld1]
                           else:
                               keyfield = keyfield +"~"+ s_dict[0][keyfld1]
                           
                       notmatching.append([keyfield,difference])
           keyfldarr = []        
           for keyfld1 in keyfld.keys():
               keyfldarr.append(keyfld1)
           #print (keyfldarr)
           df_all = sdf.merge(tdf.drop_duplicates(), on=keyfldarr,how='left', indicator=True)
           #print(df_all.values.tolist())
           df1_only = df_all[df_all['_merge'] == 'left_only']
           df1_only = df1_only.drop('_merge', axis=1)
           #print(df1_only.values.tolist())
           for index, row in df1_only.iterrows():
               keyfield = ""
               for keyfld1 in keyfld.keys():
                   if(keyfield == ""):
                       keyfield = keyfield + row[keyfld1]
                   else:
                       keyfield = keyfield +"~" + row[keyfld1]
               insource.append(keyfield)
           #print(df1_only)
           #insource.append(df1_only['conditionnum'])
           
           df_all = tdf.merge(sdf.drop_duplicates(), on=keyfldarr,how='left', indicator=True)
           #print(df_all.values.tolist())
           df1_only = df_all[df_all['_merge'] == 'left_only']
           df1_only = df1_only.drop('_merge', axis=1)
           df1_only.values.tolist()
           #print(df1_only)
           for index, row in df1_only.iterrows():
               keyfield = ""
               for keyfld1 in keyfld.keys():
                   if(keyfield == ""):
                       keyfield = keyfield + row[keyfld1]
                   else:
                       keyfield = keyfield +"~" + row[keyfld1]
               insource.append(keyfield)
           
           #intarget.append(df1_only['conditionnum'])
           #print("Different: ")
           #print(notmatching)
           #print("In Source: ")
           #print(insource)
           #print("In Target: ")
           #print(intarget)
           
           output = []
           keyfieldstr = ""
           for keyfld1 in keyfld.keys():
               if(keyfieldstr == ""):
                   keyfieldstr = keyfieldstr + keyfld1
               else:
                   keyfieldstr = keyfieldstr + "~" + keyfld1
           
           output.append([keyfieldstr,"Reason","Difference"])
           
           for val in notmatching:
               output.append([val[0],"Different between Source and Target",val[1]])
               
           for val in insource:
               output.append([val,"Missing in Target",""])
           
           for val in intarget:
               output.append([val,"Missing in Target",""])
           
           #print (output)
           
           
           wb = Workbook() # creates a workbook object.
           ws = wb.active # creates a worksheet object.
           for row in output:
               ws.append(row)
               
           wb.save('./output/'+key+'.xlsx')

           
           #df = pd.DataFrame(output)
           ##writer = pd.ExcelWriter('./input/Compare.xlsx', engine='xlsxwriter')
           #df.to_excel(writer, sheet_name='condition', index=False)
           #writer.save()
           
          
               
           
       