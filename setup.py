import os, setuptools

SETUP_OUTPUT_CSV  = './resources/output/csv'
SETUP_OUTPUT_XLS  = './resources/output/xls'
SETUP_OUTPUT_JSON = './resources/output/json'

SETUP_LOGS_APP = './resources/logs/app-logs'
SETUP_LOGS_DB  = './resources/logs/db-logs'

SETUP_DATABASE = './resources/database'
SETUP_CONFIG   = './resources/config'
SETUP_TEMP     = './resources/temp'

def main():
    try:
        os.makedirs(SETUP_OUTPUT_CSV)
        os.makedirs(SETUP_OUTPUT_XLS)
        os.makedirs(SETUP_OUTPUT_JSON)

        os.makedirs(SETUP_LOGS_APP)
        os.makedirs(SETUP_LOGS_DB)

        os.makedirs(SETUP_DATABASE)
        os.makedirs(SETUP_CONFIG)
        os.makedirs(SETUP_TEMP)

    except OSError:
        print('creating of directory failed...')

main()