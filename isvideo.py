import os
from pymediainfo import MediaInfo
from getmediainfo import *
from ishdr import *
from configutil import *
import configparser
import ast
def isvideo(file):
    filename, ext = file.split('.')
    if ext in listgen(getconfig(videoext)):
        print("Video")
        return(True)
    print(listgen(getconfig(videoext)))
    print(ext)
    print("!video")
    return(False)
