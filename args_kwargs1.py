def adress(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

#    for value in kwargs.values():
#       print(value,end=" ")

    print(f"{kwargs.get('street')},{kwargs.get('doornum')}")

    if "country" in kwargs:
            print(f"{kwargs.get('city')},{kwargs.get('state')},{kwargs.get('country')}")

    else:
            print(f"{kwargs.get('city')},{kwargs.get('state')}")

adress("miss.","mithra","bala",
       street="nvs avenue",
       doornum="21",
       city="coimbatore",
       state="tamilnadu")
