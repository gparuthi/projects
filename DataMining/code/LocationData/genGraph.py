'''
Created on Dec 4, 2012

@author: gparuthi
'''
from json import loads
import dateutil
import matplotlib
#matplotlib.use('GTK')
import matplotlib.dates
from matplotlib.pyplot import plot_date,show,figure
from StdSuites.Type_Names_Suite import rotation
from IPython import embed

dir = '../../uncompressed/locations_11_07_12'
dir2 = '../../uncompressed/locations_11_07_12'

def getCitiesHist(fpath):
    f = open(fpath)
    cities = loads(f.read())
    for c in cities:
        for t in cities[c]:
            count = 0
            for w in cities[c][t]:
                count += cities[c][t][w]
            cities[c][t] = count
    return cities
    
def genMulCities(fpath):
    print 'Generating histogram for timeline' + fpath
    with open(fpath, 'r') as content_file:
        content = content_file.read()
    print len(content)
    json = loads(content)
    for c in json:
        ts = {}
        for k in json[c]:
            ts[dateutil.parser.parse(k)] = json[c][k]
        genHist(ts, c)

def getDelhiHist(fpath):
    print 'Generating histogram for timeline' + fpath
    with open(fpath, 'r') as content_file:
        content = content_file.read()
    print len(content)
    json = loads(content)
    
    ts = {}
    for k in json:
        ts[dateutil.parser.parse(k)] = len(json[k])
    genHist(ts, 'name')

    embed()
    
def genHist(json, name):
    # generate histogram on this dictionary
    print json
    data = json.items()
    
    data.sort()
    
    x = [matplotlib.dates.date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]
    
    fig = figure()
    
    fig.canvas.set_window_title(name)
    
    graph = fig.add_subplot(111)
    
    # Plot the data as a red line with round markers
    graph.plot(x,y,'r-o')
    
    # Set the xtick locations to correspond to just the dates you entered.
    graph.set_xticks(x)
    
    # Set the xtick labels to correspond to just the dates you entered.
    graph.set_xticklabels(
            [date.strftime("%Y-%m-%d-%I") for (date, value) in data],
            rotation=90, size='small'
            
            )
    print 'done processing. Now showing...' 
    show()
    
    #plot_date(dates, ts.values())
    #show()

if __name__ == '__main__':
    #genMulCities(dir+'/5cities.timeline.json')
    getDelhiHist('../../../temp.json_1')
    print ''
