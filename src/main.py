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


def process_file(input_filename, checker_function):
    try:
        out_filename = input_filename.replace("_in_ans.txt", "_out.txt")
        results = []

        # read test cases, preserving whitespace
        with open(input_filename, "r") as f:
            lines = [line for line in f if line.strip() and not line.startswith("#")]

        with open(out_filename, "w") as f:
            f.write("Test Input | Expected | Actual | Pass/Fail\n")
            f.write("-" * 50 + "\n")

            for line in lines:
                # strip expected result
                test_input, expected = line.rstrip().rsplit(" ", 1)
                actual = "accept" if checker_function(test_input) else "reject"
                passed = actual == expected

                result_line = f"{test_input} | {expected} | {actual} | {'PASS' if passed else 'FAIL'}\n"
                f.write(result_line)
                results.append((test_input, expected, actual, passed))

        total = len(results)
        passed = sum(1 for _, _, _, p in results if p)
        print(f"\nResults written to {out_filename}")
        print(f"Total tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")

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
            print("\nSelect checker type:")
            print("1. Decimal")
            print("2. Octal")
            print("3. Hexadecimal")
            print("4. Combined (all types)")
            checker_choice = input("Enter choice (1-4): ")

            # map choices to filenames and checker functions
            checker_map = {
                "1": ("input_files/dec_in_ans.txt", decimal_integer_checker),
                "2": ("input_files/oct_in_ans.txt", octal_integer_checker),
                "3": ("input_files/hex_in_ans.txt", hexadecimal_integer_checker),
                "4": (
                    "input_files/combined_in_ans.txt",
                    lambda s: combined_checker(s)[0],
                ),
            }

            if checker_choice in checker_map:
                filename, checker = checker_map[checker_choice]
                try:
                    results = process_file(filename, checker)
                    if not results:
                        print(f"No results found. Make sure {filename} exists.")
                except FileNotFoundError:
                    print(f"Error: Could not find {filename}")
                    print("Make sure you're running from the project root directory.")
            else:
                print("Invalid choice")

        elif choice == "6":
            print("Goodbye! <(^.^)>")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
