import os
import sys
from flask_paginate import Pagination

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'alienchang'

def GetFileList( dir, fileList):
    pagination = Pagination
    # newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('utf-8'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #ignore some files
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

