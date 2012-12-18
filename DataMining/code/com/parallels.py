import datetime
from dateutil.parser import parse 

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
