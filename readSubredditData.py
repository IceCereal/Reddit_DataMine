"""
Module to read and return a readable data unit for each file in SubredditData/

Example Data:
$['2018-11-14 21:35:18.257332', [8, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""
from ast import literal_eval

class Reader:
    def __init__(self, fileName : str):
        self.fileName = fileName

    def _read(self):
        #Private Function to read file and return the actual list

        with open("SubredditData/"+self.fileName) as Fobj:
            buffer = Fobj.read()    #File Data

            globalList = [] #Final List

            while (True):
                start = buffer.find('$')
                end = buffer[start+1:].find('$')

                if (end == -1):
                    unit = buffer[start+1:]
                    readyUnit =  literal_eval(unit)
                    globalList.append(readyUnit)
                    break

                unit = buffer[start+1 : end+1]
                readyUnit = literal_eval(unit)
                globalList.append(readyUnit)
                buffer = buffer[end+1:]

        return globalList
