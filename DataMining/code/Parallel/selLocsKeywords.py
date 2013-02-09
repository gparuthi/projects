from IPython import parallel
from datetime import datetime
from DataMining.code.com import log,parallels
import os

rc= parallel.Client()

lview = rc.load_balanced_view()

lview.block = True

from DataMining.code.com.BigData import BigData
input_files = BigData.GetInputFiles('./DataMining/data/')


@lview.parallel()
def processFile(filep):
        from DataMining.code.com import log, parallels
        import os
        from ujson import loads, dumps
        import gzip
        
        outfilep = './DataMining/uncompressed/sel_cities/'+ os.path.basename(filep) + '.json'
        f = gzip.open(filep)
        logger = log.logger('Parallel/'+os.path.basename(filep))
        logger.log( 'finding all records with location for: ' + f.name)
        locs = {}
        tot_lines =0
        loc_lines =0
        line = f.readline()
        while line:
            #print line                                                                                                                                                                                                                                                                                                       
            rec = loads(line)
            tot_lines += 1
            condition = parallels.bdCheckCondition_keywords(rec,parallels.sel_cities)
            if condition:
                parallels.bdDoSomething_keywords(rec,locs,parallels.keywords)
                loc_lines += 1
                if (loc_lines%1000==0):
                    logger.log('Count:' + str(loc_lines) + '/' + str(tot_lines))
            line = f.readline()
        ret = {'fname':f.name,'tot_lines': tot_lines, 'loc_lines': loc_lines}
        logger.log('Writing json to file: ' + outfilep)
        f = open(outfilep,'wb')
        f.write(dumps(locs))
        del locs
        return ret

print 'starting now..'
starttime = datetime.now()
res = processFile.map(input_files)
print 'time taken= '+ str(datetime.now()-starttime)
