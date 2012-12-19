
'''
Created on Dec 4, 2012

@author: gparuthi
'''
from json import loads
import dateutil
from StdSuites.Type_Names_Suite import rotation
from IPython import embed
import os

dir = '/Users/gaurav/Documents/Work/Projects/DataMining/uncompressed/locations_cities'
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
        getCity(c,json[c])

def genOneCity(c,fpath):
    with open(fpath, 'r') as content_file:
        content = content_file.read()
    json = loads(content)
    getCity(c,json)
    
def getCity(c,city_json):
    ts = {}
    for k in city_json:
        ts[dateutil.parser.parse(k)] = city_json[k]
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
    return genHist(ts, 'name')
    
def genHist(json, name):
    # generate histogram on this dictionary
    # print json
    data = json.items()
    
    data.sort()
    
    x = [matplotlib.dates.date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]
    
    fig = figure(figsize=(len(x)/3,6))
    
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
    
    return graph
    #show()
    
    #plot_date(dates, ts.values())
    #show()

if __name__ == '__main__':
    #genMulCities(dir+'/5cities.timeline.json')
    #getDelhiHist('../../../temp.json_1')
    #genOneCity('nyc',os.path.join(dir,'del_11_1_to_11_15.new_timeline'))
    print ''
