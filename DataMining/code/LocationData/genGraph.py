'''
Created on Dec 4, 2012

@author: gparuthi
'''
from json import loads
import dateutil
import matplotlib
matplotlib.use('GTK')
import matplotlib.dates
from matplotlib.pyplot import plot_date,show,figure
from StdSuites.Type_Names_Suite import rotation

dir = '../../uncompressed/locations_cities'


def getDelhiHist(fpath):
    print 'Generating histogram for timeline' + fpath
    with open(fpath, 'r') as content_file:
        content = content_file.read()
    print len(content)
    json = loads(content)
    genHist(json)

def genHist(json):
    # generate histogram on this dictionary
    ts = {}
    for k in json:
        ts[dateutil.parser.parse(k)] = len(json[k])
    
    data = ts.items()
    
    data.sort()
    
    x = [matplotlib.dates.date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]
    
    fig = figure()
    
    graph = fig.add_subplot(111)
    
    # Plot the data as a red line with round markers
    graph.plot(x,y,'r-o')
    
    # Set the xtick locations to correspond to just the dates you entered.
    graph.set_xticks(x)
    
    # Set the xtick labels to correspond to just the dates you entered.
    graph.set_xticklabels(
            [date.strftime("%Y-%m-%d-%I") for (date, value) in data],
            rotation=30, size='small'
            
            )
    print 'done processing. Now showing...' 
    show()
    
    #plot_date(dates, ts.values())
    #show()

if __name__ == '__main__':
    getDelhiHist(dir+'/del_11_1_to_11_15.tsd')
        
