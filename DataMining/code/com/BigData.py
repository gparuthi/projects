'''
Created on Dec 10, 2012

@author: gparuthi
'''
import os
from datetime import datetime
from ujson import loads

class BigData(dict):
    '''
    This handles common things associated with big data
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        self.input_files = self.GetInputFiles(params['input_dir_path']) # data to crawl
        self.output_filep = params['out_file_path']  # data to output to
        # calculate some stats here for the input files
        self.logger = params['logger']
        self.obj = None
#        self.city = params['city']
    
    def log(self, str):
        self.logger.log(str)
    
    def GetInputFiles(self, dir):
        paths = []
        for f in os.listdir(dir):
            paths.append(os.path.join(dir,f))        
        return paths
    
    def processFiles(self):
        if os.path.isfile(self.output_filep):
            err_msg = 'Aborting. Out file aready exists:'+ self.output_filep
            self.log(err_msg)
            return err_msg
        else:
            # create output file
            outf = open(self.output_filep,'w')  
            for filep in self.input_files:
                f = open(filep)
                self.log_stats(self.processFile(f,outf))
                f.close()
            outf.close()

    def log_stats(self, t):
        now_time = datetime.now()
        self.log('File Stats for: ' + t['fname'])
        self.log('Total time taken: ' + str((now_time-self.start_time).seconds))
        self.log('Total number of lines found = ' + t['tot_lines'])
        self.log('Total number of lines With Locations = ' + t['loc_lines'])
    
    def processFile(self, f, outf):
        self.log( 'finding all records with location delhi or new york data for: ' + f.name)
        self.start_time = datetime.now()
        tot_lines =0
        loc_lines =0
        line = f.readline()
        while line:
            rec = loads(line)
            tot_lines += 1
            condition = self.obj.bdCheckCondition(rec) 
            if condition:
                if(outf!=None):
                    outf.write(line)
                self.obj.bdDoSomething(rec)
                loc_lines += 1
                if (loc_lines%1000==0):
                    now_time = datetime.now()
                    self.log(str(loc_lines) + '/' + str(tot_lines) + ': ' + str((now_time-self.start_time).seconds))
            line = f.readline()
        ret = {'fname':f.name,'tot_lines': tot_lines, 'loc_lines': loc_lines}
        return ret