myname="akilan"
vowels="aeiou"
tem=0
for x in myname:
     if (x in vowels):
         print("vowels:",x)
         tem=tem+1
print("total number of vowels in myname:",tem)
