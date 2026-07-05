from abc import ABC,abstractmethod  

# abc --> Abstract Base Class

# ABC
# -> Used to create Abstract Class

# abstractmethod
# -> Used to create Abstract Method


class Bankapp(ABC):
    
    def database(self):
        print("Connect to database")

    @abstractmethod
    def security(self):
        print("Bank security")

    @abstractmethod
    def display(self):
        print("Bank display")

class MobileApp(Bankapp):

    def mobile_login(self):
        print("Login into mobile")

    def security(self):
        print("Mobile security")
        super().security()

    def display(self):
        print("Mobile display")

m=MobileApp()

m.database()
m.mobile_login()
m.security()
m.display()

# b=Bankapp()  we can not make obj of abstract class