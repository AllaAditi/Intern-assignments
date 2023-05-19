from configparser import ConfigParser
import sys

try:
    config = ConfigParser()
    config.read("configuration/application.conf")
except Exception as e:
    print(f"Error while loading the config: {e}")
    print("Failed to Load Configuration. Exiting!!!")
    sys.stdout.flush()
    sys.exit()


class APis:
    view_all_items_api = '/view_all'
    create_api = '/items/'
    update_api = '/items/{items_id}'
    delete_api = '/delete/{items_id}'
    send_email = '/send_email'
    get_api = '/billing-price'


class DBConf:
    MONGO_URI = config.get("MONGO_DB", "M_uri")
    if not MONGO_URI:
        print("Error, environment variable MONGO_URI not set")
        sys.exit(1)
