#Function Declaration

def greetmenonparameterized():
    print("Good Morning without parameters")

def greetme(name):
    print("Good Morning "+name)

def GreetMeInteger(age):
    print("{} {}".format("Good Morning ", age))

def addintegers(a, b):
    return a+b

greetmenonparameterized()
greetme("Sidhesh")
GreetMeInteger(20)
print(addintegers(10, 23.6))