#set = {} unordered and immutable, but add/remove ok. no dupicates

fruits={"banana","orange","coconut","coconut"}
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)
#fruits.add("pineapple")
#fruits.remove("apple")
fruits.discard("apple")
#fruits.clear()
#fruits.pop()

print(fruits)
