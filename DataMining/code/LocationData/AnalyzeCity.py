'''
Created on Dec 2, 2012

@author: gparuthi
'''

import nltk
from ujson import loads, dumps
from datetime import datetime
import os
import log
from log import log
from city import City

DELF_PATH = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities/'+'del_11_1_to_11_15'+'.data'
NYF_PATH = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities/'+'ny_11_1_to_11_15'+'.data'


def get_nouns(text, city):
    sentences = nltk.sent_tokenize(text) # NLTK default sentence segmenter
    sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
    sentences = [nltk.pos_tag(sent) for sent in sentences] # NLTK POS tagger
    for t in sentences[0]:
        # if the type is NN, NNP
        if t[1][0] == 'N':
            # add this to the final tuples
            city.add_tuple(t)
            
def analyze_city(f, loc):
    log('Processing file: ' + f.name)
    # define vars
    start_time = datetime.now()
    loc_lines = 0
    tot_lines = 1
    line = f.readline()
    while line:
        rec = loads(line)
        noun_list = get_nouns(rec['text'], loc)
        if tot_lines %10000 ==0:
            log(f.name+ '::tot_lines: ' + str(tot_lines))
        tot_lines+=1
        line = f.readline()
    log(f.name + '::tot_lines: ' + str(tot_lines))

delc = City('delhi','')
nyc = City('nyc', '')

if __name__ == '__main__':
    analyze_city(open(DELF_PATH), delc)