class Account:
    def __init__(self, email, password, role):
        self.__email = email
        self.__password = password
        self.__role = role  #'customer', 'admin'
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def get_role(self):
        return self.__role
    