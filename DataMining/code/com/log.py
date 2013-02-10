from datetime import datetime

class logger(object):
    def __init__(self, fname):
        self.start_time = datetime.now()
        self.LOGFILE_PATH = '/Users/gaurav/Documents/Work/Projects/DataMining/logs/' + fname + '.' + str(datetime.now()) + '.log'
        self.LOGFILE = open(self.LOGFILE_PATH, 'w')
        print 'logfile initiated at : ' + self.LOGFILE_PATH

    def log(self,log_str):
        print '[' + str(datetime.now()) + '] ' + str(log_str)
        self.LOGFILE.write('[' + str(datetime.now()) + '] ' + str(log_str) + '\n')
        self.LOGFILE.flush()

    def log_file_stats(self,fname, tot_lines, loc_lines):
        now_time = datetime.now()
        self.log('File Stats for: ' + fname)
        self.log('Total time taken: ' + str((now_time - start_time).seconds))
        self.log('Total number of lines found = ' + str(tot_lines))
        self.log('Total number of lines With location = ' + str(loc_lines))

    def log_final_stats(self,res):
        self.log ('----------------------------------------------------------------------')
        self.log ('Final results:' + str(res))
        tot_lines = 0
        loc_lines_del = 0
        loc_lines_ny = 0
        for r in res:
            tot_lines += r['tot_lines']
            loc_lines_del += r['loc_lines_del']
            loc_lines_ny += r['loc_lines_ny']

        self.log ('Total Lines found: ' + str (tot_lines))
        self.log ('Total delhi lines with coordinates: ' + str(loc_lines_del))
        self.log ('Total ny lines with coordinates: ' + str(loc_lines_ny))
        self.log ('----------------------------------------------------------------------')
#LOGFILE.close()   


