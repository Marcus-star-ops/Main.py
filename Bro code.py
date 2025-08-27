#age = 21 Variables
#players = 2
#quantity = 5
#print(f"you are {age} years old")
#print(f"There are {players} players online")
#print(f"You wouldPurchase {quantity} From Temu")
#from collections.abc import async_generator
from tkinter.font import names


#invoking a function
#def happy_birthday(name, age):
 #print(f"Happy Birthday {name}")
 #print(f"You are {age} years old now")
 #print(f"Happy birthday to you")
 #print()
#happy_birthday("Bro",20)
#appy_birthday("Marcus",30)
#happy_birthday("Mutsa",40)


#def display (username,amount, due_date ):
    #print(f"Hello {username}")
    #print(f"your balance is ${amount}")
   # print(f"due date is {due_date}")
#  display("Marcus",100.50, 11/3/25)


#def add(a,b):
   # return a+b
#def sub(a,b):
   # return a-b
#print(add(3,4))
#print(sub(3,4))

#If Statements
#name =input("Enter your Name:")
#if name=="":
 #  print("You did not enter your name ")
#else:
 #  print(name)
#print(f"Your Name is {name}")

#while loop
#name = input("Enter your Name")
#while name =="":
 #    print(" You Did not Enter Your name")
#name = input("Enter your Name")
#print(f"Hello {name}")

#Creating classes/ defining a class
class Dog:
  def __init__(self,name ,age, species):
        self.name = name
        self.age = age
        self.species = species
        #Creating an object of the dog class.

 Dog1 =Dog ("Buddy", age=3, species = "canine")
Dog2 =Dog("Rex", age=4, species = "wolf")

print(Dog1.name)
print(Dog1.species)
print(Dog1.age)

print(Dog2.name)
print(Dog2.species)
print(Dog2.age)




