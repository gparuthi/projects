'''
Created on Dec 10, 2012

@author: gparuthi
'''
from DataMining.code.com.city2 import City2
from DataMining.code.com import BigData
from DataMining.code.com.log import logger
import nltk
import os

class Cities(dict):
    '''
    classdocs
    '''
    def __init__(self, params, outDir):
        '''
        Constructor
        params: a list of city names
        outDir: is the output directory path 
        '''
        self.outDir = outDir
        self = dict((x,City2(x, self.getOutFile(x))) for x in params)
        self.logger = logger()
        self.bd = BigData(self.logger)
    
    def getOutFile(self, city_name):
        # return the output file path for the input city
        return os.path.join(self.outDir, city_name)
    
    def generateTDF(self, input_files):
        self.bd = BigData(self.logger)
        self.bd.obj = self
        self.bdCheckCondition = self.CheckCondition
        self.bdDoSomething = self.DoSomething
        self.bd.processFiles(input_files)

    def CheckCondition(self, rec):
        if 'user' in rec:
            user_data = rec['user']
            if 'location' in user_data:
                if user_data['location'] != None:
                    loc = user_data['location'].lower()
                    for k in self:
                        if k in loc:
                            self.curCity = k
                            return True
                        else:
                            return False
                    
    def DoSomething(self, rec):
        text = rec['text'].encode('utf-8')
        loc = self.curCity
        
        sentences = nltk.sent_tokenize(text) # NLTK default sentence segmenter
        sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
        #sentences = post_tag(sentences)
        #print sentences
        for sent in sentences:
            #print sent
            #a = nltk.pos_tag(sent) 
            for w in sent:
                if w in self[loc].tdf:
                    self[loc].tdf[w] +=1
                else:
                    self[loc].tdf[w] = 1
    
    def getNounsTDF(self):
        for k in self:
            self[k].getNounsTDF()
    
    def getTimeLine(self):
        bd = BigData(self.logger)
        for k in self:
            self[k].getTimeLine(bd)
    
    