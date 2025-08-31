#logical operator=evaluate multiple conditions(or,and,not)
#or = at least one condition must be true
#and = both condition must be true
#not = inverts the condition(not false,not true)


#or
temp = 37
its_raining = True

if temp>40 or temp<0 or its_raining:
    print("the outdoor event is cancelled")

else:
    print("the outdoor event is still scheduled")

"""
#and
temp=14
its_sunny=True

if temp>=28 and its_sunny:
    print("it is hot outside")
    print("it is sunny")

elif temp<=0 and its_sunny:
    print("it is cold")
    print("it is sunny")

else:
    print("nothing")
"""
#not
temp=12
its_sunny=False

if temp>=28 and not its_sunny:
    print("it is hot ")
    print("it is cloudy")
else:
    print("nothing")
