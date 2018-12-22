import os
from pymediainfo import MediaInfo
import configparser
import ast
import time
import pathlib
def getvcodec(filename):
    media_info = MediaInfo.parse(filename)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            return(track.format)
    return(False)
def getcolor(filename):
    media_info = MediaInfo.parse(filename)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            return(track.color_primaries)
    return(False)
def getbit(filename):
    media_info = MediaInfo.parse(filename)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            return(track.Bit_depth)
    return(False)
def getacodec(filename):
    media_info = MediaInfo.parse(filename)
    for track in media_info.tracks:
        if track.track_type == 'Aduio':
            return(track.format)
    return(False)
def getoptivcodec(codec, hq):
    if codec == False:
        return(False)
    elif codec.lower().replace("-", "") == "vc1":
        #vc1 encoding is not supported by ffmpeg so codec is changed to h.264
        retunr('libx264')
    elif codec.lower().replace("-", "") in "wmv":
        #upgrades codec to wmv3 if wmv1/2 who wants to use outdated codecs anyway
        return('wmv3')
    elif codec.lower().replace("-", "") == "mpeg4":
        return('libxvid')
    elif codec.lower().replace("-", "") == "msmpeg4" or codec.lower().replace("-", "") == "msmpeg4v1" or codec.lower().replace("-", "") == "msmpeg4v2" or codec.lower().replace("-", "") == "msmpeg4v3":
        #Should encode to msmpeg4v3 there is no standalose encoder for V2 and V1 can not be encoded
        return('msmpeg4')
    elif codec.lower().replace("-", "") == "h264" or codec.lower().replace("-", "") == "avc" or codec.lower().replace("-", "") == "h264":
        return('libx264')
    elif codec.lower().replace("-", "") == "hvec" or codec.lower().replace("-", "") == "h265" or codec.lower().replace("-", "") == "h.265":
        return('libx265')
    elif codec.lower().replace("-", "") == "mpeg2" or codec.lower().replace("-", "") == "mpeg2video":
        return('mpeg2video')
    elif codec.lower().replace("-", "") == "vp9":
        return('libvpx-vp9')
    else:
        #h.264 is a good fallback
        if hq == True:
            return('libx265')
        return('libx264')
def getoptiacodec(codec, hq):
    if codec == False:
        return(False)
    elif codec.lower().replace("-", "") == "aac" or codec.lower().replace("-", "") == "aaclc":
        #if compiled with non free libfdk_aac is the best aac encoder
        if getconfig(nonfree) == True:
            return('libfdk_aac')
        return('aac')
    elif codec.lower().replace("-", "") == "heaac":
        #if compiled with non free libfdk_aac is the best aac encoder
        if getconfig(nonfree) == True:
            return('libfdk_aac')
        return('libaacplus')
    elif codec.lower().replace("-", "") == "eac3":
        return('eac3')
    elif codec.lower().replace("-", "") == "flac":
        return('flac audio.flac')
    elif codec.lower().replace("-", "") == "mp3":
        return('libmp3lame')
    elif codec.lower().replace("-", "") == "mp2":
        return('libtwolame')
    elif codec.lower().replace("-", "") == "ac3":
        return('ac3')
    elif codec.lower().replace("-", "") == "wmav2":
        return('wmav2')
    elif codec.lower().replace("-", "") == "alac":
        return('flac')
    elif codec.lower().replace("-", "") == "opus":
        return('libopus')
    else:
        #aac is a goodfallback
        if hq == True:
            return('libopus')
        if getconfig(nonfree) == True:
            return('libfdk_aac')
        return('aac')
def getconfig(info):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return(config['settings'][info])

def listgen(info):
    output = ['']
    output = ast.literal_eval(getconfig(info))
    output = [n.strip() for n in output]
    return(output)

def isVideo(file):
    filename, ext = file.split('.')
    if ext in listgen('videoext'):
        print("Video")
        return(True)
    print(listgen(getconfig(videoext)))
    print(ext)
    print("!video")
    return(False)

def isHDR(filename):
    global codec
    isHDR = False
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
did = False
number = 0
done = ['']
for path, subdirs, files in os.walk(getconfig('path')):
    for name in files:

        currentfile = '{}\\{}'.format(path, name)
        if currentfile in done:
            break
        done.append(currentfile)
        print(currentfile)
        filename, fileext = currentfile.split('.')
        print("Testing {}". format(currentfile))
        if isVideo(currentfile) == True:
            print('Currentfile is a video')
            if isHDR(currentfile) == True:
                did = True
                number = number + 1
                os.system ('ffmpeg -i "{}" -vf zscale=transfer=linear,tonemap=tonemap=hable:param=1.0:desat=0:peak=10,zscale=transfer=bt709,format=yuv420p -c:v {} -c:a {} "{}"'.format(currentfile, getoptivcodec(getvcodec(currentfile), getconfig('hq')), getoptiacodec(getacodec(currentfile), getconfig('hq')), filename + "tmp." + fileext))
                os.rename(currentfile, currentfile + ".bak")
                os.rename(filename + "tmp2." + fileext, currentfile)
if did == True:
    print('Tone Maped {} Files'.format())
elif did == False:
    print('Did not find any files to tone map')
else:
    print("I Dont feel so good Mr. Stark....")
