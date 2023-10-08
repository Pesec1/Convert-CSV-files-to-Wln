import pandas as pd
import time
import datetime
from os import listdir


INPUTPATH = "D:\programming\FromBBEscortToWln\inputFolder\\"
OUTPUTPATH = "D:\programming\FromBBEscortToWln\outputFolder\\"



def getInputFiles(pathToCsv):
    return listdir(pathToCsv)


def getOutputFiles(outputPath, outputData, Csv):
    outputDf = pd.DataFrame(outputData)
    outputDf.to_csv(
        outputPath + Csv[0:-4] + ".wln",
        index=False,
        header=False,
    )

def convertDateToTimestamp(date):
    element = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    tuple = element.timetuple()
    
    return time.mktime(tuple)

def convertCsvToWln(listOfCsv, inputPath, outputPath):
    outputData = []
    for i in range(len(listOfCsv)):
        df = pd.read_csv(inputPath + listOfCsv[i])

        for index, row in df.iterrows():
            result = (
                "REG;"
                + str(int(convertDateToTimestamp(row[0])))
                + ";"
                + "0.0;0.0;0;0;"
                + "bt_2:"
                + str(row[1])
                + ";;"
            )
            outputData.append(result)
        getOutputFiles(outputPath, outputData, listOfCsv[i])
        outputData = []
        


listFile = getInputFiles(INPUTPATH)
convertCsvToWln(listFile, INPUTPATH, OUTPUTPATH)
