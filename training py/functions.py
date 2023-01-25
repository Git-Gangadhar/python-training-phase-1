num=int(input("enter a number :"))
if num==1:
    print("it is a prime number")
elif num> 1:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            res=True
        break
if res:
        print(num,"the number is not a prime number")
else:
    print(num,"the number is a prime number")
