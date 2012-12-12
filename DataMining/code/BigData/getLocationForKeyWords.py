'''
Created on Dec 12, 2012

@author: gparuthi
'''
from DataMining.code.com.BigData import BigData
from DataMining.code.com.log import logger
from dateutil.parser import parse

keywords = {'barack', 'obama', 'mitt', 'romney', 'president', 'election'}
input_dir = '/Users/gaurav/Documents/Work/Projects/DataMining/data/'

class KeyWordAnalyzer(object):
    def __init__(self):
        self.locs = {}
    
    def bdCheckCondition(self, rec):
        if 'user' in rec:
            if 'location' in rec['user']:
                for k in keywords:
                    if k in rec['text'].lower():
                        if rec['user'] != None:
                            loc = rec['user']['location'].lower()
                            return loc
            else:
                return False
    
    def bdDoSomething(self,rec):
        # get time till hour
        time = parse(rec['created_at']).replace(minute=0,second=0,tzinfo=None)
        # location of tweet
        loc = rec['user']['location'].lower()
        
        if time in self.locs:
            if loc in self.locs[time]:
                self.locs[time][loc] += 1
            else:
                self.locs[time][loc] = 1
        else:
            self.locs[time] = {}

def processLocs():
    logo = logger()
    bd = BigData(logo)
    bd.processFiles(BigData.GetInputFiles(input_dir), None)

if __name__ == '__main__':
    pass