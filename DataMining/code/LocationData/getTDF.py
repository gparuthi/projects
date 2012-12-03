import nltk
from ujson import loads, dumps
from datetime import datetime
import os
import log
from log import log
from city import City

# ALGO:
# read all files in the location dir
# -read line by line
# --get location delhi/'new york'
# --line->json->tagged_text->
# ---all nouns in the tagged text-> add to the tdf dictionary for the- respective location

# global variables
# output files:
DELF_PATH = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities/'+'del_11_1_to_11_15'+'.data'
NYF_PATH = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities/'+'ny_11_1_to_11_15'+'.data'
ALL_LOCS_DIR = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_all/'


            
def get_location(rec):
    #check for delhi vs ny
    loc = rec['user']['location'].lower()
    #print loc
    if 'delhi' in loc:
        return delc
    else:
        return nyc # this means it is newyork since we have already filtered the data to keep just 'delhi' and 'new york'

def process_file(f):
    log('Processing file: ' + f.name)
    # define vars
    start_time = datetime.now()
    loc_lines = 0
    tot_lines = 1
    line = f.readline()
    while line:
        rec = loads(line)
        loc = get_location(rec)
#        noun_list = get_nouns(rec['text'], loc)
        loc.write_to_file(line) # Write the rec to the city file
        if tot_lines %10000 ==0:
            log(f.name+ '::tot_lines: ' + str(tot_lines))
        tot_lines+=1
        line = f.readline()
    log(f.name + '::tot_lines: ' + str(tot_lines))

### This method seperates the files to delhi and ny data
def start(dir):
    flist = os.listdir(dir)
    for fname in flist:
        if '.data' in fname:
            f= process_file(open(dir+fname))

delc = City('delhi',DELF_PATH)
nyc = City('nyc', NYF_PATH)
start(ALL_LOCS_DIR)
