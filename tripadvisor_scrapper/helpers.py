import os
import re

def only_numbers(s):
    return re.sub("[^0-9]","",s)

def str_to_float(s):
    try:
        return float(s.replace(",","."))
    except:
        return None

def str_to_int(s):
    try:
        return int(only_numbers(s))
    except:
        return None

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))