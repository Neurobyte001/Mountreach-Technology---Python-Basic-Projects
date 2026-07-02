#=====================================================================================
#=====================================================================================

print("\n\nQ02. Strings + Loops + Functions")

# Function to analyze the string
def analyze_string(text):

    # Checking if string is empty
    if text == "":

        print("Error: Empty string is not allowed!")

        return

    # Displaying length
    print("\nLength of the string:", len(text))

    # Displaying reverse string
    print("Reverse String:", text[::-1])

    # Counting vowels
    vowels = 0

    for ch in text.lower():

        if ch in "aeiou":

            vowels += 1

    print("Total Vowels:", vowels)

    # Displaying each character with positive and negative index
    print("\nCharacter Indexes")

    for i in range(len(text)):

        print(f"Positive Index [{i}] = {text[i]}    Negative Index [{i-len(text)}] = {text[i]}")


# Taking input from user
string = input("Enter a string: ")

# Calling function
analyze_string(string)

#=====================================================================================
#=====================================================================================
print("\n\nQ03. (Lists + Functions + Exception Handling)")

# Function to manage student marks
def manage_marks():

    # Creating empty list to store marks
    marks_list = []

    # Taking marks of 5 subjects
    for i in range(1, 6):

        try:

            # Taking marks from user
            mark = int(input(f"Enter marks for Subject {i}: "))

            # Validating marks
            if mark < 0 or mark > 100:

                print("Marks must be between 0 and 100.")

                return

            # Adding marks into list
            marks_list.append(mark)

        except ValueError:

            print("Marks must be an integer value.")

            return

    # Calculating total and average
    total = sum(marks_list)

    average = total / len(marks_list)

    # Displaying result
    print("Average Marks :", average)

    print("Highest Marks :", max(marks_list))

    print("Lowest Marks :", min(marks_list))

    print("Marks in Descending Order :", sorted(marks_list, reverse=True))


# Calling function
manage_marks()

#=====================================================================================
#=====================================================================================

print("\n\nQ04. OOP + Lists + Exception Handling")

# Creating Student class
class Student:

    # Constructor
    def __init__(self, name, roll_no):

        self.name = name

        self.roll_no = roll_no

        self.marks_list = []


    # Function to add marks
    def add_mark(self, mark):

        if mark < 0 or mark > 100:

            print("Invalid Marks!")

        else:

            self.marks_list.append(mark)


    # Function to calculate average
    def get_average(self):

        if len(self.marks_list) == 0:

            return 0

        return sum(self.marks_list) / len(self.marks_list)


    # Function to display details
    def display_info(self):

        print("\nStudent Details")

        print("Name :", self.name)

        print("Roll Number :", self.roll_no)

        print("Marks :", self.marks_list)

        print("Average :", self.get_average())


# Taking student details
name = input("Enter Student Name: ")

roll = input("Enter Roll Number: ")

student = Student(name, roll)

# Taking marks
print("\nEnter 5 Subject Marks\n")

for i in range(5):

    try:

        mark = float(input(f"Subject {i+1}: "))

        student.add_mark(mark)

    except ValueError:

        print("Invalid Input!")

# Displaying information
student.display_info()

#=====================================================================================
#=====================================================================================

print("\n\nQ05. Dictionaries + Functions + Control Structures")

# Function for Student Database
def student_database():

    # Empty dictionary
    students = {}

    while True:

        print("\n===== STUDENT DATABASE =====")

        print("1. Add Student")

        print("2. Search Student")

        print("3. Display All Students")

        print("4. Exit")

        try:

            choice = int(input("Enter Choice: "))

            if choice == 1:

                roll = input("Enter Roll Number: ")

                name = input("Enter Name: ")

                age = int(input("Enter Age: "))

                city = input("Enter City: ")

                students.update({

                    roll:{

                        "Name":name,

                        "Age":age,

                        "City":city

                    }

                })

                print("Student Added Successfully!")

            elif choice == 2:

                roll = input("Enter Roll Number: ")

                data = students.get(roll)

                if data:

                    print(data)

                else:

                    print("Student Not Found!")

            elif choice == 3:

                if len(students)==0:

                    print("No Student Records.")

                else:

                    for roll,data in students.items():

                        print("\nRoll Number:",roll)

                        print("Name :",data["Name"])

                        print("Age :",data["Age"])

                        print("City :",data["City"])

            elif choice == 4:

                print("Program Closed.")

                break

            else:

                print("Invalid Choice!")

        except ValueError:

            print("Invalid Input!")


# Calling function
student_database()

#=====================================================================================
#=====================================================================================

print("\n\nQ06. (Sets + Tuples + Modules)")

# Importing modules
import random
import math

