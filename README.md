<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

# Python Numeric Literal Checker

A tool to recognize and validate Python numerical literals according to the Python language specification.

## 🏗️ Project Overview

This project implements Non-deterministic Finite Automata (NFA) to recognize Python's numerical literals. We've designed automata to validate:

- Decimal integer literals (e.g., `0`, `123`, `1_000`)
- Octal integer literals (e.g., `0o17`, `0O644`)
- Hexadecimal integer literals (e.g., `0x1A`, `0XdeF`)

Our implementation strictly follows Python's language specification (sections 2.4.4 - 2.4.5), ensuring accurate validation of all numeric formats including proper handling of underscores as digit separators.

## 🔤 Python Numeric Literals Specification

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

- Underscores can be used to group digits for enhanced readability
- One underscore can occur between digits, and after base specifiers
- Leading zeros in a non-zero decimal number are not allowed
- There is no limit for the length of integer literals

Examples:

```
7     2147483647                        0o177    0b100110111
3     79228162514264337593543950336     0o377    0xdeadbeef
      100_000_000_000                   0b_1110_0101
```

## 📁 Project Files

- **nfa folder**: Contains JFLAP files (.jff) and images (.jpg) for all NFAs
- **src folder**: Contains Python implementation
- **tests folder**: Contains test files with various test cases

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
- [ ] Implementation of hexadecimal integer checker
- [ ] Comprehensive testing with complex cases

## 🔮 Future Work

- Support for floating-point literals (for extra credit)
- Enhanced error reporting

## 📚 References

- [Python Language Reference: Lexical Analysis](https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals)
- [JFLAP Documentation](https://www.jflap.org/jflaptmp/)
