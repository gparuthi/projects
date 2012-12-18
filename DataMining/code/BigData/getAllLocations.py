'''                                                                                                                                                                                                                                           
Created on Dec 12, 2012                                                                                                                                                                                                                       
                                                                                                                                                                                                                                              
OB@author: gparuthi                                                                                                                                                                                                                           
'''
from DataMining.code.com.BigData import BigData
from DataMining.code.com.log import logger
from dateutil.parser import parse
from IPython import embed

input_dir = '/Users/gaurav/Documents/Work/Projects/DataMining/data/'

class AllLocations(object):   
    def __init__(self):
        self.locs = {}

    def bdCheckCondition(self, rec):
        if 'user' in rec:
            if 'location' in rec['user']:
                if (rec['user']['location'] != None):
                    return True
                else:
                    return False
        return False

    def bdDoSomething(self,rec):
        # get time till hour                                                                                                                                                                                                                 
        time = parse(rec['created_at']).replace(minute=0,second=0,tzinfo=None)
        # location of rec
        loc = rec['user']['location'].lower().replace('.','').replace(',','')
        if time in self.locs:
            try:   
                self.locs[time][loc] += 1
            except:
                self.locs[time][loc] = 1
        else:
            self.locs[time] = {}

ka = AllLocations()

def processLocs():
    print 'Starting all locations search:'
    logo = logger('AllLocs')
    bd = BigData(logo, status_line_count=10000)
    bd.obj = ka
    #bd.processFile(open('/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities/ny_11_1_to_11_15.data'), None)                                                                                                       
    bd.processFiles(BigData.GetInputFiles(input_dir), None)
    return ka

if __name__ == '__main__':
    pass
