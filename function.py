# Inbuilt functions
number = min(23, 45, 656, 56, 34)
print(number)

y = max(43, 54, 165, 23, 56)
print(y)

z = pow(2, 3)
print(z)


# User defined function
def name():
    print("Dennis")


name()  # Calling a funtion


def details():
    name = "Deno"
    age = 18
    course = "MIT"
    print(name, age, course)


details()


# Parameters/variables and argument/values
def patient(name, gender, age, marriage_status):
    print(name, gender, age, marriage_status)


patient("Job", "male", 27, "single")
patient("Mary", "female", 32, "married")


def multiply(x, y):
    print(x * y)


multiply(3, 4)
multiply(13, 14)
multiply(32, 41)
multiply(32, 34)


def employees(fullname, age, position, salary):
    print(fullname, age, position, salary)


employees("Ian Matasi", 39, "CEO", "Sh 120000")
employees("John Wick ", 47, "Managing Director", "Sh 100000")
employees("Shannel Shanz", 26, "Secretary", "Sh 50000")
employees("Frank Walter", 25, "Instructor", "Sh 10000")
employees("Deborah Williams", 28, "Cleaner", "Sh 12000")
employees("Cian Cean", 30, "Security", "Sh 15000")
