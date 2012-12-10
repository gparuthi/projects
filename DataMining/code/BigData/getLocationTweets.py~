import gzip
from ujson import loads,dumps
from datetime import datetime
import os
from pprint import pprint
from DataMining.code.com.log import logger

logo = logger('BigDataLocations')
#LOGFILE_PATH = '/Users/gaurav/Documents/Work/Projects/DataMining/logs/' + 'BigData.'+str(datetime.now())+'.log'
#LOGFILE = open(LOGFILE_PATH,'wb')

def log(log_str):
    logo.log(log_str)
#    print str(log_str)
#    LOGFILE.write(str(log_str) + '\n')

def log_final_stats(res):
    # res is an array of arrays
    # the element array is a list of format: '['filename', totlines, loc_lines ]'
    log ('----------------------------------------------------------------------')
    log ('Final results:' + str(res))
    tot_lines = 0
    loc_lines = 0
    for r in res:
        tot_lines += r[1]
        loc_lines += r[2]
    log ('Total Lines found: ' + str (tot_lines))
    log ('Total lines with coordinates: ' +  str(loc_lines))
    log ('----------------------------------------------------------------------')
    LOGFILE.close()

def process_file(path):
    f = gzip.open(path)
    return f

def getCoordinatess(f,n=100):
    i =0
    for i in range(1,n):
        line = f.readline()
        rec = loads(line)
        if checkCoords(rec):
            cords = rec['coordinates']
            print cords
            print 'location: ' + rec['user']['location']
            print 'geo_enabled: ' + str(rec['user']['geo_enabled'])

def checkCoords(rec):
    if 'coordinates' in rec:
        coords = rec['coordinates']
        if coords != None:
            return True
        else:
            return False

def checkLocation(rec):
    #print(rec.keys())
    if 'user' in rec:
        user_data = rec['user']
        if 'location' in user_data:
            if user_data['location'] != None:
                loc = user_data['location'].lower()
            #print loc
                return loc
#                if 'delhi' in loc or 'new york' in loc:
#                    return loc
#                else:
#                    return None
            
locs = {}

def add_loc(loc):
    if loc in locs:
        locs[loc] +=1
    else:
        locs[loc] = 1

def getAllLocationsCount(f):
    log( 'finding all records with location delhi or new york data for: ' + f.name)
    start_time = datetime.now()
    tot_lines =0
    loc_lines =0
    line = f.readline()
    ret = []
    while line:
        rec = loads(line)
        tot_lines += 1
        location = checkLocation(rec) 
        if location != None:
            add_loc(location)
            #outf.write(line)
            loc_lines += 1
            if (loc_lines%100000==0):
                now_time = datetime.now()
                log(str(loc_lines) + '/' + str(tot_lines))
        line = f.readline()
    log('File Stats for: ' + f.name)
    log('Total time taken: ' + str((now_time-start_time).seconds))
    log('Total number of lines found = ' + str(tot_lines))
    log('Total number of lines With Locations = ' + str(loc_lines))
    ret = [f.name,tot_lines, loc_lines]
    return ret

def getAllLocations(f, outf):
    log( 'finding all records with location delhi or new york data for: ' + f.name)
    start_time = datetime.now()
    tot_lines =0
    loc_lines =0
    line = f.readline()
    ret = []
    while line:
        rec = loads(line)
        tot_lines += 1
        location = checkLocation(rec) 
        if location != None:
            outf.write(line)
            loc_lines += 1
            if (loc_lines%1000==0):
                now_time = datetime.now()
                log(str(loc_lines) + '/' + str(tot_lines) + ': ' + str((now_time-start_time).seconds))
        line = f.readline()
    log('File Stats for: ' + f.name)
    log('Total time taken: ' + str((now_time-start_time).seconds))
    log('Total number of lines found = ' + str(tot_lines))
    log('Total number of lines With Locations = ' + str(loc_lines))
    ret = [f.name,tot_lines, loc_lines]
    return ret

def getAllCoords(f, outf):
    log( 'finding all records with coordinate data for: ' + f.name)
    start_time = datetime.now()
    tot_lines =0
    loc_lines =0
    line = f.readline()
    ret = []
    while line:
        rec = loads(line)
        tot_lines += 1
        if checkCoords(rec):
            coords = rec['coordinates']
            #ret.append(rec)
            outf.write(line)
            loc_lines += 1
            if (loc_lines%1000==0):
                now_time = datetime.now()
                log(str(loc_lines) + '/' + str(tot_lines) + ': ' + str((now_time-start_time).seconds)) 
        line = f.readline()
    log('File Stats for: ' + f.name)
    log('Total time taken: ' + str((now_time-start_time).seconds))
    log('Total number of lines found = ' + str(tot_lines))
    log('Total number of lines With Coordinates = ' + str(loc_lines))
    ret = [f.name,tot_lines, loc_lines]
    return ret

def processCoords():
    dir = '/Users/gaurav/Documents/Work/Projects/DataMining/data/'
    flist = os.listdir(dir)
    res = []
    for fname in flist:
        if '.gz' in fname:
            newf_name = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/'+fname+'.data'
            if not os.path.isfile(newf_name):
                f= process_file(dir+fname)
                coordsf = open(newf_name, 'w')
                res.append(getAllCoords(f, coordsf))
            else:
                print "Skipping file because data already exists at:" + newf_name
    log_final_stats(res)

def processLocs():
    dir = '/Users/gaurav/Documents/Work/Projects/DataMining/data/'
    flist = os.listdir(dir)
    res = []
    for fname in flist:
        newf_name = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_11_07_12/'+fname+'.data'
        if not os.path.isfile(newf_name):
            f= process_file(dir+fname)
            #coordsf = open(newf_name, 'wb')
            res.append(getAllLocationsCount(f))
        else:
            print "Skipping file because data already exists at:" + newf_name
    log_final_stats(res)

# write a method to process the data and see if the location is something

#processLocs()
