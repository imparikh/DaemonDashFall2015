'''
Created on Sep 26, 2015

@author: Jack
'''
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api


import dataAnalysis
import numpy as np
from flask import Flask, render_template, request
from aParser import aParser
from send_email import email
import Dictionary
app = Flask(__name__)


x=aParser()
tempString = '56070b7de9a2530d0016bda3'
x.setChild(tempString)
x.getBalance()

times = aParser.dateArray
purchases = aParser.purchaseArray
allow = 500
purchases, times = dataAnalysis.dataSort(purchases, times)
data = dataAnalysis.analyzeData(purchases, times)
allowance = []
xvalue = []
x = []
for i in range(30):
    xvalue.append(i + 1)
    allowance.append(allow)
for i in range(len(data)):
    x.append(i + 1)
x = np.array(x)
y = np.array(data)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
fit = []

b = email(Dictionary.HDTV.name, Dictionary.HDTV.price, Dictionary.HDTV.store, z[0], (z[1]>50))
for i in fit:
    if i > allow:
        b.run()
        

for i in xvalue:
    fit.append(p(i))
print (xvalue)
print (data)
print (z)
@app.route('/')
@app.route('/index')
def index(chartID = 'chart_ID', chart_type = 'line', chart_height = 700):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Total spending', "data": data}, {"name": 'Projected Spending', "data": fit}, {"name": 'Allowance', "data": allowance}, {"name": 'Purchases', "data": purchases}]
    title = {"text": 'October'}
    xAxis = {"categories": xvalue}
    yAxis = {"title": {"text": 'Spending'}}
    return render_template('index.html' , chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

if __name__ == "__main__":
    app.run(debug = True, port=5000, passthrough_errors=True)




    
