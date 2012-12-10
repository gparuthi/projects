'''
Created on Dec 9, 2012

@author: gparuthi
'''
from DataMining.code.com.log import logger
from DataMining.code.com.BigData import BigData
from DataMining.code.com.city import City

params = { 
              'input_dir_path': '',
              'out_file_path': '',
              'timeline_path':'',
              'logger' : logger('OneCity')  
              }

def start():
    
    # crawl each data file and get data for the given location
    # store the data in the output file    
    bd = BigData(params['dir_path'],params['out_file_path'])
    city = City('london',bd)
    # Generate the tdf for the city
    city.generateTDF()
    # get nouns for the city
    city.getNounsTDF()
    
    # load another bigData obj
    params = {'input_file_path' : city.filep, out_file_path : None, }
    # get timeline for city
    city.getTimeLine()
    # write timeline to file
    city.writeTimelineToFile(params['timeline_path'])

if __name__ == '__main__':
    pass