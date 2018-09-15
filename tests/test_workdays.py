#write the tests
#order of variables (start time, stop time, bedtime), result is $earnings
#5 to 8 is 3 hours at ($12/hr) = $36
#8 to mid is 4 hours at ($8/hr) = $32
#mid to 4 is 4 hours at ($16/hr) = $64

#This test script uses the Pytest framework.

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

def test_workdays6():
    #this test validates the input of a string or float type of input for Starting time
    input_values = ['6.25']
    output = []
    
    def mock_input(s):
        output.append(s)
        return input_values.pop(0)
    calculate.input = mock_input
    calculate.print = lambda s : output.append(s)
    
    calculate.validateStart()
    
    assert output == [
        'Enter Starting time:']

def test_workdays7():
    #this test validates the input of a string or float type of input for Stopping time
    input_values = ['9.75']
    output = []
    
    def mock_input(s):
        output.append(s)
        return input_values.pop(0)
    calculate.input = mock_input
    calculate.print = lambda s : output.append(s)
    
    calculate.validateStop()
    
    assert output == [
        'Enter Stopping time:']
        
        
def test_workdays8():
    #this test validates the input of a string or float type of input for Bed time
    input_values = ['8.5']
    output = []
    
    def mock_input(s):
        output.append(s)
        return input_values.pop(0)
    calculate.input = mock_input
    calculate.print = lambda s : output.append(s)
    
    calculate.validateBed()
    
    assert output == [
        'Enter Bed time:']

