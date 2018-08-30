def calculate(start,stop,bed):
    #import the needed libraries
    import math
    
    #This is an array representing a full/maximum work night.
    #strategy: calculate position minus position to get hours
    timescale = [5,6,7,8,9,10,11,12,1,2,3,4]
    
    #round the start\stop time to the nearest hour
    #bedtime may be fluid, round to the next hour
    
    sta = timescale.index(start)
    sto = timescale.index(stop)
    bed = timescale.index(bed)
    
	#the first time block
	#calculate the hours from start to bed
    time1 = bed - sta
    earn1 = time1 * 12
    print("hours:",time1,"earned:",earn1)
    
	#the second time block
	#calculate the hours from bed to midnight or end of hours worked
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