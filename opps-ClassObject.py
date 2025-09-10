class student():
    def say_hello(self,n):
        print(f"hi im {n}")
s1=student()
s1.say_hello('keerthi')

class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return(f'hi im {self.name},and age {self.age}')

s1=student('keerthi',23)
print(s1)