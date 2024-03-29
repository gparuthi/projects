'''
Created on Dec 2, 2012

@author: gparuthi
'''
from nltk.corpus import stopwords
import os
from json import dumps

class City(object):
    def __init__(self,name,fname):
        self.name = name
        self.tdf = {}
        if fname != None:
            self.fname = fname
            self.f = open(fname,'w')
        self.tuples = []
        self.wordc = 0
        self.linec = 0
        self.tdf_class = {}
        self.timeline = {}
        self.tdf_nouns = {}

    def add_tuple(self, tuple):
        #self.tuples.append(tuple)
        #if len(tuples) == 1000
        if tuple in self.tdf:
            self.tdf[tuple] += 1
        else:
            self.tdf[tuple] = 1
        self.wordc += 1
        if self.wordc % 100 ==0:
            print(self.get_top_words())
        
        
    def get_top_words(self):
        # return the top 10 from the tdf
        l = len(self.tuples)
        for i in range(l-100,l-1):
            print self.tuples[i]

        return self.name + ':: top words here. Size is : '+ str(len(self.tdf))  

    def write_to_file(self, line):
        self.f.write(line)
        self.linec += 1
        if self.linec % 100000 == 0:
            print (str(self.linec) + ':' + self.name)
        
    def clean_tdf(self):
        print 'Generating tuples for nouns in the tdf for :' + self.name 
        self.tuples = []
        for k in self.tdf:
            if k.lower() not in stopwords.words('english'): # is not a stopword
                if self.tdf_class[k][0]=='N': # is a noun
                    self.tdf_nouns[k] = self.tdf[k]
 #                   self.tuples.append((self.tdf[k],k))
 #       self.tuples.sort()

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
