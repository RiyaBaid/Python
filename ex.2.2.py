# Calculator
e=int(input("Enter your first number: "))
f=int(input("Enter your second number: "))
d=input("Enter 1 for addition, 2 for subraction, 3 for multiplication and 4 for division: ")
def calculator(a,b,c):
  if d=="1":
    print(e+f)
  elif d=="2":
    print(e-f)
  elif d=="3":
    print(e*f)
  elif d=="4":
    print(e/f)
  else:
    print("You can only enter 1,2,3,4")
calculator(e,f,d)

# trying functions with 4 arguements
a= input("Enter your name: ")
b= input("Enter your age: ")
c= input("Enter your class: ")
d= input("Enter your section: ")
# Function with four parameters
def introduction(name,age,class2,section):
  print(a +" is of "+b+" years and studies in class " +c+d )
introduction(a,b,c,d)