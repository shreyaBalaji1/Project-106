import csv
import plotly.express as px
import numpy as np

def plotFigure(data) :
    with open(data) as f : 
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Marks In Percentage", y = "Days Present")
        fig.show()

def getDataSource(data) :
    marks = []
    present = []
    with open(data) as f :
        df = csv.DictReader(f)

        for i in df :
            marks.append(float(i["Marks In Percentage"]))
            present.append(float(i["Days Present"]))

    return {"x" : marks, "y" : present}

def findCorrelation(dataSource) :
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation[0,1])

def setup() :
    data = "data1.csv"
    dataSource = getDataSource(data)
    findCorrelation(dataSource)
    plotFigure(data)

setup()