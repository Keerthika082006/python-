'''
class bank_account:
    name=""
    balance=0.0
    account_number=0

    def customer(self):
       print("sucessfu")

customer1=bank_account()
customer1.name='keerthi'
customer1.balance=200000
print('name:',customer1.name)
print('balance:',customer1.balance)

customer2=bank_account()
print("account number:",customer2.account_number)

end=bank_account()
end.customer()

#using constructor

class clasroom:
    def __init__ (self,name,age,degree):
        self.name=name
        self.age=age
        self.degree=degree
    
    #def __del__(self):
     #  print('this is destructor',id(self))

    #def __str__(self):
    #   return(self.degree)
    
        
    def student(self,salery):
      print(f'im {self.name} my age is {self.age},and im persuing {self.degree} my intership salery is {salery}')

student1=clasroom('keerthi',18,'bsc computer science')
student1.student(30000)

student2=clasroom('akilan',19,'bsc')
student2.student(40000)

student3=clasroom('mithre',20,'cyber security')
student3.student(30000)
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  
p1 = Person("John", 36)

print(p1)
