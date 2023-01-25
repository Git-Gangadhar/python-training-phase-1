from User import user

class login:
    __db=[]
    def __init__(self):
        print("welcome user")
        print("1.register")
        print("2.login")
        print("3.exit")
    def create_user(self, name, email, password):
        new_user=user(name, email, password)
        self.__db.append(new_user)
        print(self.__db)
        return True
    def validate_user(self, email, password):
        temp=self.__db.copy()
        for user_obj in temp:
            if email==user_obj.email:
                if password==user_obj.get_user_password():
                    return "login success"
                else:
                    return "login failed"
obj=login()
while True:
    option=input("enter your choice")
    if option=='1':
        name=input("enter your full name: ")
        email=input("enter email: ")
        password=input("enter password: ")
        res=obj.create_user(name, email, password)
        if res==True:
            print("user created successfully")
        elif option=='2':
            email=input("enter email: ")
            password=("enter passowrd: ")
            result=obj.validate. user(email,password)
            
        else:
             option='3'
             print("exit")
                
                  
            
