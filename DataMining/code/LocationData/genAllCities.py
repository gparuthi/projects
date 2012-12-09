import nltk
from ujson import loads, dumps
from datetime import datetime
import os
from log import logger
from city import City
from dateutil.parser import parse  

file_path = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities/'+'del_11_1_to_11_15'+'.data'
logo = logger('City_Location')

def log(str):
    logo.log(str)



cities = {}

noun_words = {}
not_nouns = {}

def get_timeline(text, date, loc):
    sentences = nltk.sent_tokenize(text) # NLTK default sentence segmenter
    sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
    #sentences = post_tag(sentences)
    #print sentences

    # check if location is in the cities dict
    if loc not in cities:
        cities[loc] = {}

    for sent in sentences:
        #print sent
        #a = nltk.pos_tag(sent)
        for w in sent:
            if w not in noun_words and w not in not_nouns:
                # identify w and add it to either one of the list
                tag = nltk.pos_tag([w])
                tag = tag[0][1]
                if tag[0] == 'N':
                    noun_words[w] = 1
                else:
                    not_nouns[w] = 1
            if w in noun_words:
                if date not in cities[loc]:
                    cities[loc][date] = {}
                if w in cities[loc][date]:
                    cities[loc][date][w] += 1 # add word to that date key
                else:
                    cities[loc][date][w] = 1        
    return ''

def getTillHour(date):
    ret = parse(date).replace(minute=0,second=0,tzinfo=None)
    return ret

def getTimesCity(f,locs):
    log('Processing file: ' + f.name)
    # define vars 
    start_time = datetime.now()
    loc_lines = 0
    tot_lines = 1
    line = f.readline()
    text = ''
    while line:
        rec = loads(line)
        text = rec['text'].encode('utf-8')
        # get pos_tags for the line and write to output file
        tweet_date = getTillHour(rec['created_at'])
        loc = rec['user']['location']
        if loc in locs:
            get_timeline(text, tweet_date, loc)
        if tot_lines %10000 == 0:
            log(f.name+ '::tot_lines: ' + str(tot_lines))
        tot_lines+=1
        line = f.readline()
    logo.log_file_stats(f.name, tot_lines, tot_lines)
    return city
