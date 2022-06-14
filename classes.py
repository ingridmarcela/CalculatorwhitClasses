class User:
    def __init__(self, name, email, password, age):
        self.name=name
        self.email=email
        self.password=password
        self.age=age

    def get_name(self):
        print("My name is " + self.name)
        
    def get_email(self):
        print("My email is " + self.email)

    def get_password(self):
        print("My password is " + self.password)

    def get_age(self):
        print("My age is " + self.age)
        
    def get_data(self):
        self.get_name()
        self.get_email()
        self.get_password()
        self.get_age()

    def get_data2(self): #otra forma
        print("My name is " + self.name)
        print("My email is " + self.email)
        print("My password is " + self.password)
        print("My age is " + self.age)
             
#vamos a instanciar la clase
def main():
    user1= User("ana", "ana@hotmail.com", "1234", "44")
    print("information of the user")
    print(user1.name)
    print(user1.email)
    print(user1.password)
    user1.name="marce"
    print(user1.name)
    marce = User("Daniel", "ingridmarcela2@gmail.com", "1234", "40")
    marce.get_data()
    marce.get_data2()
    
#metodos en una clase son funciones

if __name__ == "__main__":

    main()