# Creating empty set
numbers = set()

try:

    # Taking 10 numbers
    for i in range(1, 11):

        num = int(input(f"Enter Number {i}: "))

        numbers.add(num)

    # Converting set into tuple
    numbers_tuple = tuple(numbers)

    print("\nUnique Numbers :", numbers_tuple)

    # Picking random numbers
    if len(numbers_tuple) >= 3:

        print("Random Numbers :", random.sample(numbers_tuple, 3))

    else:

        print("Not enough unique numbers.")

    # Square root of sum
    total = sum(numbers_tuple)

    print("Square Root of Sum :", math.sqrt(total))

except ValueError:

    print("Please Enter Valid Numbers.")

except Exception as e:

    print("Error :", e)

#=====================================================================================
#=====================================================================================

print("\n\nQ07. (Lambda + range() + Lists + Exception Handling)")

try:

    # Lambda function
    square = lambda x: x * x

    # Creating list of squares
    squares = []

    for i in range(1, 21):

        squares.append(square(i))

    print("All Squares :", squares)

    print("\nEven Squares :")

    for num in squares:

        if num % 2 == 0:

            print(num)

except Exception as e:

    print("Error :", e)

#=====================================================================================
#=====================================================================================

print("\n\nQ08. (Tuples + Dictionaries + OOP)")

# Creating Employee class
class Employee:

    # Constructor
    def __init__(self, emp_id, name, department, salary):

        self.emp_id = emp_id

        self.name = name

        self.details = (department, salary)

    # Display function
    def show_details(self):

        print("\nEmployee ID :", self.emp_id)

        print("Name :", self.name)

        print("Department :", self.details[0])

        print("Salary :", self.details[1])


# Dictionary of employees
employees = {}

# Adding objects
employees[101] = Employee(101, "Rahul", "AI", 45000)

employees[102] = Employee(102, "Prathmesh", "ML", 60000)

employees[103] = Employee(103, "Aman", "Python", 50000)

# Displaying all employees
for emp in employees.values():

    emp.show_details()

#=====================================================================================
#=====================================================================================

print("\n\nQ09. (Strings + Sets + Exception Handling + Modules)")

# Importing module
import math

try:

    # Taking sentence
    sentence = input("Enter a Sentence: ")

    # Creating unique words set
    unique_words = set(sentence.lower().split())

    print("\nUnique Words :")

    for word in sorted(unique_words):

        print(word)

    # Calculating square
    total = len(unique_words)

    print("\nSquare of Total Unique Words :", math.pow(total, 2))

except Exception as e:

    print("Error :", e)

#=====================================================================================
#=====================================================================================

print("\n\nQ10. Mini Project - Smart Calculator & Data Manager")

# Importing required modules
import math
import random
from datetime import datetime

# Dictionary to store calculation history
history = {}

# Variable to store latest result
result = None

# Running menu until user exits
while True:

    print("\n1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Numbers")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")

    try:

        # Taking menu choice
        choice = int(input("Enter your choice: "))

        # Basic Arithmetic
        if choice == 1:

            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            operation = int(input("Enter operation: "))

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == 1:
                result = num1 + num2

            elif operation == 2:
                result = num1 - num2

            elif operation == 3:
                result = num1 * num2

            elif operation == 4:
                result = num1 / num2

            else:
                print("Invalid operation!")
                continue

            print("Result =", result)

        # Scientific Calculations
        elif choice == 2:

            print("\n1. Square Root")
            print("2. Power")

            operation = int(input("Enter operation: "))

            if operation == 1:

                num = float(input("Enter number: "))
                result = math.sqrt(num)

            elif operation == 2:

                base = float(input("Enter base: "))
                power = float(input("Enter power: "))
                result = math.pow(base, power)

            else:
                print("Invalid operation!")
                continue

            print("Result =", result)

        # Generate Random Numbers
        elif choice == 3:

            result = []

            # Generating 5 random numbers
            for i in range(5):
                result.append(random.randint(1, 100))

            print("Random Numbers =", result)

        # Store latest result with current time
        elif choice == 4:

            if result == None:
                print("No result available to store.")

            else:
                time = str(datetime.now())
                history[time] = result
                print("Result stored successfully.")

        # Display calculation history
        elif choice == 5:

            if len(history) == 0:
                print("No history found.")

            else:

                print("\nHistory")

                for key, value in history.items():

                    print("Time   :", key)
                    print("Result :", value)
                    print()

        # Exit program
        elif choice == 6:

            print("Program Closed Successfully.")
            break

        else:
            print("Invalid choice!")

    # Handling invalid number input
    except ValueError:
        print("Please enter valid numbers.")

    # Handling division by zero
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

#=====================================================================================
#=====================================================================================

