'''

'''
# This class creates the graphs
# We used Flask to display the graph in HTML


import dataAnalysis
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
import numpy as np
from flask import Flask, render_template, request
from aParser import aParser
from send_email import email
import Dictionary
import random
from numpy import integer
tls.set_credentials_file(username = 'qazwsxcde125', api_key = 'jqwnqq7qkh')
app = Flask(__name__, static_url_path="/static")


x = aParser()
tempString = '56070b7de9a2530d0016bda3'
x.setChild(tempString)
x.getBalance()
x.addBalanceToChildAcc(3000)
for i in Dictionary.BestBuy_Array:
    x.spending(i.name, i.price, int (random.random() * 15))
for i in Dictionary.AmericanEagle_Array:
    x.spending(i.name, i.price, int (random.random() * 15))
for y in Dictionary.WholeFoods_Array:
    for i in Dictionary.WholeFoods_Array:
        x.spending(i.name, i.price, int (random.random() * 15))
for i in Dictionary.Kmart_Array:
    x.spending(i.name, i.price, int (random.random() * 15))
times = x.getDate()
purchases = x.getPurchases()
you = x.getNames()
allow = 3000
purchases, times, you = dataAnalysis.dataSort(purchases, times, you)
data = dataAnalysis.analyzeData(purchases, times)
allowance = []
xvalue = []
x = []
for i in range(31):
    xvalue.append(i + 1)
    allowance.append(allow)
for i in range(len(data)):
    x.append(i + 1)
x = np.array(x)
y = np.array(data)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
fit = []

for i in xvalue:
    fit.append(p(i))
trace0 = Scatter(
    x=range(len(fit)),
    y=fit,
    mode='lines'
)
trace1 = Scatter(
    x=range(len(data)),
    y=data,
    mode='markers'
)
trace2 = Scatter(
    x=range(len(allowance)),
    y=allowance,
    mode='lines'
)
data2 = Data([trace0, trace1, trace2])
py.image.save_as({'data': data2}, 'testing.png')
#plot_url = py.plot(data, filename='line-scatter')
flag = 0
b = email(Dictionary.HDTV.name, Dictionary.HDTV.price, Dictionary.HDTV.store, z[0], (z[1] > 50))
for i in fit:
    if i > allow and flag == 0:
        b.run()
        flag = 1
fp = open('index.html', 'r')
string = (fp.read())
fp.close()
for i in range(len(you)):
    string +=  "<tr> <td> "+str(you[i])+" </td> <td> "+str(purchases[i])+" </td> <td> "+str(times[i]+1)+" </td>"
string += "</div> </div> <div>  </div> </body> </html>"
string += "</div> </div> <ul>  <li>Average spending per day: $"+ str(int(np.average(purchases))) +"</li> <li> Adjusted average spending per day: $"+str(int(p[1]))+"</li> <li> Highest expenditure: $"+str(int(max(purchases)))+" on a "+str((you[purchases.index(max(purchases))]))+"</li> <li> Projected spending for the month: $"+str(int(max(fit)))+"</li> </body> </html>"
fp = open('templates/index.html', 'w+')
string = (fp.write(string))
fp.close()

@app.route('/')

@app.route('/index')
def index(chartID='chart_ID', chart_type='line', chart_height=500):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    series = [{"name": 'Total spending', "data": data}, {"name": 'Projected Spending', "data": fit}, {"name": 'Allowance', "data": allowance}]
    title = {"text": 'October'}
    xAxis = {"categories": xvalue}
    yAxis = {"title": {"text": 'Spending'}}
    return render_template('index.html' , chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
    
if __name__ == "__main__":
    app.run(debug=True, port=80, passthrough_errors=True)




    
