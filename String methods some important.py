# Define a sample string
sample_string = "  Hello, World! Welcome to Python Programming.  "
sample_list = ["Hello", "World", "Python", "Programming"]

# strip, lstrip, rstrip
print(sample_string.strip())  # "Hello, World! Welcome to Python Programming."
print(sample_string.lstrip()) # "Hello, World! Welcome to Python Programming.  "
print(sample_string.rstrip()) # "  Hello, World! Welcome to Python Programming."

# split
print(sample_string.split())  # ['Hello,', 'World!', 'Welcome', 'to', 'Python', 'Programming.']

# join
print(' '.join(sample_list))  # "Hello World Python Programming"

# replace
print(sample_string.replace("World", "Universe"))  # "  Hello, Universe! Welcome to Python Programming.  "

# find, rfind
print(sample_string.find("Welcome"))  # 15
print(sample_string.rfind("o"))       # 40

# startswith, endswith
print(sample_string.startswith("  Hello"))  # True
print(sample_string.endswith("Programming.  "))  # True

# lower, upper, capitalize, title, swapcase
print(sample_string.lower())  # "  hello, world! welcome to python programming.  "
print(sample_string.upper())  # "  HELLO, WORLD! WELCOME TO PYTHON PROGRAMMING.  "
print(sample_string.capitalize())  # "  hello, world! welcome to python programming.  "
print(sample_string.title())  # "  Hello, World! Welcome To Python Programming.  "
print(sample_string.swapcase())  # "  hELLO, wORLD! wELCOME TO pYTHON pROGRAMMING.  "

# format (using .format() and f-strings)
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # "My name is Alice and I am 30 years old."
print(f"My name is {name} and I am {age} years old.")  # "My name is Alice and I am 30 years old."

# count
print(sample_string.count("o"))  # 4

# isdigit, isalpha, isalnum, isspace
numeric_string = "12345"
alpha_string = "HelloWorld"
alnum_string = "Hello123"
space_string = "   "

print(numeric_string.isdigit())  # True
print(alpha_string.isalpha())    # True
print(alnum_string.isalnum())    # True
print(space_string.isspace())    # True

# Using join to concatenate list elements into a single string
separator = ", "
print(separator.join(sample_list))  # "Hello, World, Python, Programming"
