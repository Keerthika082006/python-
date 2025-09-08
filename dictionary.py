#dictionary = a collection of {key:value} pairs
#              ordered and changable . no dupicates

fruits={"apple":"red",
        "mango":"yellow",
        "grapes":["green","black"],
        "mango":"yellow",
        }

#print(fruits.get("mango"))

#if fruits.get("orange"):
#   print("that fruit exists")
#else:
#   print("that fruit does not exiests")

#fruits.update({"goa":"green"})
#fruits.update({"grapes":"black"})
#fruits.pop("mango")
#fruits.popitem()
#fruits.clear()
#print(fruits["mango"])
#print(fruits['grapes'][1])

for sweet in fruits['grapes']:
    print(sweet)

#keys=fruits.keys()
#for key in fruits.keys():
#   print(key)

#value = fruits.values()
#for value in fruits.values():
#   print(value)

#item =fruits.items()
#for key,value in fruits.items():
#   print(f"{key} : {value}")


#print(fruits)
