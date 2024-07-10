a = int(input("Enter a "))
b = int(input("Enter b "))

choice = int(input("Choose anyone to do the math operation {add: 1, mul: 2, div: 3, sub: 4 } "))

if choice == 1:
    print(a+b)
elif choice == 2:
    print(a*b)
elif choice == 3:
    print(a/b)
elif choice == 4:
    print(a-b)
else:
    print("Invalid choice")