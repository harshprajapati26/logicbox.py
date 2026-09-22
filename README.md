[README.md](https://github.com/user-attachments/files/32506534/README.md)
# Logic Box -- Pattern Generator and Number Analyzer

## 📌 Project Overview

**Logic Box** is a beginner-friendly Python project that combines a
**Pattern Generator** and a **Number Analyzer** in a menu-driven
program.

The project is designed to practice important Python programming
concepts such as:

-   `for` loops
-   `while` loops
-   Nested loops
-   `range()`
-   `break`
-   `continue`
-   `pass`
-   Conditional statements
-   Input validation
-   Error handling
-   Functions
-   Menu-driven programming

------------------------------------------------------------------------

## 🎯 Objective

The main objective of this project is to develop a Python program that:

1.  Generates a right-angled triangle pattern using nested loops.
2.  Analyzes a user-defined range of numbers.
3.  Displays whether each number is **Odd or Even**.
4.  Calculates the **sum of all numbers** in the given range.
5.  Handles invalid user input properly.
6.  Provides a simple menu-driven interface.

------------------------------------------------------------------------

## ✨ Features

### 1. Pattern Generator

The user can enter the number of rows and generate a right-angled
triangle pattern.

Example for 5 rows:

``` text
*
**
***
****
*****
```

The pattern is created using nested `for` loops.

### 2. Number Analyzer

The user enters a starting number and an ending number.

The program:

-   Checks every number in the range.
-   Displays whether each number is **Odd** or **Even**.
-   Calculates and displays the sum of all numbers.

Example:

``` text
Enter the start of the range: 10
Enter the end of the range: 15

Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd

Sum of all numbers from 10 to 15 is: 75
```

### 3. Menu-Driven Interface

The program provides three options:

``` text
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
```

The user can select an option and perform the required operation.

------------------------------------------------------------------------

## 🧠 Python Concepts Used

  Concept              Purpose
  -------------------- --------------------------------
  `print()`            Display output
  `input()`            Take input from the user
  `int()`              Convert input into an integer
  `if / elif / else`   Decision making
  `for` loop           Repetition
  `while` loop         Repeated menu execution
  Nested loops         Generate patterns
  `range()`            Generate a sequence of numbers
  `break`              Stop a loop
  `continue`           Skip the current iteration
  `pass`               Placeholder for future logic
  `try / except`       Handle invalid input
  Functions            Organize the program

------------------------------------------------------------------------

## 🔐 Error Handling and Input Validation

The program validates user input to prevent invalid values.

For example:

-   Pattern rows must be greater than `0`.
-   The ending number must be greater than or equal to the starting
    number.
-   Non-numeric input is handled using `try-except`.
-   Appropriate error messages are displayed when invalid input is
    entered.

Example:

``` text
Invalid input! Please enter a whole number.
```

------------------------------------------------------------------------

## 📂 Project Structure

``` text
Logic-Box/
│
├── logic_box.py
├── README.md
└── demo-video-link.txt
```

------------------------------------------------------------------------

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

``` bash
python --version
```

or:

``` bash
python3 --version
```

### Step 2: Clone the Repository

``` bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 3: Open the Project Folder

``` bash
cd Logic-Box
```

### Step 4: Run the Program

``` bash
python logic_box.py
```

------------------------------------------------------------------------

## 🎥 Project Demonstration Video

Watch the complete project demonstration here:

**▶️ Video Link:**\
https://drive.google.com/file/d/17SeFKqD1G5roCrMhkJRW47gf27zJv9mb/view?usp=sharing
------------------------------------------------------------------------

## 🖥️ Example Console Interaction

``` text
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice: 1

Enter the number of rows for the pattern: 5

Pattern:
*
**
***
****
*****
```

Number analysis example:

``` text
Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice: 2

Enter the start of the range: 10
Enter the end of the range: 15

Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd

Sum of all numbers from 10 to 15 is: 75
```

Exit example:

``` text
Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice: 3

Exiting the program. Goodbye!
```

------------------------------------------------------------------------

## 📋 Assumptions

-   The user enters whole numbers where numeric input is required.
-   Pattern rows must be positive.
-   The start of the number range should not be greater than the end.
-   The program runs in a Python 3 environment.
-   The project is intended for learning and academic purposes.

------------------------------------------------------------------------

## 👨‍💻 Author

**Student Project -- Logic Box**

**Language:** Python 3

**Project Type:** Academic / Beginner Python Project

------------------------------------------------------------------------

## 📜 License

This project is created for educational and academic purposes.
