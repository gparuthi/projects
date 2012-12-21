import os
from ujson import dumps
from datetime import datetime

def write_all_locs_to_file(dir,locs):
    i = 1
    for d in locs:
        f= open(os.path.join(dir,str(i)+'.data'),'wb')
        f.write(dumps(d))
        i+=1

def merge(locs):
    start_time = datetime.now()
    print 'start time is : '+ str(start_time)
    all_locs = {}
    i =0
    for d in locs:
        print 'processing file results from day: ' + str(i)
        for time in d:
            print 'time:' + str(time)
            if time not in all_locs:
                all_locs[time] = {}
            for loc in d[time]:
                if d[time][loc]>50:
                    newloc = loc
                    if newloc in all_locs[time]:
                        all_locs[time][newloc] += d[time][loc]
                    else:
                        all_locs[time][newloc] = d[time][loc]
        i+=1
    print 'finished at : '+str(datetime.now()) 
    print 'time taken= ' + str (datetime.now()-start_time)
    return all_locs


def merge_aloc(locs, oneloc):
    start_time = datetime.now()
    print 'start time is : '+ str(start_time)
    all_locs = {}
    i =0
    for d in locs:
        print 'processing file results from day: ' + str(i)
        for time in d:
            print 'time:' + str(time)
            if time not in all_locs:
                all_locs[time] = {}
            loc = oneloc
            if loc in d[time]:
                if d[time][loc]>50:
                    newloc = loc
                    if newloc in all_locs[time]:
                        all_locs[time][newloc] += d[time][loc]
                    else:
                        all_locs[time][newloc] = d[time][loc]
            else:
                all_locs[time][loc] = 0
        i+=1
    print 'finished at : '+str(datetime.now())
    print 'time taken= ' + str (datetime.now()-start_time)
    return all_locs

def merge_locs(locs, loc_list):
    start_time = datetime.now()
    print 'start time is : '+ str(start_time)
    all_locs = {}
    i =0
    for d in locs:
        print 'processing file results from day: ' + str(i)
        for time in d:
            print 'time:' + str(time)
            if time not in all_locs:
                all_locs[time] = {}
            for loc in loc_list:
#            for loc in d[time]:
#                if d[time][loc]>50:
                newloc = loc
                if loc in d[time]:
                    if newloc in all_locs[time]:
                        all_locs[time][newloc] += d[time][loc]
                    else:
                        all_locs[time][newloc] = d[time][loc]
                else:
                    print 'key error loc:%s, time:%s' %(loc,time)
        i+=1
    print 'finished at : '+str(datetime.now()) 
    print 'time taken= ' + str (datetime.now()-start_time)
    return all_locs
                
def temp():
    for k in all_locs:
        key = k.isoformat()
        if key not in all_locsd:
            all_locsd[key] = {}
        for l in all_locs[k]:
            if len(l)<2:
                print l
            else:
                all_locsd[key][l] = all_locs[k][l] 
            
