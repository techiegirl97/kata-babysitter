def calculate(start,stop,bed):
    #import the needed libraries
    import math
    import re
    
    #This is an array representing a full/maximum work night.
    #strategy: calculate position minus position to get hours
    timescale = [5,6,7,8,9,10,11,12,1,2,3,4]
    
    #check the variable and handle int, float or strings types    
    if type(start) is int:
        sta = timescale.index(start)
    elif type(start) is float:
        sta = timescale.index(round(start))
        print("startime index:",sta)
    elif type(start) is str:
        #filter out special char and letters
        filterStart = re.search('[0-9]+', start).group()
        print(type(filterStart))
        
        numStart = int(filterStart)
        print(type(numStart))
        
        sta = timescale.index(numStart)
    
    if type(stop) is int:
        sto = timescale.index(stop)
    elif type(stop) is float:
        sto = timescale.index(round(stop))
        print("stoptime index:",sto)
    elif type(stop) is str:
        filterStop = re.search('[0-9]+', stop).group()
        numStop = int(filterStop)
        sto = timescale.index(numStop)
    
    if type(bed) is int:
        bed = timescale.index(bed)
    elif type(bed) is float:
        bed = timescale.index(round(bed))
        print("bedtime index:",bed)
    elif type(bed) is str:
        filterBed = re.search('[0-9]+', bed).group()
        numBed = int(filterBed)
        bed = timescale.index(numBed)
    
	#the first time block
	#calculate the hours from start to bed
    time1 = bed - sta
    earn1 = time1 * 12
    print("hours:",time1,"earned:",earn1)
    
	#the second time block
	#calculate the hours from bed to midnight or end of hours worked
    #index 7 is midnight on the timescale
    if sto >=7:
        time2 = 7 - bed
        earn2 = time2 * 8
        print("hours:",time2,"earned:",earn2)
    else:
        time2 = sto - bed
        earn2 = time2 * 8
    
	#the third time block
	#calculate the hours from midnight to stop time
    #if stop time before midnight then break or return 0
    #index 7 is midnight on the timescale
    if sto >7:
        time3 = sto - 7
        earn3 = time3 * 16
        print("hours:",time3,"earned:",earn3)
    else:
        earn3 = 0
	
	#add up the earnings and return the result
    totalHours = sto - sta
    print("total hours:",totalHours)
    
    totalEarnings = earn1 + earn2 + earn3
    print("total earnings:",totalEarnings)
    
    return totalEarnings