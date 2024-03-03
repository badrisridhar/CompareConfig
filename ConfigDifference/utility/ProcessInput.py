
from utility import Transform as tr
from utility import DataDict as dd

class ProcessInput:
    def processinp(self,jsonObject,objectname, env):
        
        output=[]
        #print (jsonObject)
        jsonlist=jsonObject["member"]
        #print(jsonlist)
        for jsonobj in jsonlist:
            #print(jsonobj)
            transform=tr.Transform(objectname,jsonobj,None,env)
            output.append(transform.transform())
            #print(output)
        dd.DataDict.addRecord(objectname, output, env)

    def processinpchild(self,jsonObject,objectname, env, parent):
        output=[]
        for jsonobj in jsonObject:
            transform=tr.Transform(objectname,jsonobj,parent, env)
            output.append(transform.transform())
        dd.DataDict.addRecord(objectname, output, env)