from dec_checker import decimal_integer_checker
from octal_checker import octal_integer_checker
from hex_checker import hexadecimal_integer_checker

def combined_checker(input_str):
    if decimal_integer_checker(input_str):
        return True, "decimal"
    elif octal_integer_checker(input_str):
        return True, "octal"
    elif hexadecimal_integer_checker(input_str):
        return True, "hexadecimal"
    else:
        return False, None

def process_file(filename, checker_function):
    try:
        with open(filename, 'r') as f:
            test_cases = [line.strip() for line in f.readlines()]
        results = []
        for test in test_cases:
            result = checker_function(test)
            results.append((test, "accept" if result else "reject"))
        return results
    except Exception as e:
        print(f"Error processing file: {e}")
        return []

def main():
    while True:
        print("\nPython Numeric Literal Checker")
        print("1. Test Decimal Integer")
        print("2. Test Octal Integer")
        print("3. Test Hexadecimal Integer")
        print("4. Test All Types")
        print("5. Process Test File")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            test_str = input("Enter a string to check: ")
            result = decimal_integer_checker(test_str)
            print(f"Result: {'ACCEPT' if result else 'REJECT'}")
        elif choice == "2":
            test_str = input("Enter a string to check: ")
            result = octal_integer_checker(test_str)
            print(f"Result: {'ACCEPT' if result else 'REJECT'}")
        elif choice == "3":
            test_str = input("Enter a string to check: ")
            result = hexadecimal_integer_checker(test_str)
            print(f"Result: {'ACCEPT' if result else 'REJECT'}")
        elif choice == "4":
            test_str = input("Enter a string to check: ")
            result, type_name = combined_checker(test_str)
            if result:
                print(f"ACCEPT - Valid {type_name} integer literal")
            else:
                print("REJECT - Not a valid Python numeric literal")
        elif choice == "5":
            filename = input("Enter test file name: ")
            print("Select checker type:")
            print("1. Decimal")
            print("2. Octal")
            print("3. Hexadecimal")
            print("4. Combined (all types)")
            checker_choice = input("Enter choice (1-4): ")
            if checker_choice == "1":
                results = process_file(filename, decimal_integer_checker)
            elif checker_choice == "2":
                results = process_file(filename, octal_integer_checker)
            elif checker_choice == "3":
                results = process_file(filename, hexadecimal_integer_checker)
            elif checker_choice == "4":
                def combined_result(s):
                    result, _ = combined_checker(s)
                    return result
                results = process_file(filename, combined_result)
            else:
                print("Invalid choice")
                continue
            for test, result in results:
                print(f"{test}: {result}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()