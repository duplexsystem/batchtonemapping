import os
from pymediainfo import MediaInfo
from getmediainfo import *
from isvideo import *
from ishdr import *
from configutil import *
import configparser
import ast
import time
import pathlib
for path, subdirs, files in os.walk(getconfig('path')):
    for name in files:
        currentfile = pathlib.PurePath(path, name)
        filename, fileext = currentfile.split('.')
        if isvideo(currentfile) == True:
            if ishdr(currentfile) == True:
                os.system ('ffmpeg.exe  -i {} -vf zscale=transfer=linear,tonemap=tonemap=hable:param=1.0:desat=0:peak=10,zscale=transfer=bt709,format=yuv420p -c:v {} -c:a {} {}'.format(currentfile, getoptivcodec(getvcodec(currentfile)), getoptiacodec(getacodec(currentfile)), name + "tmp2." + extension))
