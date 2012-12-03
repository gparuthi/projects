from datetime import datetime

start_time = datetime.now()

LOGFILE_PATH = '/Users/gaurav/Documents/Work/Projects/DataMining/logs/' + 'CityData.'+str(datetime.now())+'.log'
LOGFILE = open(LOGFILE_PATH,'w')

def log(log_str):
    print '[' + str(datetime.now()) +'] '+ str(log_str)
    LOGFILE.write('[' + str(datetime.now()) +'] '+ str(log_str) + '\n')

def log_file_stats(fname, tot_lines, loc_lines):
    now_time = datetime.now()
    log('File Stats for: ' + fname)
    log('Total time taken: ' + str((now_time-start_time).seconds))
    log('Total number of lines found = ' + str(tot_lines))
    log('Total number of lines With location = ' + str(loc_lines))

def log_final_stats(res):
    log ('----------------------------------------------------------------------')
    log ('Final results:' + str(res))
    tot_lines = 0
    loc_lines_del = 0
    loc_lines_ny = 0
    for r in res:
        tot_lines += r['tot_lines']
        loc_lines_del += r['loc_lines_del']
        loc_lines_ny += r['loc_lines_ny']

    log ('Total Lines found: ' + str (tot_lines))
    log ('Total delhi lines with coordinates: ' +  str(loc_lines_del))
    log ('Total ny lines with coordinates: ' +  str(loc_lines_ny))
    log ('----------------------------------------------------------------------')
    #LOGFILE.close()
