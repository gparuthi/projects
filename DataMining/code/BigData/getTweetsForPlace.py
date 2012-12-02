from get_dist_coords import distance_on_unit_sphere
from ujson import loads,dumps
from datetime import datetime
import os

# load file to process

# delhi coordinates

# for each tweet calculate the distance between delhi and new york and that coordinate
# if its less than 40 miles then write to ouput files of delhi or newyork

# input Dir
IN_DIR = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/'

# output directory:
OUT_DIR = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/cities/'
# multiplication factor for miles:
MF = 3960
CITY_RADIUS = 40
path1 = IN_DIR + 'temp.data' #'gardenhose.2012-11-01.gz.data'

del_lat = 29.0167
del_long= 77.3833
#del_file_path = OUT_DIR + 'delhi.data'
#delf = open(del_file_path, 'w')

ny_lat = 40.7142
ny_long = -74.0064
#ny_file_path = OUT_DIR + 'ny.data'
#nyf = open(ny_file_path, 'w')

start_time = datetime.now()

LOGFILE_PATH = '/Users/gaurav/Documents/Work/Projects/DataMining/logs/' + 'CityData.'+str(datetime.now())+'.log'
LOGFILE = open(LOGFILE_PATH,'w')

def log(log_str):
    print str(log_str)
    LOGFILE.write(str(log_str) + '\n')

def log_file_stats(fname, tot_lines, loc_lines):
    now_time = datetime.now()
    log('File Stats for: ' + fname)
    log('Total time taken: ' + str((now_time-start_time).seconds))
    log('Total number of lines found = ' + str(tot_lines))
    log('Total number of lines With Coordinates = ' + str(loc_lines))

def log_final_stats(res):
    log ('----------------------------------------------------------------------')
    log ('Final results:' + str(res))
    tot_lines = 0
    loc_lines_del = 0
    loc_lines_ny = 0
    for r in res:
        tot_lines += r['tot_lines']
        loc_lines_del += r['loc_lines_del']
        loc_lines_ny += r['loc_lines_ny']

    log ('Total Lines found: ' + str (tot_lines))
    log ('Total delhi lines with coordinates: ' +  str(loc_lines_del))
    log ('Total ny lines with coordinates: ' +  str(loc_lines_ny))
    log ('----------------------------------------------------------------------')
    #LOGFILE.close()

def near_to_city(city_lat, city_long, lat, long, name):
    del_dist = distance_on_unit_sphere(lat,long,city_lat,city_long) * MF
    if del_dist<CITY_RADIUS:
        return True
    else:
        return False

def printcStat(loc_lines, tot_lines, label, n):
    if (loc_lines%n==0 and loc_lines>1):
        now_time = datetime.now()
        log(label + ':::::'+str(loc_lines) + '/' + str(tot_lines) + ': ' + str((now_time-start_time).seconds))



def ProcessFiles(dir):
    log('Getting del and ny data from files:')
    flist = os.listdir(dir)
    res = []
    for fname in flist:
        if '.data' in fname:
            print 'processing file: ' + fname
            tot_lines =0
            loc_lines_del=0
            loc_lines_ny=0

            delfname = OUT_DIR + fname + '.delhi'
            nyfname = OUT_DIR + fname + '.ny'
            delf = open(delfname, 'w')
            nyf = open(nyfname, 'w')
            inputf = open(IN_DIR + fname)
            line = inputf.readline()
            while line:
                rec = loads(line)
                coord = rec['coordinates']
                type = coord['type']
                coordinates = coord['coordinates']
                lat1 = coordinates[1]
                long1 = coordinates[0]
                near_to_city(del_lat,del_long, lat1, long1, 'del')
                del_dist = distance_on_unit_sphere(lat1,long1,del_lat,del_long) * MF
                ny_dist =  distance_on_unit_sphere(lat1,long1,ny_lat,ny_long) * MF
                if del_dist< CITY_RADIUS:
                    delf.write(line) 
                    loc_lines_del += 1
                    printcStat(loc_lines_del,tot_lines,'del', 100) #print the status
                if ny_dist < CITY_RADIUS:
                    nyf.write(line)
                    loc_lines_ny +=1
                    printcStat(loc_lines_ny, tot_lines,'ny',1000)
                tot_lines+=1
                line = inputf.readline()
            log_file_stats(delfname, tot_lines, loc_lines_del)
            log_file_stats(nyfname, tot_lines, loc_lines_ny)
            res.append({'input_file':fname,'del_file':delfname, 'ny_file': nyfname, 'tot_lines':tot_lines, 'loc_lines_del': loc_lines_del, 'loc_lines_ny': loc_lines_ny})
            delf.close()
            nyf.close()
            inputf.close()

    log_final_stats(res)

#ProcessFiles(IN_DIR)

