from IPython import parallel
from datetime import datetime
import log, parallels, settings, helpers
import os

rc= parallel.Client()

lview = rc.load_balanced_view() 

lview.block = True

@lview.parallel()
def processFile(filep):
        import log, parallels, helpers, settings
        import os
        from ujson import loads
        import gzip

        locs = {}
        logger = log.logger('test/AllLocsBigData_'+os.path.basename(filep))
        
        try:
            # f = open(filep)
            f = open(filep)
            logger.log( 'finding all records with location for: ' + f.name)
            tot_lines =0
            loc_lines =0
            line = f.readline()
            while line:
                #print line                                                                                               
                rec = loads(line)
                tot_lines += 1
                condition = parallels.bdCheckCondition(rec)
                if condition:
                    parallels.bdDoSomethingMemory(rec,locs)
                    loc_lines += 1
                    if (loc_lines%10000==0):
                        logger.log('Count:' + str(loc_lines) + '/' + str(tot_lines))
                line = f.readline()
            ret = {'fname':f.name,'tot_lines': tot_lines, 'loc_lines': loc_lines}
            logger.send_final_stats(ret)
        except Exception as e:
            logger.log('Error log: ' + str(e))
        # write results to file
        logger.log('Sending to files now..')
        try:
            helpers.write_all_locs_to_file([locs],settings.OUTPUT_DIR)
        except Exception as e:
            logger.log('Error log: ' + str(e))
        logger.log('Done!')    
        return locs

input_files = helpers.GetInputFiles(settings.INPUT_DIR, '.data')
print 'starting now..'
starttime = datetime.now()
res = processFile.map(input_files)
print 'time taken= '+ str(datetime.now()-starttime)