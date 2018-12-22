# Batch HDR -> SDR Tone Mapping

- Do you have 1 or more HDR video files that you want tone mapped?
  - Batch Tone Mapper can help you!
- Do you need a fast and simple python script that is built on top of ffmpeg and can support virtually any format?
  - Batch Tone Mapper can help you!
- Do you need a place to rant about your life problems and current dilemmas?
  - You’re on your own buddy!
  
Batch Tone Mapper is a fast+ python script that can tone map an unlimited++ number of files from HDR to SDR. Because it is built on top of ffmpeg it can support any virtually format+++!

# Installation 

- Download Batch Tone Mapper (if you need help with this, you probably shouldn’t be tone mapping files anyway)

- Download ffmpeg. You have two options:
    - Download the latest build from here (Recommended for people with little time or technical knowledge): https://www.ffmpeg.org/download.html#build-windows
    - Compile your own Non-Free build using the ffmpeg source code (This is Recommended if you have time and technical knowledge. This is because in some cases it delivers better quality): https://trac.ffmpeg.org/wiki/CompilationGuide
- Copy only ffmpeg.exe (and any external libraries if you compiled your own build) into a folder with the rest of the files

- Download Media info 
    - Windows. https://mediaarea.net/en/MediaInfo/Download/Windows
        - You must download the DLL WITHOUT installer (note: architecture is your python version not necessarily your system architecture)
        
    - Linux. Someone is going to have to figure this out because I don’t have a Linux machine to test this on (I know I could use a virtual machine but I am lazy)
    
    - MacOS.
        - Really?
# Configuration

You need to make a config.ini file
Sample:
```
[settings]
videoext = ['asf','avi','mov','mp4','mpegts','ts','mkv','wmv']
hwaccel = False
nonfree = False
hq = False
deleteorig = False
path =  (File Path to Scan for tone mapping)
```
videoext: These are the extensions that will be counted as video files

hwaccel: This enable/disables Hardware acceleration support which does not exist yet, but is planned (good to leave as False to prevent future errors)

nonfree: Set this to true if you compiled your own non-free version of ffmepg: otherwise, leave it false.

hq: Enable this if you want higher quality codec fallbacks

deleteorig: Enable this if you want the file to be deleted after completion !WARNING! IF THERE IS A FAILURE TONE MAPPING THE FILE, THE ORIGNAIL FILE WILL STILL BE DELETED!

path: Folder you want to be tone mapped

# Disclaimers and licensing stuff

This product uses MediaInfo library, Copyright (c) 2002-2018 MediaArea.net SARL.

This software uses code of <a href=http://ffmpeg.org>FFmpeg</a> licensed under the <a href=http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>LGPLv2.1</a>

[+] Possible furious
[+|+] Limited to 9,223,372,036,854,775,807 on 64 bit, and 2,147,483,647 on 32 Bit Systems
[+|+|+] Supports These Formats++++: https://ffmpeg.org/general.html#Supported-File-Formats_002c-Codecs-or-Features
[+|+|+|+] Not All formats are supported
