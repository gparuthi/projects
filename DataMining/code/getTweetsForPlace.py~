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

while line:
    rec = loads(line)
    coord = rec['coordinates']
    type = coord['type']
    coordinates = coord['coordinates']
    lat1 = coordinates[0]
    long1 = coordinates[1]
    del_dist = distance_on_unit_sphere(lat1,long1,del_lat,del_long) * MF
    ny_dist =  distance_on_unit_sphere(lat1,long1,ny_lat,ny_long) * MF
    if del_dist< CITY_RADIUS:
        delf.write(line)
    if ny_dist < CITY_RADIUS:
        nyf.write(line)
        
    line = inputf.readline()

delf.close()
nyf.close()
inputf.close()
