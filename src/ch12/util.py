#-------------------------------------------------------------------------------
# Purpose:
#
# Author:      b9890_000
#
# Created:     02/03/2016
# Copyright:   (c) b9890_000 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import json
import xml.etree.ElementTree as ET

from Automata import View

def parse_xml(path):
    if os.path.getsize(path) == 0:
        root = []
    else:
        xml = ET.parse(path)
        root = xml.getroot()

    return root

def getViewList(root,layer=1):
    returnList = []
    for child in root:
      returnList.append((child,layer))
      returnList.extend(getViewList(child,layer+1))
    return returnList

def viewListTransform(viewList):
    returnList = []
    for index,view in enumerate(viewList):
        # View(layer,index,xml)
        newView = View(view[1],index,view[0])
        returnList.append(newView)
    return returnList

def load_json(path):
    jsonFile = open(path, encoding='utf8')
    data = json.load(jsonFile)
    jsonFile.close()
    return data

def write_json(data,path):
    with open(path, "w", encoding='utf8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

def getRoot():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def getFilebyStepID(stepID,fileType):
        root = getRoot()

        account,app,versionNum,abstractionNum,sessionNum,traceNum,stepNum = stepID
        if fileType == "png":
            file = os.path.join(root,"traces",account,app,str(versionNum),"abstraction"+str(abstractionNum),\
                        "session"+str(sessionNum),"traceSet",str(traceNum),"screenShot"+str(stepNum)+".png")
        elif fileType == "xml":
            file = os.path.join(root,"traces",account,app,str(versionNum),"abstraction"+str(abstractionNum),\
                        "session"+str(sessionNum),"traceSet",str(traceNum),"uidump"+str(stepNum)+".xml")

        elif fileType == "json":
            file = os.path.join(root,"traces",account,app,str(versionNum),"abstraction"+str(abstractionNum),\
                        "session"+str(sessionNum),"traceSet",str(traceNum),"move"+str(stepNum)+".json")
        return file