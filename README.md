<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

# Python Numeric Literal Checker

A tool to recognize and validate Python numerical literals according to the Python language specification.

## 🏗️ Project Overview

This project implements Non-deterministic Finite Automata (NFA) to recognize Python's numerical literals. We've designed automata to validate:

- Decimal integer literals (e.g., `0`, `123`, `1_000`)
- Octal integer literals (e.g., `0o17`, `0O644`)
- Hexadecimal integer literals (e.g., `0x1A`, `0XdeF`)

According to the [Python documentation](https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals):

### Integer Literals

Integer literals are described by the following lexical definitions:

```
integer      ::= decinteger | bininteger | octinteger | hexinteger
decinteger   ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
bininteger   ::= "0" ("b" | "B") (["_"] bindigit)+
octinteger   ::= "0" ("o" | "O") (["_"] octdigit)+
hexinteger   ::= "0" ("x" | "X") (["_"] hexdigit)+
nonzerodigit ::= "1"..."9"
digit        ::= "0"..."9"
bindigit     ::= "0" | "1"
octdigit     ::= "0"..."7"
hexdigit     ::= digit | "a"..."f" | "A"..."F"
```

## 📁 Project Files

- **nfa folder**: Contains JFLAP files (.jff) and images (.jpg) for all NFAs
- **src folder**: Contains Python implementation
  - **input_files**: Contains test files for validating numeric literals
    - `hex_in_ans.txt`: Test cases for hexadecimal integers
    - `dec_in_ans.txt`: Test cases for decimal integers
    - `oct_in_ans.txt`: Test cases for octal integers
- **tests folder**: Contains pytest test files (for development)

## 🧪 Testing Format

### Test Input Files
Each `*_in_ans.txt` file contains test cases in the following format:
```
test_input accept/reject
```

Example `hex_in_ans.txt`:
```
0x0 accept
0xABC accept
0x123_ reject
0x 123 reject
```

### Running Tests
1. Choose option 5 from the main menu
2. Select the type of checker (decimal, octal, or hexadecimal)
3. Program will generate an `*_out.txt` file showing:
   - Test input
   - Expected result
   - Actual result
   - Pass/Fail status

Example output:
```
Test Input | Expected | Actual | Pass/Fail
--------------------------------------------------
0x0       | accept   | accept | PASS
0xABC     | accept   | accept | PASS
0x123_    | reject   | reject | PASS
0x 123    | reject   | reject | PASS
```

## 🐭🐭🐭 Team "Three Musketeers"

| Member   | GitHub            | Contribution    |
| -------- | ----------------- | --------------- |
| [Name 1] | [GitHub Username] | NFA design, ... |
| [Name 2] | [GitHub Username] | NFA design, ... |
| [Name 3] | [GitHub Username] | NFA design, ... |

## 📋 Current Status

- [x] NFA designs completed for decimal, octal, and hex integers
- [x] Basic program structure established
- [ ] Implementation of decimal integer checker
- [ ] Implementation of octal integer checker
- [x] Implementation of hexadecimal integer checker
- [ ] Comprehensive testing with complex cases

## 🔮 Future Work

- Support for floating-point literals (for extra credit)
- Enhanced error reporting

## 📚 References

- [Python Language Reference: Lexical Analysis](https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals)
- [JFLAP Documentation](https://www.jflap.org/jflaptmp/)
