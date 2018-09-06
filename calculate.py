import re
import math

def inputs():
    #begin by displaying a help message with instructions
    help_msg()
    
    #prompt user for times and validate the input
    start = validateStart()    
    stop = validateStop()
    bed = validateBed()

    #run the calculations
    calculate(start,stop,bed)

def calculate(start,stop,bed):    
    #This is an array representing a full/maximum work night.
    #strategy: calculate position minus position to get hours
    timescale = [5,6,7,8,9,10,11,12,1,2,3,4]
    
    #create the calculator variables based on the Index strategy          
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
    #if stop time before midnight then return 0
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

def help_msg():
    print("    This program will prompt for 3 inputs (Starting time, Ending time and Bed time).\n    Enter either numbers (e.g. 5, 7.25, 8) or a time form (e.g. 5:00, 7pm, 9:30pm).\n    The program expects a number between 5pm - 4am.\n")
	
def validateStart():
    start = input('Enter Starting time:')
    #error check the user input for a valid time
    while int(start) < 5:
        print("Please enter a Starting time between 5pm and 12am:")
        start = input('Re-Enter start time:')    
    return int(start)

def validateStop():
    stop = input('Enter Stopping time:')
    return int(stop)

def validateBed():
    bed = input('Enter Bed time:')
    while int(bed) < 5:
        print("If bed time began before arrival, please enter your arrival time.")
        bed = input('Re-Enter Bed time:')    
    return int(bed)
    
inputs()