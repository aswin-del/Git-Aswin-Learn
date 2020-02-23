# comment  this is my first line
print("Narayanan Aswin aaaaa""")
print ('0-------------')
print ('value of 10 * 10 ')
print(10*10)

# comment variable declaration
price = 10 # intiger
rate = 5.1 # for floating point
name = 'aswin' # string
blnStat = False # for boolean
print (price)
print (rate)
print(name)
# new assinment to get hospital details of an patent
cstName = 'New Hospital'
ptname = 'John Smith'
ptAge = 20
ptDOB = '1976/10/10'
isNew = True
#comment Printing patent details
print(cstName)
print(ptname)
print(ptDOB)
print (ptAge)
print (isNew)
#comment getting input from console
ptname = input('waht is the patent name :-')

print ('welcome to '+ cstName +' '+ ptname)
# comment age calulation program
DobYear = input ('Enter your year of birth ')
SysYear = 2020
Age = SysYear - int(DobYear)
print ('Your Age :- '+ str(Age))

#comment get string and convrt to float


#commment for python for biginers using cotes
print ('python for "Bigginers" ')
print ("python cour's for bigginers ")

#comment Array operartion in python

print(ptname[4])
print(len(ptname))
print (ptname[-4])
print(ptname[0:4])
print (ptname[2:3])
print(ptname[:])
print (ptname[2:-2])
strconcat = f'{ptname}  and his age is {Age}' # for string formating
print(strconcat)
print (strconcat.upper()) # for using built in methods
#comment math functions
x = 10
print(x/3)
print(x//3)
print(x%3)
print(x^3)
print(x*3)
print(x**3)
x=x+3
print(x)
x-=3
print(x)
print(10+2*3-4)
#try to read math module and read all the methods
# conditional statements
bln1 = True
bln2 = False

if bln1 and bln2:
    print("eliglible for loan ")
else:
    print("not eligible for loan")
# comment for conditional operator example
if len(ptname) <5 or len(ptname) >49:
    print("please enter characters between 5 to 50")
else:
    print("name is good to go!!!")
#comment looping statements
intX = 1
while intX < 5:
    print ("*" * intX)
    intX = intX +1

#comment for car start, stop & quit program
strGetInput = ""
strStart = "start"
strtStop = "stop"
strQuit = "quit"
strStatus = False
while True:
    strGetInput =  input(">>").lower()
    if strGetInput == strStart and strStatus == False:
        print("Car Engine Started...")
        strStatus = True
    elif strGetInput == strStart and strStatus == True:
        print("Car Engine is Already Running.....")
    elif strGetInput == strtStop and strStatus == True:
        print("Car Engine Stopped...")
        strStatus = False
    elif strGetInput == strtStop and strStatus == False:
        print("Car Engine has already Stopped...")
    elif strGetInput == strQuit and strStatus == False:
        print("Quiting the game..!")
        break
        strStatus = False
    elif strGetInput == strQuit and strStatus == True:
        print(" First Stop the Car..")
# Comment for For Loop
for intX in range(10):
    print(intX)
for intX in ptname:
    print(intX)
intSum = 0
for intX in [10,20,30]:
    intSum = intSum + intX
print(intSum)
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
strconcat = ""
for intX in [5,2,5,2,2]:
    for intY in range(intX):
        strconcat = strconcat + "X"
    print(strconcat)
    strconcat = ""
# list tutorial
names = ['Aswin','Baratharam','Raghav','Ramya']
print(names)
print(names[1])
print(names[3])
print(names[0])
print(names[-2])
print(names[-1])
print(names[0:4])
print(names[:3])
print(names[2:])
# print(names[5])
# number sort alogoritham using list
numbers= [1,3,4,2]
intMax = numbers[0]
for intX in numbers:
    if intMax < intX:
        intMax = intX
print(intMax)

#two dimentional arrray or matrix
int2DMat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(int2DMat[1][1])
for intR in int2DMat:
    for intC in intR:
        print(intC)
# list funtions
numbers= [1,3,4,2,9,9,9,9,9,9,9,2,2,2,2,2,1,1,1,1,3,3,3,3,4,4,4]
print(numbers)
numbers.append(9)
print(numbers)
numbers.insert(3,9)
numbsers1 = numbers.copy()
print(numbers)
print(numbsers1)
numbers.remove(9)
print(numbers)
print(9 in numbers)
print(numbers.count(9))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
intCnt = 0
print(numbsers1)
numbsers2 = []
for intX in numbsers1:
    if intX not in numbsers2:
        numbsers2.append(intX)
        print(numbsers2)
# Tuple are immutable
intTup = (1,2,3,4)
print(intTup)
# Python unboxing of variable ?
intX = intTup[0]
intC = intTup[1]
intR = intTup[2]
print(intX,intC,intR)
# easy way to assingn

intR,intC,intX,intCnt = intTup
print(intR,intC,intX,intCnt)
names = input(">>")
print(names)
names_list= names.split(" ")
print(names_list)
# now we learn key value pair Dictionery
strDigit = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
    }
intX = input("Number >> ")
for intC in intX:
    print(strDigit.get(intC),"none")
# defining function


def first_fun(myname):
    print(f'My First Function Call print line 1 {myname}')
    print('My First Function Call Print Line 2 ')


first_fun("Aswin Narayanan")
