import os
from ujson import dumps, loads
from datetime import datetime

dir = './DataMining/uncompressed/all_locations/all_data_again/'

def GetInputFiles(dir, file_type=''):
    paths = []
    for f in os.listdir(dir):
        if file_type in f:
            paths.append(os.path.join(dir,f))        
    return paths

def write_all_locs_to_file(locs, dir = dir):
    start_time = datetime.now()
    print 'start time is : '+ str(start_time)
    i = 1
    print 'writing all data to file'
    for d in locs:
        print str(datetime.now()) + ': working on file: ' + str(i)
        f= open(os.path.join(dir,str(i)+'_'+str(start_time)+'.data'),'wb')
        f.write(dumps(d))
        i+=1
    print 'finished at : '+str(datetime.now())  
    print 'time taken= ' + str (datetime.now()-start_time) 

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

def merge_files(filesp):
    start_time = datetime.now()
    print 'start time is : '+ str(start_time)
    # iterate each file and readjson
    all_locs = {}
    i =0
    for fp in filesp:
        f = open(fp,'rb')
        d = loads(f.read())
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
            
