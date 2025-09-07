#collection = single variable used to store multiple values
#list = [] ordered and chnageable. duplicates

fruits=["apple","banana","orange","mango","apple"]
#print(dir(fruits))
#print(help(fruits))

#print(fruits[0])
#print(len(fruits))
#print("chacolateS" in fruits) #this operator returns boolean
fruits[3]="goa"  #we can change the elements
#fruits.append("pineapple") #we an add an elemente at end using append method
#fruits.remove("mango") #removind an element
#fruits.insert(2,"grapes") #inserting an element based on index value
#fruits.sort() # arramge an elements in alphabetical order
#fruits.reverse()
#fruits.clear()
#print(fruits.index("mango"))
#print(fruits.count("goa"))
print(fruits)

#for fruit in fruits:
 #  print(fruit)

list=[]

elements=int(input('enter anything'))

for i in range(elements):
    element=input(f'enter element {i+1}:')

list.append(element)
print(list)