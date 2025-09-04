num=int(input("enter a num:"))
if num>1:   
     for i in range(2,num):
        if num%i==0 :
            print(f"the given num {num} is not prime")
            break
     else:
           print(f"The given num {num} is prime")
else:
    print("negative num is not a prime num")

