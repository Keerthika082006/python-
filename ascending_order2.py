number=[20,10,5,15,25,30]
temp=0
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if(number[i]>number[j]):
            #number[i],number[j]=number[j],number[i]
            temp=number[i]
            number[i]=number[j]
            number[j]=temp

            
print("ascending order:",number)
