import time
def count(end=7,start=6):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("done!")
count(10)
