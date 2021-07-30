
import csv
import plotly.express as px
import numpy as np

def plotFigure(data) :
    with open(data) as f : 
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours", color = "week")
        fig.show()

def getDataSource(data) :
    coffee = []
    sleep = []
    with open(data) as f :
        df = csv.DictReader(f)

        for i in df :
            coffee.append(float(i["Coffee in ml"]))
            sleep.append(float(i["sleep in hours"]))

    return {"x" : coffee, "y" : sleep}

def findCorrelation(dataSource) :
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation[0,1])

def setup() :
    data = "data2.csv"
    dataSource = getDataSource(data)
    findCorrelation(dataSource)
    plotFigure(data)

setup()