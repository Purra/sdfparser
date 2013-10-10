# Module that does the bpm calculations
def creatAveragedBeats(raw_bpm):
    # Function that makes an structure with the averaged bpm and the timestamp for the recorded bpm
    j = 1
    bpm_prev = 0
    counter = 0
    doubles = []
    average = []
    for bpm in raw_bpm:
        if bpm != bpm_prev:
            average.append(bpm)
            doubles.append(counter)
            counter = 0;
            #print "blupp %d" %raw_bpm[j-1]
        else:
             counter = counter + 1
        j = j + 1
        #print bpm , bpm_prev
        bpm_prev = bpm
    return average,doubles
