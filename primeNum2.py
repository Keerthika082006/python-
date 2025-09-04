num=int(input("enter a num"))
if num ==2:
    prime=True
else:
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            prime=False
            break
if prime:
    print("Prime")
else:
    print("Not Prime")
