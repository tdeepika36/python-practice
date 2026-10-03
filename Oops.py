from abc import ABC, abstractmethod
from dataclasses import dataclass
class Oops:
    def __init__(self):
      self.name="Deepika"
      self.age=26
      self.position="developer"
e= Oops()
print(e)
print(e.__dict__)

class Employee:
   min_age=20
   @classmethod
   def update_age(cls,new_age):
      if(new_age)<20:
         raise ValueError("Need age gt 20")
      cls.min_age=new_age

   def __init__(self,name,age,role):
      self.name=name
      self.age=age
      self.role=role

   def info(employee):
      print(f"{employee.name} is {employee.age} years old.Employee is a {employee.role}.")

   def __str__(self):
      return f"{self.name} is a employee name.For end user readable format"
   def __repr__(self):
      return f"{self.name} is a employee name.Used for developer debugging "

   def __add__(self,other):
      name=self.name+other.name
      age=self.age+other.age
      role=self.role+other.role
      return Employee(name,age,role)
  
   
obj1=Employee("Alex",38,"devops engineer")
obj2=Employee("Rocky",25,"Developer")
Employee.info(obj1)
print(obj1.age)
print(obj2.name)
print(obj1.__dict__)
print(obj1.__class__)
print(obj2)
print(repr(obj1))
print(str(obj2))
obj_new=obj1+obj2
print(obj_new.__dict__)
print(Employee.min_age)
Employee.update_age(27)
print(Employee.min_age)

class Bank:
   
   def __init__(self,owner,balance):
      self.owner=owner
      self._balance=balance
   @property
   def balance(self):
      """Getter:read the balance."""
      return self._balance

   @balance.setter
   def balance(self,amount):
      """Setter: Safely modify balance"""
      if amount<0:
         print("Balance cannot be negative")
      else:
         self._balance=amount

account=Bank("Deepika",1000)
print(account.balance)
new_balance=account.balance=2000
print(new_balance)

class Animal(ABC):

   @abstractmethod
   def sound(self):
       pass
class Dog(Animal):
   def sound(self):
     return """Dog says bow-bow"""
class Cat(Animal):
   def sound(self):
      return """Cat says meow-meow"""
obj=Dog()
print(obj.sound())

class Child(Employee):
   pass
child_obj=Child("Dilly",26,"Developer")
child_obj.info()

@dataclass
class Project:
   name:str
   payment:int
   client:str

   def payment_info(self):
         return f"{self.name} is paid {self.payment}"
object=Project("Dilly",10000,"DS")
print(object.payment_info())