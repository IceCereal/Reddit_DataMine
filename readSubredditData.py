"""
Module to read and return a readable data unit for each file in SubredditData/

Example Data:
$['2018-11-14 21:35:18.257332', [8, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""
from ast import literal_eval

class Reader:
    def __init__(self, fileName : str):
        self.fileName = fileName
        
