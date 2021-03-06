import os.path
from collections import OrderedDict

# SEGMENTS DURATION (seconds)
SEGMENT_SIZE = 7

# FFMPEG PRESET [ultrafast,superfast, veryfast, faster, fast, medium, slow, slower, veryslow]
FFMPEG_PRESET = 'slow'

# PRESETS FOR ADAPTATIVE QUALITY
PROFILES = OrderedDict()
PROFILES['0-ugly'] = {
    'resolutions':  { '4/3': '400x300', '16/9': '416x234' },
    'audiobitrate': '64k',
    'videobitrate': '100k',
    'buffersize':   '200k',
    'profile':      'baseline',
    'level':        '3.0',
    'fps':          10
}
PROFILES['1-bad'] = {
    'resolutions':  { '4/3': '400x300', '16/9': '416x234' },
    'audiobitrate': '64k',
    'videobitrate': '200k',
    'buffersize':   '400k',
    'profile':      'baseline',
    'level':        '3.0',
    'fps':          15
}
PROFILES['2-poor'] = {
    'resolutions':  { '4/3': '480x360', '16/9': '480x270' },
    'audiobitrate': '64k',
    'videobitrate': '400k',
    'buffersize':   '800k',
    'profile':      'baseline',
    'level':        '3.0',
    'fps':          15
}
PROFILES['3-low'] = {
    'resolutions':  { '4/3': '640x480', '16/9': '640x360' },
    'audiobitrate': '96k',
    'videobitrate': '600k',
    'buffersize':   '1200k',
    'profile':      'baseline',
    'level':        '3.0',
    'fps':          24
}
PROFILES['4-medium'] = {
    'resolutions':  { '4/3': '640x480', '16/9': '640x360' },
    'audiobitrate': '96k',
    'videobitrate': '1200k',
    'buffersize':   '2400k',
    'profile':      'baseline',
    'level':        '3.1',
    'fps':          24
}
PROFILES['5-high'] = {
    'resolutions':  { '4/3': '960x720', '16/9': '960x540' },
    'audiobitrate': '128k',
    'videobitrate': '3500k',
    'buffersize':   '7000k',
    'profile':      'main',
    'level':        '3.1',
    'fps':          25
}
PROFILES['6-hd'] = {
    'resolutions':  { '4/3': '1280x960', '16/9': '1280x720' },
    'audiobitrate': '128k',
    'videobitrate': '5000k',
    'buffersize':   '10000k',
    'profile':      'main',
    'level':        '3.1',
    'fps':          25
}
PROFILES['7-fullhd'] = {
    'resolutions':  { '4/3': '1920x1440', '16/9': '1920x1080' },
    'audiobitrate': '256k',
    'videobitrate': '7000k',
    'buffersize':   '10000k',
    'profile':      'main',
    'level':        '4',
    'fps':          25
}

def build(inputfile, ratio='16/9', segmentsize=False, ffmpegmode=False):
    presets = PROFILES.copy()
    for quality, profile in presets.items():
        try:
            presets[quality]['resolution'] = profile['resolutions'][ratio]
            presets[quality]['gop'] = presets[quality]['fps'] * SEGMENT_SIZE
            presets[quality]['inputfile'] = inputfile
            presets[quality]['outputname'] = quality
            presets[quality]['segmentsize'] = segmentsize if segmentsize else SEGMENT_SIZE
            presets[quality]['ffmpegmode'] = ffmpegmode if ffmpegmode else FFMPEG_PRESET
        except Exception as e:
            print 'Error while building {0} Profile with ratio {1}.. Ignoring'.format(quality, ratio)
            del presets[quality]

    return presets.items()
