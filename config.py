import yaml
from pprint import pprint

with open('config.yaml') as f:
    templates = yaml.safe_load(f)