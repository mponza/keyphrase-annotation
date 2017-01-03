import os
import json

main_base = os.path.dirname(__file__)
conf_path = os.path.join(main_base, '../configuration.json')
CONFIG = json.load(open(conf_path, 'r'))