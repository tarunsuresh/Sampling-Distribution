import statistics
import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"]


def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)

    mean=statistics.mean(dataSet)
    
    return mean

def sampling():
    meanList=[]
    for i in range(0,1000):
        setOfMean=randomSetOfMean(100)
        meanList.append(setOfMean)
    
    fig=ff.create_distplot([meanList],["reading_time"])
    fig.show()

    samplingMean=statistics.mean(meanList)
    samplingStdev=statistics.stdev(meanList)

    print("sampling mean is :"+str(samplingMean))
    print("sampling Stdev is :"+str(samplingStdev)) 

sampling()

