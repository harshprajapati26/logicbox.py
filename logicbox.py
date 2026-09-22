print(" welcome to logic box program by harsh prajapati!")
def show_menu():
    print("\nSelect an option:")
    print("1. Generate a pattern (right-angled triangle)")
    print("2. Analyze a range of numbers")
    print("3. Exit")
def generate_pattern():
    print("\n--- Pattern Generator ---")

    while True:
        try:
            rows = int(input("Enter the number of rows for the pattern: "))

            if rows <= 0:
                print("Invalid input! Number of rows must be positive.")
                print("Stopping pattern generation...")
                break

            print("\nPattern:")

            for i in range(1, rows + 1):

                for j in range(i):

                    print("*", end="")

                print()  
            break

        except ValueError:
            print("Invalid input! Please enter a whole number.")



def analyze_range():
    print("\n--- Number Analyzer ---")

    try:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("Invalid range! Starting number must be smaller.")
            return

        even = 0
        odd = 0

        for number in range(start, end + 1):

            if number % 2 == 0:
                even += 1
            else:
                odd += 1

        print("\nAnalysis:")
        print("Even numbers:", even)
        print("Odd numbers:", odd)

    except ValueError:
        print("Invalid input! Please enter whole numbers.")


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_pattern()

    elif choice == "2":
        analyze_range()

    elif choice == "3":
        print("\nThank you for using Logic Box!")
        print("Program ended.")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
