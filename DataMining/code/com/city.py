'''
Created on Dec 2, 2012

@author: gparuthi
'''
from nltk.corpus import stopwords
import nltk
import os
from json import dumps
from dateutil.parser import parse
from DataMining.code.com import BigData


class City(object):
    '''
    This class is for storing one city's data
    '''
    def __init__(self,name,bd, out_filep):
        self.name = name
        self.filep = out_filep
        self.bd = bd
        self.tdf = {}
        self.tuples = []
        self.timeline = {}
        self.tdf_nouns = {}
        self.tdf_tags = {} # contains tdf tags
    
    def generateTDF(self):
        self.bd.obj = self
        self.bdCheckCondition = self.CheckCondition
        self.bdDoSomething = self.DoSomething
        self.bd.processFiles()
        
        
    def CheckCondition(self,rec):
        if 'user' in rec:
            user_data = rec['user']
            if 'location' in user_data:
                if user_data['location'] != None:
                    loc = user_data['location'].lower()
                    if self.name in loc:
                        return True
                    else:
                        return False
                    
    def DoSomething(self, rec):
        text = rec['text'].encode('utf-8')
        
        sentences = nltk.sent_tokenize(text) # NLTK default sentence segmenter
        sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
        #sentences = post_tag(sentences)
        #print sentences
        for sent in sentences:
            #print sent
            #a = nltk.pos_tag(sent) 
            for w in sent:
                if w in self.tdf:
                    self.tdf[w] +=1
                else:
                    self.tdf[w] = 1
        return self.tdf
    
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

    def getTimeLine(self, bd):
        self.bd.obj = bd
        self.bdCheckCondition = self.CheckCondition
        self.bdDoSomething = self.bdTimeLineDS
        self.bd.log_stats(self.bd.processFiles(open(self.filep), None))

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
        ts = dict((x,self.timeline[x]) for x in self.timeline.keys())
        City.writeJsonToFile(fpath,ts)
