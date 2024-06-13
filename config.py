import yaml
from pprint import pprint

with open('conf.yaml') as f:
    templates = yaml.safe_load(f)