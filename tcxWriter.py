# File writing module
from datetime import date, time , timedelta , datetime
import math
# Function that writes the current pulsestamp to the output file
# takes a pulse value (could be averaged ) and a timestamp needs the filestream also

def newTrackpoint(currentTime, outfile,bpm):
     outfile.write("\t  <Trackpoint>\n")
     outfile.write("\t   <Time>%sT%sZ\</Time>\n" % (currentTime.date(), currentTime.time()))
     outfile.write("\t   <DistanceMeters>0.0000000</DistanceMeters>\n")
     outfile.write("\t   <HeartRateBpm xsi:type=\"HeartRateInBeatsPerMinute_t\">\n")
     outfile.write("\t     <Value>%d</Value>\n" %bpm)
     outfile.write("\t   </HeartRateBpm>\n")
     outfile.write("\t   <SensorState>Absent</SensorState>\n")
     outfile.write("\t  </Trackpoint>\n")
     return 0

def setupFile(outfile,startTime,totalTime):
     #Function that fixes the first lines of the file
     #Still needing the writing of average pulses and max pulse 
     outfile.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\" ?>\n")
     outfile.write("<TrainingCenterDatabase xmlns=\"http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.garmin.com/xmlschemas/ActivityExtension/v2 http://www.garmin.com/xmlschemas/ActivityExtensionv2.xsd http://www.garmin.com/xmlschemas/FatCalories/v1 http://www.garmin.com/xmlschemas/fatcalorieextensionv1.xsd http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd\">\n\n")
     outfile.write("  <Folders/>\n\n")
     outfile.write("  <Activities>\n")
     outfile.write("    <Activity Sport=\"Running\">\n")
     outfile.write("       <Id>%sT%sZ</Id>\n" % (startTime.date(), startTime.time()))
     outfile.write("       <Lap StartTime=\"%sT%sZ\">\n" % (startTime.date(), startTime.time()))
     outfile.write("\t  <TotalTimeSeconds>%d</TotalTimeSeconds>\n" % totalTime)
     outfile.write("\t  <DistanceMeters>0.0000000</DistanceMeters>\n")
     outfile.write("\t  <MaximumSpeed>0.0000000</MaximumSpeed>\n")
     outfile.write("\t  <Calories>0</Calories>\n")
     outfile.write("\t  <AverageHeartRateBpm xsi:type=\"HeartRateInBeatsPerMinute_t\">\n\t    <Value>145</Value>\n\t  </AverageHeartRateBpm>\n")
     outfile.write("\t  <MaximumHeartRateBpm xsi:type=\"HeartRateInBeatsPerMinute_t\">\n\t    <Value>175</Value>\n\t   </MaximumHeartRateBpm>\n")
     outfile.write("\t  <Intensity>Active</Intensity>\n")
     outfile.write("\t  <TriggerMethod>Manual</TriggerMethod>\n")
     outfile.write("\t  <Track>\n")

def writeBPMs(outfile,bpm,doubles,workoutdate,totalTime):
     timestep = timedelta(milliseconds = 1000*math.ceil((float(len(bpm))/totalTime)))
     for beat in bpm:
          newTrackpoint(workoutdate,outfile,beat)
          workoutdate = workoutdate +  timestep



def setupFileEnd(outfile):
     #This writes the end of the file more to go like device info and other worthless shit
     outfile.write("\t</Track>\n")
     outfile.write("      </Lap>\n")
     outfile.write("    </Activity>\n")
     outfile.write("  </Activities>\n")
     outfile.write("  <Workouts/>\n")
     outfile.write("  <Courses/>\n")
     outfile.write("</TrainingCenterDatabase>")

def exportBeats(outfile,bpm,totalTime):
     timestep = 1000*math.ceil((float(len(bpm))/totalTime))
     outfile.write("%d\n" %totalTime)
     for beat in bpm:
          outfile.write("%d \n" %beat)
          
