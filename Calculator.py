#add two numbers
def add(x, y):
    return x+y
#subtract two numbers
def subtract(x,y):
    return x-y
#multiply two numbers
def multiply(x,y):
    return x*y
#divide two numbers 
def divide(x,y):
    return x/y
print("Select Operation to perform : ")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVISION")
while True:
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("Enter First Number: "))
            num2=float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid input! Please enter a number")
            continue
        if choice =='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice =='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice =='4':
            print(num1,'/',num2,'=',divide(num1,num2))
        next_calculation=input("Let's Do Next Calculation ? (Yes/No): ")
        if next_calculation=="No":
            break
    else:
        print("Invalid Input")