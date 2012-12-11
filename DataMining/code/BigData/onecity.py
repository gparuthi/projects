'''
Created on Dec 9, 2012

@author: gparuthi
'''
from DataMining.code.com.log import logger
from DataMining.code.com.BigData import BigData
from DataMining.code.com.city import City
from DataMining.code.com.cities import Cities
import os

CITY_NAME = 'london'

params = { 
              'input_dir_path': '/Users/gaurav/Documents/Work/Projects/DataMining/data/',
              'out_file_path': '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities/'+CITY_NAME+'/'+CITY_NAME+'.data',
              'timeline_path':'/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities/'+CITY_NAME+'/'+CITY_NAME+'.timeline.json',
              'logger' : logger('OneCity')  
              }

def GetInputFiles(dir):
    paths = []
    for f in os.listdir(dir):
        paths.append(os.path.join(dir,f))        
    return paths

def start(params):
    # crawl each data file and get data for the given location
    # store the data in the output file    
    bd = BigData(params)
    city = City(CITY_NAME,bd,params['out_file_path'])
    input_files = bd.GetInputFiles(params['input_dir_path'])
    # Generate the tdf for the city
    city.generateTDF(input_files)
    # get nouns for the city
    city.getNounsTDF()
    
    # load another bigData obj for generating timeline
    params = {'input_dir_path':'', 'input_file_path' : city.filep, 'out_file_path' : None, 'logger':params['logger']}
    bd = BigData(params)
    # get timeline for city
    city.getTimeLine(bd)
    # write timeline to file
    city.writeTimelineToFile(params['timeline_path'])


in_dir = '/Users/gaurav/Documents/Work/Projects/DataMining/data/'
out_dir = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/all_locations/'
cits = {'delhi', 'london', 'washington'}

def startm():

    cs = Cities(cits, out_dir)
    
    input_files = GetInputFiles(in_dir)
    cs.generateTDF(input_files)
    cs.getNounsTDF()
    cs.getTimeLine()

if __name__ == '__main__':
    pass
