def getDiff(locs2,locs3):
    locs_diff = {}
    for k in locs2:
        if k in locs3:
            diff_perc = float((locs2[k]-locs3[k]))/float(locs3[k])*100
            diff = locs2[k]-locs3[k]
#            print k + '::' + str(diff)
            locs_diff[k] = diff_perc
        else:
#            if locs2[k] > 1100:
            print k + ':: not found :: ' + str(locs2[k])
    return locs_diff

def writeJsonToFile(fpath,json):
    if not os.path.isfile(fpath):
        f= open(fpath,'wb')
        f.write(dumps(json))
        f.close()
    else:
        print 'file already exists: '+ fpath    


def get_timeline_freq(cities):
    cities_freq = {}
    for city in cities:
        for hr in cities[city]:
            count = 0
            for w in cities[city][hr]:
                count += cities[city][hr][w]
    return cities_freq
