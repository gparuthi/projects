from datetime import datetime
from DataMining.code.com import settings
# import redis

DM_OBSERVER_CH = 'dm_observer'

class logger(object):
    def __init__(self, fname):
        self.start_time = datetime.now()
        self.LOGFILE_PATH = settings.LOG_PATH_DIR + fname + '.' + str(datetime.now()) + '.log'
        self.LOGFILE = open(self.LOGFILE_PATH, 'w')
        # self.rc = redis.Redis(host='gauravparuthi.com', port=6379, db=1)
        print 'logfile initiated at : ' + self.LOGFILE_PATH

    def log(self,log_str):
        print '[' + str(datetime.now()) + '] ' + str(log_str)
        self.LOGFILE.write('[' + str(datetime.now()) + '] ' + str(log_str) + '\n')
        self.rc.publish(DM_OBSERVER_CH, log_str)
        self.LOGFILE.flush()

    def log_file_stats(self,fname, tot_lines, loc_lines):
        now_time = datetime.now()
        self.log('File Stats for: ' + fname)
        self.log('Total time taken: ' + str((now_time - start_time).seconds))
        self.log('Total number of lines found = ' + str(tot_lines))
        self.log('Total number of lines With location = ' + str(loc_lines))

    def send_final_stats(self, ret):
        # publish to our redis server that its done
        self.rc.publish(DM_OBSERVER_CH, ret)
        



    # def log_final_stats(self,res):
    #     self.log ('----------------------------------------------------------------------')
    #     self.log ('Final results:' + str(res))
    #     tot_lines = 0
    #     loc_lines_del = 0
    #     loc_lines_ny = 0
    #     for r in res:
    #         tot_lines += r['tot_lines']
    #         loc_lines_del += r['loc_lines_del']
    #         loc_lines_ny += r['loc_lines_ny']

    #     self.log ('Total Lines found: ' + str (tot_lines))
    #     self.log ('Total delhi lines with coordinates: ' + str(loc_lines_del))
    #     self.log ('Total ny lines with coordinates: ' + str(loc_lines_ny))
    #     self.log ('----------------------------------------------------------------------')
#LOGFILE.close()   


