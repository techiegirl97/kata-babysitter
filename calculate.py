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
	print(time1, earn1)
	
	#the second time block
	#calculate the hours from bed to midnight
	time2 = 7 - bed
	earn2 = time2 * 8
	print(time2, earn2)
	
	#the third time block
	#calculate the hours from midnight to stop time
	time3 = sto - 7
	earn3 = time3 * 16
    print(time3, earn3)
	
	#add up the earnings and return the result
	totalEarnings = earn1 + earn2 + earn3
	print(totalEarnings)
	return totalEarnings
	
