import os
from pymediainfo import MediaInfo
from getmediainfo import *
from isvideo import *
from ishdr import *
from configutil import *
import configparser
import ast
def ffmpeg(input, varugment, aarugment, output, vcodec, acodec):
    aarugments = ''
    varugments = ''
    for args in aarugment:
        if aarugments == '':
            aarugments = aarugments + "{}".format(args)
        else:
            aarugments = aarugments + ",{}".format(args)
    for args in varugment:
        if varugments == '':
            varugments = varugments + "{}".format(args)
        else:
            varugments = varugments + ",{}".format(args)
    if varugment and aarugment and vcodec and acodec != False:
        print("ffmpeg -I {} -vf {} -af {} -c:v {} -c:a {} {}".format(input, varugments, aarugments, vcodec, acodec, output))
    elif varugment and vcodec and acodec != False:
        print("ffmpeg -I {} -vf {} -c:v {} -c:a {} {}".format(input, varugments, vcodec, acodec, output))
    elif aarugment and vcodec and acodec != False:
        print("ffmpeg -I {} -af {} -c:v {} -c:a {} {}".format(input, aarugments, vcodec, acodec, output))
    elif varugment and aarugment and vcodec != False:
        print("ffmpeg -I {} -vf {} -af {} -c:v {} {}".format(input, varugments, aarugments, vcodec, output))
    elif varugment and vcodec != False:
        print("ffmpeg -I {} -vf {} -c:v {} {}".format(input, varugments, vcodec, output))
    elif aarugment and vcodec != False:
        print("ffmpeg -I {} -af {} -c:v {} {}".format(input, aarugments, vcodec, output))
    elif varugment and aarugment and acodec != False:
        print("ffmpeg -I {} -vf {} -af {} -c:a {} {}".format(input, varugments, aarugments, acodec, output))
    elif varugment and acodec != False:
        print("ffmpeg -I {} -vf {} -c:a {} {}".format(input, varugments, acodec, output))
    elif aarugment and acodec != False:
        print("ffmpeg -I {} -af {} -c:a {} {}".format(input, aarugments, acodec, output))
    elif varugment and aarugment != False:
        print("ffmpeg -I {} -vf {} -af {} {}".format(input, varugments, aarugments, output))
    elif varugment != False:
        print("ffmpeg -I {} -vf {} {}".format(input, varugments, output))
    elif aarugment != False:
        print("ffmpeg -I {} -af {} {}".format(input, aarugments, output))
    else:
        print("error no ons given")
