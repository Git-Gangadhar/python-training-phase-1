db=[{'abc@example.com':'abc'},{'xyz@example.com':'xyz'},{'aaa@example.com':'aaa'},{'gangadhar@gmail.com':'gnagadhar'}]

mailid=input("enter the mailid ")
password=input("enter the password")
temp={
    mailid:password
    }
if temp in db:
    print("found")
else:
    print("not found")

userinput= input("enter the mailid ")
if userinput==mailid:
    g=input("password")
    if g==password:
        print("welcome")
    else:
            print("this is wrong password")
            
else:
        print("this is wrong usermail")
