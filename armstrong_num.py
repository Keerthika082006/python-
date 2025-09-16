num=int(input("enter a num:"))
num_str=str(num)
num_digits=len(num_str)
powers=0
for digit in num_str:
    powers += int(digit)**num_digits

if powers==num:
    print(f"the given num {num} is armstrong")
else:
    print(f"the given num {num} is not armstrong")
