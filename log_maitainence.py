import os
import shutil
from datetime import datetime
import time
import gzip

dataFolder = os.getcwd() + "/data/"
oldLogFolder = dataFolder + "/oldLOGS/"

def getLength(file):
        with open(file, 'r') as file:
                line_count = sum(1 for line in file)
        return line_count


def compressFile(file):
        outFile = file +".gz"
        with open(file, 'rb') as f_in:
                with gzip.open(outFile, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
        os.remove(file)

def resetFile(file):
        newFilePath = oldLogFolder + datetime.now().strftime("%m_%d_%Y")
        shutil.copy(file, newFilePath)

        compressFile(newFilePath)

        with open(file, 'w') as file:
                pass

'''Function to see if logs are too large. Usage :
import log_maintainence

paths = ["/path/to/log", "/path/to/different/log"]
maintainLogs(paths)
'''
maintainLogs(paths)
def maintainLogs(paths):
        for path in paths:
                size = getLength(path)
                if size > 1000:
                        resetFile(path)
