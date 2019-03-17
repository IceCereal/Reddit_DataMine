"""Regression:
1. Linear
2. Polynomial
"""

"""
Y-axis Types:
1. High Score: List[0] (i.e. Highest Popularity Index during the time)
2. Average Score: i = 0:n do { Sigma(List[i]) / n }
"""
### Add sys for Subreddit Reader
import sys
sys.path.insert(0, "../")

### Bring in Subreddit Reader
from ReadSubredditData.SubredditReader import Reader

### Bring in LinReg Module
from sklearn import linear_model as lm

from matplotlib import pyplot as plt
from ast import literal_eval as l_e

with open("../subredditList", 'r') as Fobj:
    rawList = Fobj.read()
    subredditList = l_e(rawList)

for subR in subredditList:
    print ("Process", subR)
    tempSubR = Reader(subR, '../SubredditData/')

    (X, y) = tempSubR.getData(numpyEnabled = True)

    regression = lm.LinearRegression()
    regression.fit(X, y)

    predX = 0
    predX = regression.predict(X)

    plt.scatter(X, y, c='red', s = 1) #Scatter Plot for actual data
    plt.plot(X, predX, c='blue') #Line Plot for predicted data
    plt.savefig("LinRegPlots/"+subR+'.png', dpi=500) #Save figure
    plt.cla() #Clear axes for next plot
