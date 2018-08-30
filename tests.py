#write the tests
#order of variables (start time, stop time, bedtime), result is $earnings
#5 to 8 is 3 hours at ($12/hr) = $36
#8 to mid is 4 hours at ($8/hr) = $32
#mid to 4 is 4 hours at ($16/hr) = $64

test.expect(calculate(5,4,8) == 132)
test.expect(calculate(5,4,7) == 128)
test.expect(calculate(5,8,7) == 32)
test.expect(calculate(5,7,7) == 24)