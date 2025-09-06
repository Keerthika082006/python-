#*args=allows you to pass multiple num-key arguments(tuple)
#**kwargs=allows you to pass multiple keyword-arguments(dict)
"""
#def add(a,b):
def add(*args):#anything can be for *args eg:*num,*name
   # print(type(args))
   total=0
   for arg in args:
       total+=arg
   return total
print(add(1,2,3,4))
"""

def display_name(*names):
    #for name in names:
        print(names,end=" ")
display_name("keerthi","akilan,","mithra")
""" 
def address(**kwargs):
    #for value in kwargs.values():
    #for key in kwargs.keys():
    #print(key)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
address(street="nvs avanue",
        house_num="21",
        city="coimbatore",
        state="tamilnadu")
"""                      
