#day 2 afternoon

#strings and its methods

s="hello world"
res=s.split(' ')
print(res)
print(s.capitalize())#only starting is captilized
print(s.title())#converts all the starting letters to capital letters

print(s.upper())
print(s.swapcase())#inverts the uppper to lower and lower to upper

##############################3
first="i am"
age=21
last="years old"
print("i am {} years old".format(age))

############

num=8.3
print("the square of {} is {:.5f}".format(num,num*num))#applied at the ennd
####

num=8.3
print(f"the square of {num} is {num*num:.5f}")   #f string methodz

##exception handling

a=int(input("enter a : "))
b=int(input("enter b : "))
try:
    print(a/b)

except:
    print("b cannot be 0")
print("after the error")

##########################

print(eval("7*9/8-99999"))



###################################################################################################
##FUNCTION  i 1 regular functions }}}}}}default value fuctions    keyword argument function     variable length functions

#def function_name
#def addition(number1+number2)
#DEFAULT VALUE
def add(num1, num2=1):
    return num1+num2
c=1
d=2
res=add(10)
print(res)
###

def add(a,b,c,d):
    print(a,b,c,d)
add(10,20,a=30,b=40)

#variable length

def add(*):#define with star because it can take any number of arguemnetas
    print(abc)
add(189,38,"hello",[1,2,3],1000.3)
####
def add(*abc):
    res1=1
    for i in abc:
        res1*=i
    return res1
print(add(10,20,30,40,50))
###

###RECRUSIVE FUNCTIONS

def check(n):
    print(n)
    if n>0:
        check(n-1)
check(5)
















#############



