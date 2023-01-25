#login system
class user:
    name=""
    email=""
    __password=""
    mobile_number=""
    def update_name(self,new_name):
        self.name=new_name
    def get_name(self):
        return self.name
    def update_password(self,new_password):
        self.__password=new_password
    def update_mobile_number(self, new_number):
        pass
    def get_user_password(self):
        return self.__password
