from IPython import parallel
from datetime import datetime
from DataMining.code.com import log
import os

rc= parallel.Client()

lview = rc.load_balanced_view() 

lview.block = True

from DataMining.code.com.BigData import BigData
# input_files = BigData.GetInputFiles('./DataMining/data/')
input_files = ['./DataMining/data/gardenhose.2012-11-01.gz']


def bdCheckCondition(rec):
    if 'user' in rec:
        if 'location' in rec['user']:
            if (rec['user']['location'] != None):
                return True
            else:
                return False
        return False

def doSomething(rec):
	# store the rec to mongodb
	db.test.insert(rec)

@lview.parallel()
def processFile(filep):
        from DataMining.code.com import log, parallels
        import os
        from ujson import loads
        import gzip
        from pymongo import Connection
        
        c = Connection('localhost')
        db = c['tweets']


        f = gzip.open(filep)
        logger = log.logger('Parallel/'+os.path.basename(filep))
        logger.log( 'finding all records with location for: ' + f.name)
        locs = {}
        tot_lines =0
        loc_lines =0
        line = f.readline()
        while line:
            #print line                                                                                               
            rec = loads(line)
            tot_lines += 1
            condition = bdCheckCondition(rec)
            if condition:
                doSomething(rec)
                loc_lines += 1
                if (loc_lines%10000==0):
                    logger.log('Count:' + str(loc_lines) + '/' + str(tot_lines))
            line = f.readline()
        ret = {'fname':f.name,'tot_lines': tot_lines, 'loc_lines': loc_lines}
        return locs

print 'starting now..'
starttime = datetime.now()
res = processFile.map(input_files)
print 'time taken= '+ str(datetime.now()-starttime)
