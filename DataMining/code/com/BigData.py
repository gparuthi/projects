'''
Created on Dec 10, 2012

@author: gparuthi
'''
import os
from datetime import datetime
from ujson import loads
import gzip
class BigData(object):
    '''
    This handles common things associated with big data
    '''
    def __init__(self, logger, status_line_count = 1000):
        '''
        Constructor
        '''
#       # calculate some stats here for the input files
        self.logger = logger
        self.obj = None
        self.start_time = datetime.now()
        self.status_line_count = status_line_count
#        self.city = paramets['city']
    
    def log(self, str):
        self.logger.log(str)
    
    def processFiles(self, input_files, output_filep):
        outf = None
        if output_filep != None:
            if os.path.isfile(output_filep):
                err_msg = 'Aborting . Out file aready exists:'+ self.output_filep
                self.log(err_msg)
                
            else:
                # create output file
                outf = open(output_filep,'w')  
        for filep in input_files:
            self.log('input gzip file:'+ filep)
            f = gzip.open(filep)
            self.log_stats(self.processFile(f,outf))
            # f.close() # commenting this as this showed an error. need to find out what the real problem is though.
        outf.close()

    def log_stats(self, t):
        now_time = datetime.now()
        self.log('File Stats for: ' + t['fname'])
        self.log('Total time taken: ' + str((now_time-self.start_time).seconds))
        self.log('Total number of lines found = ' + str(t['tot_lines']))
        self.log('Total number of lines With Locations = ' + str(t['loc_lines']))
    
    def processFile(self, f, outf):
        self.log( 'finding all records with location for: ' + f.name)
        
        tot_lines =0
        loc_lines =0
        line = f.readline()
        while line:
            #print line
            rec = loads(line)
            tot_lines += 1
            condition = self.obj.bdCheckCondition(rec) 
            if condition:
                if(outf!=None):
                    outf.write(line)
                self.obj.bdDoSomething(rec)
                loc_lines += 1
                if (loc_lines%self.status_line_count==0):
                    now_time = datetime.now()
                    self.log(str(loc_lines) + '/' + str(tot_lines) + ': ' + str((now_time-self.start_time).seconds))
            line = f.readline()
        ret = {'fname':f.name,'tot_lines': tot_lines, 'loc_lines': loc_lines}
        return ret
    
    @staticmethod
    def GetInputFiles(dir):
        paths = []
        for f in os.listdir(dir):
            paths.append(os.path.join(dir,f))        
        return paths
