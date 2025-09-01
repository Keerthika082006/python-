
#byte=cannote be modified prints the ascii value
data=b'keerthi'
print(data)

print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

#bytearray =it can be modified 
#direct indexing
data=bytearray(b'hello')
data[0]=72 #changes 'h' (104)to'H'(72)
print(data)

#slicing
data=bytearray(b'hello')
data[1:3]=b'EL'
print(data)

#append
data=bytearray(b'hello')
data.append(33)
print(data)

#extend
data=bytearray(b'hello')
data.extend(b'world')
print(data)
# we can use insert,pop(using index value),remove(using ascii value)

#byte cannot be modified if u want to modify change byte to bytearray and u can modify it
data=b'hello'
#converts byte to bytearray
mutable_data=bytearray(data)
mutable_data[0]=72
#convert binary back to bytes
modified_data=bytes(mutable_data)
print(modified_data)

#memory view
data=b'hello world'
view=memoryview(data)
print(view[0])
mutable_value=bytearray(view)
mutable_value[0]=72
print(mutable_value)
print(data)
