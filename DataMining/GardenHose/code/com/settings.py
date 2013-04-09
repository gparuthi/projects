import run_modules

LOG_PATH_DIR = '../../logs/'
INPUT_DIR = '../../data/olympics_opening/'
OUTPUT_DIR = '../../output/'
FILE_TYPE = '.data'
keywords = ['olympics', 'opening']

CheckCondition = run_modules.bdCheckCondition_select_keywords
DoSomething = run_modules.bdDoSomethingMemory