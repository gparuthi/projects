'''
Created on Dec 2, 2012

@author: gparuthi
'''



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
        