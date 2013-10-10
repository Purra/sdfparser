# Module for parsing sdf files into a array with all the heartbeats values. Also gets starttime duration and some other nifty stuff from the file. 
# All code is free to use for anyone that wants
import re
def parseSDF(infile,raw_bpm):
    #infile = open(insource,'r')
    line_count = 0
    workoutTime = 0
    
    start_time = ''
    #raw_bpm = []
    while 1:
        lines = file.readlines(infile)
        if not lines:
            break
        for line in lines:
            if re.match('^STARTTIME',line):
                m2 = re.split('=|\r|\n',line)
                start_time = m2[1]
            if re.match('^"MONITORLOG"', line): 
                m = re.split(',|\r|\n',line)
                raw_bpm.append(int(m[1]))
            if re.match('^DURATION',line):
                m3 = re.split('=|\r|\n',line)
                workoutTime = m3[1]
            else:
                line_count = line_count + 1
                #print line

    infile.close
    return workoutTime,start_time
