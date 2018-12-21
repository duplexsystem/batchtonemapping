import os
from pymediainfo import MediaInfo
from getmediainfo import *
from isvideo import *
from ffmpeg import *
from configutil import *
import configparser
import ast
def isHDR(filename):
    global codec
    isHDR = "false"
    if isvideo(filename) == True:
        color = getcolor(filename)
        bit = getbit(filename)
        try:
            if "BT.2020" in color:
                print("{} uses BT.2020 color space and is HDR.".format(filename))
                return(True)
        except:
            print("Warning No color_primaries String in {}".format(filename))
        try:
            if "10" in bit:
                print("{} uses 10 bit color and is HDR.".format(filename))
                return(True)
        except:
            print("Warning No bit_depth String in {}".format(filename))
        print("File {} is not an HDR Video, Does not use the BT.2020 color space, or has already been converted".format(filename))
        return(False)
    else:
        print("File {} is not a video".format(filename))
        return(False)
