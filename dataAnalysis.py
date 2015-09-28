'''
Created on Sep 26, 2015

@author: Jack
'''

import statistics

outliers = []
trimmedData = []
trimmedTimes = []
olCheck = 0
# sort data by purchases
def dataSort(purchases, times, names):
    for i in range(len(times) - 1, 0, -1):
        for j in range(i):
            if times[j] > times[j + 1]:
                tempt = times[j]
                tempp = purchases[j]
                tempn = names[j]
                times[j] = times[j + 1]
                purchases[j] = purchases[j + 1]
                names[j] = names[j + 1]
                times[j + 1] = tempt
                purchases[j + 1] = tempp
                names[j + 1] = tempn
    return purchases, times, names


def analyzeData(purchases, times):
    std = statistics.stdev(purchases, statistics.mean(purchases))
    analyzedData = []
    
    for i in range(len(purchases)):
        if purchases[i] > (statistics.mean(purchases) + std * 1):
            outliers.append(purchases[i])
        else:
            trimmedData.append(purchases[i])
            trimmedTimes.append(times[i])
   
    for i in range(max(trimmedTimes)):
        analyzedData.append(0)
        
    flag = 0
    
    for w in trimmedTimes:
        analyzedData[w - 1] += trimmedData[flag]
        flag = flag + 1
        
    for w in range(max(trimmedTimes) - 1):
       
        analyzedData[w + 1] += analyzedData[w]

    for i in outliers:
        for w in range(len(analyzedData)):
            analyzedData[w] += i

    
    return analyzedData
                



