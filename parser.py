# First version of a parser that will convert a sdf file to a tcx file
# To enable to easy move suunto group files into endomondo or other apps

from sys import argv
from datetime import datetime, date , time, timedelta
import re
from tcxWriter import *
from HeartBeats import *
from parsermodule import *


    pass
     
def creatTimestamp():
    # Takes times in seconds and converts to HH:MM:SS and mabye more
    # Returns a string with the prober timestamp
     return timestamp

def main():

    script,insource, outsource , exportsource = argv
    infile = open(insource,'r')
    outfile = open(outsource,'w')
    exportfile = open(exportsource,'w')
    line_count = 0
    workoutTime = 0
    raw_bpm = []
    # Idea to rewrie so that the parser is a standalone lib that can be used with the haxed fit to tcx parser found on github..

    
    parsed = parseSDF(infile,raw_bpm)
    print parsed
    start_time = parsed[1]
    workoutTime = int(parsed[0])
    workoutDate = datetime.strptime(start_time, "%d.%m.%Y %H:%M:%S")
    av_bpm, doubles = creatAveragedBeats(raw_bpm)
    print "\n The file consists of %d lines" % line_count
    print "and %d of those lines are heartbeats" %len(raw_bpm)
    print "Averaged bpm list have the length of %d " % len(av_bpm)
    #print av_bpm
    print len(doubles)
    print "The workout started at %s and the duration was " %start_time
    print workoutDate.date()
    print workoutDate.time()
    setupFile(outfile,workoutDate,workoutTime)
    #newTrackpoint(workoutDate,outfile,'125')
    #newTrackpoint(workoutDate+newb,outfile,'145')
    writeBPMs(outfile,raw_bpm,doubles,workoutDate,workoutTime)
    setupFileEnd(outfile)
    outfile.close
    exportBeats(exportfile,raw_bpm,workoutTime)
    exportfile.close
    
if __name__ == "__main__":
	main()
