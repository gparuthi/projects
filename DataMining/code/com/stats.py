
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
