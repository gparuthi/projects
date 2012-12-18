import os
from ujson import dumps

#sellocs = {}

def run(all_locs,sel_locs, w):
    for k in all_locs:
        if k not in sel_locs:
            sel_locs[k] = {}
        sel_locs[k][w]=0
        d= all_locs[k]
        for loc in d:
            if w in loc:
                sel_locs[k][w] += d[loc]

def getfnam(path):
    rex = '\..*\.'
    m = re.search(rex,path)
    return m.group().replace('.','')


def writeJsonToFile(fpath,json):
    if not os.path.isfile(fpath):
        f= open(fpath,'wb')
        f.write(dumps(json))
        f.close()
    else:
        print 'file already exists: '+ fpath

## for the json with filename as keys 
def write_to_file(all_locs, dir):
    for k in all_locs:
        fname = os.path.basename(k)
        fpath = os.path.join(dir,fname)
        print fname
        if not os.path.isfile(fpath):
            f = open(fpath,'w')
            f.write(dumps(all_locs[k]))
        else:
            print 'file already existing: '+ fpath

## for the json with dates as keys
def write_dates_json_to_file2(locs, filep):
    json = {}
    if not os.path.isfile(filep):
        for k in locs.keys():
            print k
            datestr = k.isoformat() # get date str
            json[datestr] = locs[k]
        # write json to file
        f = open(filep,'w')
        f.write(dumps(json))
    else:
        print 'file already existing: '+ filep
        
def get_all_locs_i(locs):
    ret = {}
    for k in locs:
        newk = k.lower().replace(',','').replace('.','')
        if newk in ret:
            ret[newk] += 1
        else:
            ret[newk] = 1
    return ret
