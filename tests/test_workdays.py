#write the tests
#order of variables (start time, stop time, bedtime), result is $earnings
#5 to 8 is 3 hours at ($12/hr) = $36
#8 to mid is 4 hours at ($8/hr) = $32
#mid to 4 is 4 hours at ($16/hr) = $64

import calculate

def test_workday1():
    total = calculate.calculate(5,4,8)
    assert total == 132
    
def test_workdays2():
    total = calculate.calculate(5,4,7)
    assert total == 128
    
def test_workdays3():
    total = calculate.calculate(5,8,7)
    assert total == 32    

def test_workdays4():
    total = calculate.calculate(5,7,7)
    assert total == 24
    
def test_workdays5():
    total = calculate.calculate(6,7,7)
    assert total == 12