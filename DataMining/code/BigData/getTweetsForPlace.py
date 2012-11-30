from get_dist_coords import distance_on_unit_sphere
from ujson import loads,dumps

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
del_file_path = OUT_DIR + 'delhi.data'
delf = open(del_file_path, 'w')

ny_lat = 40.7142
ny_long = -74.0064
ny_file_path = OUT_DIR + 'ny.data'
nyf = open(ny_file_path, 'w')

inputf = open(path1)
line = inputf.readline()

start_time = datetime.now()
tot_lines =0
loc_lines_del=0
loc_lines_ny=0

def near_to_city(city_lat, city_long, lat, long, line, name, cfile):
    del_dist = distance_on_unit_sphere(lat1,long1,del_lat,del_long) * MF
    if del_dist<CITY_RADIUS:
        return True
    else:
        return False

def printcStat(linc, tot_linescm, label, n):
    if (linc%n==0 and linc>1):
        now_time = datetime.now()
        print label + ':::::'+str(loc_lines) + '/' + str(tot_lines) + ': ' + str((now_time-start_time).seconds)

while line:
    rec = loads(line)
    coord = rec['coordinates']
    type = coord['type']
    coordinates = coord['coordinates']
    lat1 = coordinates[1]
    long1 = coordinates[0]
    near_to_city(del_lat,del_long, lat1, lat2, 'del', delf)
    del_dist = distance_on_unit_sphere(lat1,long1,del_lat,del_long) * MF
    ny_dist =  distance_on_unit_sphere(lat1,long1,ny_lat,ny_long) * MF
    if del_dist< CITY_RADIUS:
        delf.write(line)
        #print the status
        loc_lines_del += 1
        printcStat(loc_lines_del,tot_lines,'del', 100)
    if ny_dist < CITY_RADIUS:
        nyf.write(line)
        loc_lines_ny +=1
        printcStat(loc_lines_ny, tot_lines,'ny',1000)
    tot_lines+=1
    line = inputf.readline()

delf.close()
nyf.close()
inputf.close()
