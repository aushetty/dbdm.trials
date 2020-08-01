from flask import Flask
from pathlib import Path
import sys
import configparser
import os 

# const_config_file = Path(os.environ.get('config_file' , '/etc/config/config.ini'))

const_config_file = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'config.ini')

const_conn_type_cos = r'MONGODB'



def get_credentials():
    parser = configparser.ConfigParser()
    parser.read(const_config_file)


    section = const_conn_type_cos

    try:
        mongodb_url = parser.get(section, 'MONGODB_URL')
    except (configparser.NoOptionError, configparser.NoSectionError) as e:
        msg = "No MongoDB URL in MongoDB Configuration {}".format(e)
        return False
    try:
        mongodb_name = parser.get(section, 'MONGODB_NAME')
    except (configparser.NoOptionError, configparser.NoSectionError) as e:
        msg = "No MongoDB Name in MongoDB Configuration {}".format(e)
        return False
    try:
        mongodb_tbl_coll_name = parser.get(section, 'MONGODB_TBL_COLL_NAME')
    except (configparser.NoOptionError, configparser.NoSectionError) as e:
        msg = "No MongoDB Table Column Name in MongoDB Configuration {}".format(e)
        return False
    else:
        return mongodb_url, mongodb_name, mongodb_tbl_coll_name






    # process_key = parser.get(proc_extract , 'API_KEY')
    # sub_process_key = parser.get(sub_proc_extract , 'API_KEY')

    # process_key = os.environ['API_KEY_MAIN']
    # process_key = os.getenv("API_KEY_MAIN")

    # sub_process_key = os.environ['API_KEY_SUB']
    # sub_process_key = os.getenv("API_KEY_SUB")


    # print (process_key , sub_process_key)
    # return (process_key, sub_process_key)





# name_arg = sys.argv[1]

# @app.route("/")
def execute():

    if get_credentials():
        print(get_credentials()[2])

        

        if get_credentials()[2] == 'autoClassification':
            print ('Hi {} , welcome to test'.format('abhi'))

        else:
            print ('This is a error')    
        
        
        
    





if __name__ == '__main__':

    # app.run(debug=True)
    execute()
    # get_credentials()
