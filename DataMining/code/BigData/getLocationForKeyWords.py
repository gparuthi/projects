'''
Created on Dec 12, 2012

OB@author: gparuthi
'''
from DataMining.code.com.BigData import BigData
from DataMining.code.com.log import logger
from dateutil.parser import parse
from IPython import embed

keywords = {'barack', 'obama', 'mitt', 'romney', 'president', 'election'}
input_dir = '/Users/gaurav/Documents/Work/Projects/DataMining/data/'

class KeyWordAnalyzer(object):
    def __init__(self, keywords):
        self.locs = {}
        self.keywords = keywords
    
    def bdCheckCondition(self, rec):
        if 'user' in rec:
            if 'location' in rec['user']:
                if (rec['user']['location'] != None):
                    for k in self.keywords:
                        if k in rec['text'].lower():
                                return True
            else:
                return False
        return False
    
    def bdDoSomething(self,rec):
        # get time till hour
        time = parse(rec['created_at']).replace(minute=0,second=0,tzinfo=None)
        # location of tweet
        loc = rec['user']['location'].lower().replace('.','').replace(',','')
        
        if time in self.locs:
            if loc in self.locs[time]:
                self.locs[time][loc] += 1
            else:
                self.locs[time][loc] = 1
        else:
            self.locs[time] = {}

ka = KeyWordAnalyzer(keywords)

def processLocs():
    print 'Starting keyword search:'
    logo = logger('Keywords')
    bd = BigData(logo)
    bd.obj = ka
    #bd.processFile(open('/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities/ny_11_1_to_11_15.data'), None)
    bd.processFiles(BigData.GetInputFiles(input_dir), None)
    return ka

if __name__ == '__main__':
    pass
