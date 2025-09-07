#list comprehension=a concise way to create lists in python
#                   compact and easier to read than traditional loops
#                   [expression for value in iterable if condition]
'''
double=[]
for x in range(1,11):
    double.append(x*2)
print(double)


double = [x*2 for x in range(1, 11)]
triples= [y*3 for y in range(1,11)]
squares=[(pow(z,2))for z in range(1,11)]
print(squares)

fruits=["apple","orange","mango","goa"]
fruits=[fruit.upper() for fruit in fruits]
print(fruits)
'''
numbers=[1,-2,3,-4,5,6,-8]
positive_num=[num for num in numbers if num >=0]
negative_num=[num  for num in numbers if num<=0]
even_num=[num for num in numbers if num%2==0]

print(even_num)



