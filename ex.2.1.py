# comparision operators
a=18
if a>=18:
  print("You can vote")
else:
  print("You cannot vote")
b=60
if b<=60:
  print("You can do the job")
else:
  print("You cannot do the job")

# logical operators
c=False
d=True

if c or d:
  print("It's true")
else:
  print("It's false")

if not c:
  print("It's true")
else:
  print("It's false")

# Calculate the radius of the circle
pi=3.141592653589793238462643383279502884197
r=(input("Enter the radius "))
rs=str(r)
area=(pi*r*r)
areas=str(area)
print("The area of the cricle with radius "+ rs + " is "+ areas)  