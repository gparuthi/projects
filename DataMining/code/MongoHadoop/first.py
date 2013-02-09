from IPython import parallel
from datetime import datetime
from DataMining.code.com import log
import os

rc= parallel.Client()

lview = rc.load_balanced_view() 

lview.block = True

from DataMining.code.com.BigData import BigData
input_files = BigData.GetInputFiles('./DataMining/data/')
# input_files = ['./DataMining/data/gardenhose.2012-11-01.gz']


keywords = ['barack', 'obama', 'mitt', 'romney', 'president', 'election']
sel_cities = ['washington dc','boston ','atlanta ','boston','chicago ','new york','chicago','los angeles','toronto','london','rio','paris','mexico city','lima','singapore','tokyo','buenos aires','jakarta','bandung']
def bdCheckCondition_keywords(rec,sel_cities):
    if 'user' in rec:
        if 'location' in rec['user']:
            if (rec['user']['location'] != None):
                if rec['user']['location'] in sel_cities:
                    return True
            else:
                return False
        return False

def bdDoSomething_keywords(rec,locs,kwords):
    # get time till hour                                                                                                                                                                                                                 
    time = parse(rec['created_at']).replace(minute=0,second=0,tzinfo=None)
    # location of rec                                                                                                                                                                                                                     
    loc = rec['user']['location'].lower().replace('.','').replace(',','')

    isin_kwords = False

    for k in kwords:
        if k in rec['text'].lower():
            isin_kwords = True
        else:
            isin_kwords = False

    if time in locs:
        #initialize the location for the given time if not found
        if loc not in locs[time]:
            locs[time][loc] = {'kwords':0,'others':0}

        if isin_kwords:
            locs[time][loc]['kwords'] += 1
        else:
            locs[time][loc]['others'] += 1

    else:
        locs[time] = {}

def bdCheckCondition(rec):
    if 'user' in rec:
        if 'location' in rec['user']:
            if (rec['user']['location'] != None):
                return True
            else:
                return False
        return False

def doSomething(rec, db, filep):
	# get tweet id, the curent file path
	t_id = rec['id']
	# store the rec to mongodb
	db.tweets.insert({'tweet_id':t_id, 'filep':filep})
	time = parse(rec['created_at']).replace(minute=0,second=0,tzinfo=None)
    # location of rec                                                                                                                                                                                                                     
    loc = rec['user']['location'].lower().replace('.','').replace(',','')

    # if the time and loc already existing then increase count else insert new count
    db.timeline.update({'time':time, 'loc':loc}, {'$inc':{'count':1}}, True)



@lview.parallel()
def processFile(filep, bdCheckCondition, doSomething):
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
                doSomething(rec, db, filep)
                loc_lines += 1
                if (loc_lines%10000==0):
                    logger.log('Count:' + str(loc_lines) + '/' + str(tot_lines))
            line = f.readline()
        ret = {'fname':f.name,'tot_lines': tot_lines, 'loc_lines': loc_lines}
        return locs

print 'starting now..'
starttime = datetime.now()
res = processFile.map(input_files, bdCheckCondition, doSomething)
print 'time taken= '+ str(datetime.now()-starttime)
