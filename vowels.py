def name():
    my_name=["a","k","i","l","a","n"]
    vowels=["a","e","i","o","u"]
    temp=0
    for x in my_name:
        if x in vowels:
            print("vowels:",x)
            temp+=1
    print("total number in munamde:",temp)
name()
