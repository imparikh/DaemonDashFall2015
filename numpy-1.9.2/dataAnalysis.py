'''
Created on Sep 26, 2015

@author: Jack
'''

import statistics

outliers = []
trimmedData = []
trimmedTimes = []
olCheck = 0

def dataSort(purchases, times):
    for i in range(len(times) - 1, 0, -1):
        for j in range(i):
            if times[j] > times[j + 1]:
                tempt = times[j]
                tempp = purchases[j]
                times[j] = times[j + 1]
                purchases[j] = purchases[j + 1]
                times[j + 1] = tempt
                purchases[j + 1] = tempp
    return purchases, times

def analyzeData(purchases, times):
    std = statistics.stdev(purchases, statistics.mean(purchases))
    data = []
    
    for i in range(len(purchases)):
        if purchases[i] > (statistics.mean(purchases) + std * 1.5):
            outliers.append(purchases[i])
        else:
            trimmedData.append(purchases[i])
            trimmedTimes.append(times[i])
            
    for i in range(max(trimmedTimes)):
        data.append(0)
        
    flag = 0
    
    for w in trimmedTimes:
        data[w - 1] += trimmedData[flag]
        flag = flag + 1
        
    for w in range(max(trimmedTimes) - 1):
       
        data[w + 1] += data[w]

    for i in outliers:
        for w in range(len(data)):
            data[w] += i

    
    return data
                



