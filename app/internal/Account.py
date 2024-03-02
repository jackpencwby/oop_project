class Account:
    def __init__(self, email, password, role):
        self.__email = email
        self.__password = password
        self.__role = role
    
    #Request จ่ากคนทำ Payment ขอเพื่ม attribute account id และ bank เพื่อนำไปใช้ใน MobilebankTransaction
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def get_role(self):
        return self.__role
    