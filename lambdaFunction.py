"""
#lambda function
add=lambda x,y:x+y
print(add(4,5))

#lambda function using conditional statemnet
number=lambda x,y: x if x>y else y
print(number(4,3))

#string concant using lambda
name=lambda x,y:x+" "+y
print(name("raj","kumar"))

num=lambda x: x**2
print(num(2))
"""
num=int(input("enter a num"))
if num/1==0:
    print("prime")

else:
    print("not a prime")
        
