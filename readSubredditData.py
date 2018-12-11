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

    def _HighScore(self, data):
        return max(data)

    def _Mean(self, data):
        return (sum(data)/len(data))

    def _Sigma(self, data):
        return sum(data)

    def getData(self, type = None):
        """
        type:
            'high'  :   returns the highest score in the list (DEFAULT)
            'mean'  :   returns the mean of the values in the list
            'sigma' :   returns the sum of all the values of the list

        Module returns a tuple:
            ([time_1, time_2, ..., time_n], [num_1, num_2, ..., num_n])
                time_i : float
                    [0.00, 0.25, 0.50, ..., 23.75]
                num_i : int
                    [int, int, int, ..., int]
        """

        if (type == None):
            type = 'high'

        if (type not in ['high', 'mean', 'sigma']):
            return -1

        X = []
        y = []

        def typeSelect(data):
            if type == 'high':
                return self._HighScore(data)
            if type == 'mean':
                return self._Mean(data)
            if type == 'sigma':
                return self._Sigma(data)

        rawData = self._read()

        count = 0.00

        X.append(count)
        y.append(typeSelect(rawData[0][1]))
        count += 1

        for i in range(1, len(rawData)):
            timeLower = datetime.strptime(rawData[i-1][0], '%Y-%m-%d %H:%M:%S.%f')
            timeHigher = datetime.strptime(rawData[i][0], '%Y-%m-%d %H:%M:%S.%f')

            timeDiffMins = int( (timeHigher - timeLower).total_seconds() / 60 )

            if (timeDiffMins >= 16):
                missingDataNumber = (timeDiffMins / 15) + 1

                dataLower = rawData[i-1][1]
                dataHigher = rawData[i][1]

                dataMissing = typeSelect(dataLower) + typeSelect(dataHigher)
                dataMissing = dataMissing/2

                for i in range(1, timeDiffMins + 1):
                    X.append(count * 0.25)
                    y.append(dataMissing)
                    count += 1

            else:
                X.append(count * 0.25)
                count += 1

                y.append(typeSelect(rawData[i][1]))

        return (X, y)
