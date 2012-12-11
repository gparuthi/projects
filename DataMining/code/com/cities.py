'''
Created on Dec 10, 2012

@author: gparuthi
'''
from DataMining.code.com.city2 import City2
from DataMining.code.com.BigData import BigData
from DataMining.code.com.log import logger
import nltk
import os
from ujson import dumps

class Cities(object):
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
        self.d = dict((x,City2(x, self.getOutFile(x))) for x in params)
        self.logger = logger('Multiple_cities')
        self.curCity = ''
    
    def getOutFile(self, city_name):
        # return the output file path for the input city
        return os.path.join(self.outDir, city_name + '.data')
    
    def generateTDF(self, input_files):
        self.bd = BigData(self.logger)
        self.bd.obj = self
        self.bdCheckCondition = self.CheckCondition
        self.bdDoSomething = self.DoSomething
        self.bd.processFiles(input_files,None)

    def CheckCondition(self, rec):
        if 'user' in rec:
            user_data = rec['user']
            if 'location' in user_data:
                if user_data['location'] != None:
                    loc = user_data['location'].lower()
                    for k in self.d:
                        if k in loc:
                            self.curCity = k
                       #     print k + ':' + loc
                            return True
                        else:
                            return False
        return False
                    
                    
    def DoSomething(self, rec):
        text = rec['text'].encode('utf-8')
        loc = self.curCity
        #print loc
        sentences = nltk.sent_tokenize(text) # NLTK default sentence segmenter
        sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
        #sentences = post_tag(sentences)
        #print sentences
        for sent in sentences:
            #print sent
            #a = nltk.pos_tag(sent) 
            for w in sent:
                if w in self.d[loc].tdf:
                    self.d[loc].tdf[w] +=1
                else:
                    self.d[loc].tdf[w] = 1
        # write output to outfile
        self.d[loc].write(dumps(rec))
        
    def getNounsTDF(self):
        for k in self.d:
            self.d[k].getNounsTDF()
    
    def getTimeLine(self):
        bd = BigData(self.logger)
        for k in self.d:
            self.d[k].getTimeLine(bd)
    
    
