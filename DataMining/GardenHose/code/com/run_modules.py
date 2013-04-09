from dateutil.parser import parse 

# Condtion methods available
def bdCheckCondition_select_keywords(rec, keywords):
    if 'user' in rec:
        if 'location' in rec['user']:
            if (rec['user']['location'] != None):
                for kword in keywords:
                    if kword in rec['text'].lower():
                        return True
            else:
                return False
        return False


def bdDoSomethingMemory(rec,times):
    # get time till hour                                                                                                                                                                                                                 
    time = parse(rec['created_at']).replace(minute=0,second=0,tzinfo=None)
    # location of rec                                                                                                                                                                                                                     
    loc = rec['user']['location'].lower().replace('.','').replace(',','')
    if time in times:
        try:
            times[time][loc] += 1
        except:
            times[time][loc] = 1
    else:
        times[time] = {}


def bdCheckCondition(rec):
    if 'user' in rec:
        if 'location' in rec['user']:
            if (rec['user']['location'] != None):
                return True
            else:
                return False
        return False