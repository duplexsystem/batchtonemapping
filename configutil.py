import os
from pymediainfo import MediaInfo
from getmediainfo import *
from isvideo import *
from ishdr import *
import configparser
import ast
def getconfig(info):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return(config['settings'][info])
def listgen(info):
    output = ['']
    output = ast.literal_eval(getconfig(info))
    output = [n.strip() for n in output]
    return(output)
