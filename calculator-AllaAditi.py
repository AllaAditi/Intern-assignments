"calculator "
class Calculator():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 

    def add(self, num1, num2):
        return num1+num2
    
    def subtract(self, num1, num2):
        return num1-num2
    
    def multiply(self, num1, num2):
        return num1*num2
    
    def divide(self,num1 , num2):
        return num1 / num2


print("Select operator")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
    continue
calc=Calculator(num1,num2)
if choice == '1':
    print(num1, "+", num2, "=", calc.add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", calc.subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", calc.multiply(num1, num2))

elif choice == '4':
    if num1 and num2 !=0:
         print(num1, "/", num2, "=", calc.divide(num1, num2))
    else:
         print('incorrect input')
else:
    print("Invalid Input")