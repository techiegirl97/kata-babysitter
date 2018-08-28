def calculate(start,stop,bed):
	
	#import the needed libraries	
	import math
	
	timescale = {5,6,7,8,9,10,11,12,1,2,3,4}
	#do position minus position to get hours
	
	#round the start\stop time to the nearest hour
	#bedtime may be fluid, round to the next hour

	#the main function to add all earnings, will call the others
	#add up the earnings

	#the first time block
	#calculate the hours from start to bed
	#5 to 8 is 3 hours at ($12/hr) = $36
	
	#the second time block
	#calculate the hours from bed to midnight
	#8 to mid is 4 hours at ($8/hr) = $32
	
	#the third time block
	#calculate the hours from midnight to stop time
	#mid to 4 is 4 hours at ($16/hr) = $64
	


	
#write the tests
#order of variables (start time, stop time, bedtime), result is $earnings
test.expect(calculate(5,4,8) == 132)
test.expect(calculate(5,4,7) == 128)

