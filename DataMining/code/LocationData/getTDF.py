import nltk
from ujson import loads, dumps
from datetime import datetime
import os
import log
from log import log

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



class City(object):
    def __init__(self,name,fname):
        self.name = name
        self.tdf = {}
        self.fname = fname
        self.f = open(fname,'w')
        self.tuples = []
        self.wordc = 0
        self.linec = 0

    def add_tuple(self, tuple):
        #self.tuples.append(tuple)
        #if len(tuples) == 1000
        if tuple in self.tdf:
            self.tdf[tuple] += 1
        else:
            self.tdf[tuple] = 1
        self.wordc += 1
        if self.wordc % 10000 ==0:
            log(self.get_top_words())
        
        
    def get_top_words(self):
        # return the top 10 from the tdf
        return self.name + ':: top words here. Size is : '+ str(len(self.tdf))  

    def write_to_file(self, line):
        self.f.write(line)
        self.linec += 1
        if self.linec % 100000 == 0:
            log (str(self.linec) + ':' + self.name)
        
def traverse(t):
    try:
        t.node
    except AttributeError:
        return
    else:
        if t.node == 'NP':  print t.sen  # or do something else
        else:
            for child in t:
                traverse(child)

def get_nouns(text, city):
    sentences = nltk.sent_tokenize(text) # NLTK default sentence segmenter
    sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
    sentences = [nltk.pos_tag(sent) for sent in sentences] # NLTK POS tagger
    for t in sentences[0]:
        # if the type is NN, NNP
        if t[1][0] == 'N':
            # add this to the final tuples
            city.add_tuple(t)
            
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

def start(dir):
    flist = os.listdir(dir)
    for fname in flist:
        if '.data' in fname:
            f= process_file(open(dir+fname))

delc = City('delhi',DELF_PATH)
nyc = City('nyc', NYF_PATH)
start(ALL_LOCS_DIR)
