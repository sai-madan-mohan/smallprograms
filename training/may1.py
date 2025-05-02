1. Variables and Data Types
name = "sai"
age = 26
height = 5.10
learning_django = True
list = ["java","python"]
self_info ={"name":name,"age":26,"is_learning":True}
set = {1,2,3,4,}

print(name)
print(age)
print(height)
print(learning_django)
print(list)
print(self_info)
print(set)

2. Operators
   Arithmetic operators,relation operators,assignment,identity,logical,membership,bitwise
Arithmetic operators
a= 40
b = 20
print(a+b) #add
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

 comaprison operators
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

Assignmnet operators

a= 10
a=a+5
a=a-5
a=a*5 
print(a)

logical
a=10
b=9
if a>9 and b<6:
    print("both are true")
else:
    print("one of them is false")

control flow

power_level = 99

if power_level >100:
    print("deploy hulkbuster")
elif power_level >80:
    print("depoly mark85")
else:
    print("hold on")

suits = ["Mark1","Mark2","Mark3"]
for suit in suits:
    print("Deploying Suit : ",suit)
for i in range(1,4):
    print("Testing Suit : ",i)  

power = 3

while power >0 :
    print("power count  :", power)
    power = power-1

    print("power count  :", power)
    if suit == "Mark2":
        
        break
    print(suit)

for i in range(1,10):
    if i%2 != 0:
      continue 
    print(i)

i = 1
n = 0

while i<=5:
    n = i+n
    i= i+1
print("Sum of first 5 natural numbers:", n)    

i=5
while i>=0:
    print(i)
    i=i-1

i = 2

while i<=10:
    print(i)
    i=i+2

i = 3
n = 1
while n<=10:
    print(f"{i} x{n}  = {i*n}")
    n = n+1
    
num = 1234
y = 0 
while num!=0:
    x=num%10
    y=y*10+x
    num=num//10
print("reverse of number is:",y)

def suit(name="Iron Man"):
    return f"Deploying Suit : {name}"
def Mark(name):
    return f"Testing Suit : {name}"

mark2 = Mark("Mark2")
print(mark2)
print(suit())

list

suits = ["Mark 45", "Mark 90", "Hulkbuster", "Mark 85"]
print(suits[0])
print(suits[-1])
suits[1] = "Mark 50"
print(suits)

def find_the_element(suits,target):
    
