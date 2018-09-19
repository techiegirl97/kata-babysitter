import math

def inputs():
    help_msg()
    
    start = validateStart()    
    stop = validateStop()
    bed = validateBed()

    calculate(start,stop,bed)

def calculate(start,stop,bed):    
    timescale = [5,6,7,8,9,10,11,12,1,2,3,4]      
    sta = timescale.index(start)
    sto = timescale.index(stop)
    bed = timescale.index(bed)

    time1 = bed - sta
    earn1 = time1 * 12

    if sto >=7:
        time2 = 7 - bed
        earn2 = time2 * 8
    else:
        time2 = sto - bed
        earn2 = time2 * 8
    
    if sto >7:
        time3 = sto - 7
        earn3 = time3 * 16
    else:
        earn3 = 0	
    totalHours = sto - sta
    print("total hours:",totalHours)    
    totalEarnings = earn1 + earn2 + earn3
    print("total earnings:",totalEarnings)    
    return totalEarnings

def help_msg():
    print("    This program will prompt for 3 inputs (Starting time, Ending time and Bed time).\n    Enter either numbers (e.g. 5, 7.25, 8) or a time form (e.g. 5:00, 7pm, 9:30pm).\n    The program expects a number between 5pm - 4am.\n")
	
def validateStart():
    start = input('Enter Starting time:')
    parsed = round(float(start))
    while parsed < 5:
        print("Please enter a Starting time between 5pm and 12am:")
        start = input('Re-Enter start time:')
        parsed = round(float(start))        
    return int(parsed)

def validateStop():
    stop = input('Enter Stopping time:')  
    parsed = round(float(stop))    
    return int(parsed)

def validateBed():
    bed = input('Enter Bed time:')
    parsed = round(float(bed))    
    while parsed < 5:
        print("If bed time began before arrival, please enter your arrival time.")
        bed = input('Re-Enter Bed time:')
        parsed = round(float(bed))        
    return int(parsed)

#comment this line out when running the pytests or you will be prompted for input
inputs()