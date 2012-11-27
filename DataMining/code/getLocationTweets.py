import gzip
from ujson import loads,dumps
from datetime import datetime
import os


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
            

def getAllCoords(f, outf):
    print 'finding all records with coordinate data'
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
                print str(loc_lines) + '/' + str(tot_lines) + ': ' + str((now_time-start_time).seconds) 
        line = f.readline()
    return ret


dir = '/Users/gaurav/Documents/Work/Projects/DataMining/data/'
flist = os.listdir(dir)
for fname in flist:
    if '.gz' in fname:
        newf_name = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/'+fname+'.data'
        if not os.path.isfile(newf_name):
            f= process_file(dir+fname)
            coordsf = open(newf_name, 'w')
            getAllCoords(f, coordsf)

