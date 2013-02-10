import datetime
from dateutil.parser import parse 

def bdDoSomethingRedis(rec, rc, filep):
    # get tweet id, the curent file path
    t_id = rec['id']
    # store the rec to redis
    rc.hset('tweets',t_id,filep)

    time = parse(rec['created_at']).replace(minute=0,second=0,tzinfo=None)

    # location of rec                                                                                                                                                                                                                     
    loc = rec['user']['location'].lower().replace('.','').replace(',','')

    # if the time and loc already existing then increase count else insert new count
    rc.hincrby(time,loc,1)

def bdDoSomething2(rec, db, filep):
	# get tweet id, the curent file path
	t_id = rec['id']
	# store the rec to mongodb
	db.tweets.insert({'tweet_id':t_id, 'filep':filep})

	time = parse(rec['created_at']).replace(minute=0,second=0,tzinfo=None)

	# location of rec                                                                                                                                                                                                                     
	loc = rec['user']['location'].lower().replace('.','').replace(',','')

	# if the time and loc already existing then increase count else insert new count
	db.timeline.update({'time':time, 'loc':loc}, {'$inc':{'count':1}}, True)

def bdCheckCondition(rec):
    if 'user' in rec:
        if 'location' in rec['user']:
            if (rec['user']['location'] != None):
                return True
            else:
                return False
        return False

def bdDoSomething(rec,locs):
    # get time till hour                                                                                                                                                                                                                 
    time = parse(rec['created_at']).replace(minute=0,second=0,tzinfo=None)
    # location of rec                                                                                                                                                                                                                     
    loc = rec['user']['location'].lower().replace('.','').replace(',','')
    if time in locs:
        try:
            locs[time][loc] += 1
        except:
            locs[time][loc] = 1
    else:
        locs[time] = {}


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


