class calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b
        result=0
         
    def addition_of_two_numbers(self):
        result = self.a + self.b
        print("The add is " + str(result))

    def substraction_of_two_numbers(self):
        result = self.a - self.b
        print("The substract is " + str(result))

    def multiplication_of_two_numbers(self):
        result = self.a * self.b
        print("The mutiply is " + str(result))

    def division_of_two_numbers(self):
        result = self.a / self.b
        print("The divide is " + str(result))

def main():
    operation = int(input("""
List Operations:
        1) add
        2) subtract
        3) divide
        4) multiply

Enter operation: """))
    if (operation >= 1 and operation <= 4):
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        num = calculator(num1, num2)
        if operation == 1:
            num.addition_of_two_numbers()
        elif operation == 2:
            num.substraction_of_two_numbers()
        elif operation == 3:
            num.multiplication_of_two_numbers()
        elif operation == 4:
            num.division_of_two_numbers()
    else:
        print("wrong operation")

if __name__ == "__main__":
    #para evitar decir que funcion correr y correr todo
    main()

    
