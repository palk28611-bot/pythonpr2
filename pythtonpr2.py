print("===================================")
print("         WELCOME TO LOGIC BOX")
print("===================================")

while True:
    print("1. Pattern Generator")
    print("2. Number Analyzer")
    print("3. Control Statements")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(" Pattern Generator ")

        rows = int(input("Enter number of rows: "))

        if rows < 1:
            print("Please enter a positive number.")
        else:
            i = 1
            while i <= rows:
                print("* " * i)
                i += 1

    elif choice == "2":
        print(" Number Analyzer ")

        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("Invalid range!")
        else:
            even = []
            odd = []
            total = 0
            number = start

            while number <= end:
                total += number

                if number % 2 == 0:
                    even.append(number)
                else:
                    odd.append(number)

                number += 1

            print("Even numbers:", even)
            print("Odd numbers:", odd)
            print("Sum of numbers:", total)

    elif choice == "3":
        print(" Break Statement ")

        i = 1
        while i <= 5:
            if i == 4:
                break
            print(i)
            i += 1

        print(" Continue Statement ")

        i = 0
        while i < 5:
            i += 1

            if i == 3:
                continue

            print(i)

        print(" Pass Statement ")

        i = 1
        while i <= 3:
            if i == 2:
                pass

            print(i)
            i += 1

    elif choice == "4":
        print("Thank you for using Logic Box!")
        break

    else:
        print("Invalid choice! Please enter 1 to 4.")
