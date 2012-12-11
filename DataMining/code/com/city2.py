'''
Created on Dec 2, 2012

@author: gparuthi
'''
from nltk.corpus import stopwords
import nltk
import os
from json import dumps
from dateutil.parser import parse

class City2(object):
    '''
    This class is for storing one city's data
    '''
    def __init__(self,name,out_filep):
        self.name = name
        self.tdf = {}
        self.tuples = []
        self.timeline = {}
        self.tdf_nouns = {}
        self.tdf_tags = {} # contains tdf tags
        self.filep = out_filep
        self.fileo = open(self.filep,'w')
       
    def tag_tdf(self):
        tags = nltk.pos_tag(self.tdf.keys())
        self.tdf_tags = dict((x,y) for x,y in tags)

    def getNounsTDF(self):
        print 'Generating tuples for nouns in the tdf for :' + self.name 
        self.tag_tdf()
        for k in self.tdf:
            if k.lower() not in stopwords.words('english'): # is not a stopword
                if self.tdf_tags[k][0]=='N': # is a noun
                    self.tdf_nouns[k] = self.tdf[k]
    
    def tlCheck(self,rec):
        return True

    def getTimeLine(self, bd):
        bd = bd
        bd.obj = self
        self.bdCheckCondition = self.tlCheck 
        self.bdDoSomething = self.bdTimeLineDS
        bd.log_stats(bd.processFile(open(self.filep), None))

    def bdTimeLineDS(self, rec):
        tweet_date = parse(rec['created_at']).replace(minute=0,second=0)
        text = rec['text']
        sentences = nltk.sent_tokenize(text) # NLTK default sentence segmenter
        sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
        #sentences = post_tag(sentences)
        #print sentences
        for sent in sentences:
            #print sent
            #a = nltk.pos_tag(sent) 
            for w in sent:
                if w in self.tdf_nouns:
                    if tweet_date in self.timeline:
                        self.timeline[tweet_date].append(w) # add word to that date key
                    else:
                        self.timeline[tweet_date] = [w]
        
    @staticmethod
    def writeJsonToFile(fpath,json):
        if not os.path.isfile(fpath):
            f= open(fpath,'wb')
            f.write(dumps(json))
            f.close()
        else:
            print 'file already exists: '+ fpath
    
    def writeTimelineToFile(self,fpath):
        ts = dict((x.isoformat(),self.timeline[x]) for x in self.timeline.keys())
        City.writeJsonToFile(fpath,ts)
        
    def write(self,line):
        self.fileo.write(line)