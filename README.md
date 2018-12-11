# Reddit_DataMine
The Data Mining Program for the <a href="https://github.com/IceCereal/Bot_REGOD-New">Bot_REGOD-new</a> which collected <a href="https://github.com/IceCereal/Bot_REGOD-New/tree/master/Modules/SubredditData">Reddit Data</a> for one day. The program tries to look for patterns in the collected data.

Modules:<br/><br/>
`readSubredditData.py` - Data Preprocessing
```python
from readSubredditData import Reader

subreddit = Reader('todayilearned')
(X, y) = subreddit.getData(type)
```
`type` (`str`): <br/>
`'high'`  :   returns the highest score in the list (<b>DEFAULT</b>)<br/>
`'mean'`  :   returns the mean of the values in the list<br/>
`'sigma'` :   returns the sum of all the values of the list<br/>
