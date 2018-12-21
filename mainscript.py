
#By Bud Gidiere
import os
from pymediainfo import MediaInfo
os.environ['PATH'] = os.path.dirname('C:/Users/Bud Gidiere/Documents/ffmpegproject/Mediainfo.dll') + ';' + os.environ['PATH']
#Options
filename = ""

def isHDR(filename):
    global codec
    isHDR = "false"
    if isvideo(filename) == True:
        media_info = MediaInfo.parse(filename)
        for track in media_info.tracks:
            if track.track_type == 'Video':
                isHDR = track.color_primaries
                codec = track.codec
                print(isHDR)
        try:
            if "BT.2020" in isHDR:
                print("{} uses BT.2020 color space and needs to be tone maped.".format(filename))
                return(True)
        except:
            print("Warning No color_primaries String in {}".format(filename))
        print("File {} is not an HDR Video, Does not use the BT.2020 color space, or has already been converted".format(filename))
        return(False)
    else:
        print("File {} is not a video".format(filename))
        return(False)

#isHDR = subprocess.call(['mediainfo', '{}.mkv'.format(filename), '--Inform="Video;%colour_primaries%"'])
#isHDR = commands.getoutput('mediainfo {}.mkv --Inform="Video;%colour_primaries%"'.format(filename))
#isHDRout = subprocess.Popen(['mediainfo', '{}.mkv'.format(filename), '--Inform="Video;%colour_primaries%"'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#stout,stderr = isHDRout.communicate()
for currentfile in os.listdir('.'):
    if isHDR(currentfile) == True:
        name, extension  = currentfile.split('.')
        print("Tone Mapping {}".format(currentfile))
        os.system('ffmpeg.exe  -i "{}" '.format(currentfile) + '-vf "format=p010,hwupload,tonemap_opencl=t=bt2020:tonemap=linear:format=p010,hwdownload,format=p010" "{}"'.format(name + "tmp." + extension))
        os.system('ffmpeg.exe  -i "{}" '.format(name + "tmp." + extension) + '-vf zscale=transfer=linear,tonemap=tonemap=hable:param=1.0:desat=0:peak=10,zscale=transfer=bt709,format=yuv420p "{}"'.format(name + "tmp2." + extension))
        print("Finished Tone Mapping {} deleting orignail file and remaing {} to {} ".format(currentfile, name + "tmp2." + extension, currentfile))
        #os.remove(name + "tmp." + extension)
        #os.remove(currentfile)
        #os.rename(name + "tmp2." + extension, currentfile)
