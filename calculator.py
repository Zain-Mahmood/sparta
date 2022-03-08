

def add(first,second):
    return int(first) + int(second)

def sub(first, second):
    return int(first) - int(second)

def mul(first, second):
    return int(first) * int(second)

def div(first, second):
    return int(first) / int(second)

first_number = input("Please enter first number")
second_number = input("Please enter second number")

print("Select operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice = int(input("Enter number choice From operations list above"))
    if choice in (1,2,3,4,5):
        if choice == 1:
            print(add(first_number, second_number))
        elif choice == 2:
            print(sub(first_number, second_number))
        elif choice == 3:
            print(mul(first_number, second_number))
        elif choice == 4:
            print(div(first_number, second_number))
        elif choice == 5:
            print("Thankyou")
            break
        else:
            print("invalid choice")




    