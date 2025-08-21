# Demonstration of variables, constraints, and print function

# Variables
age = 22
name = "Mutsa"
salary = 10000.0

# Constraints
if age >= 18:
    status = "Grownup"
else:
    status = "Minor"

if salary > 1000:
    income_level = "Above average"
else:
    income_level = "Below average"

# results
print("Name:", name)
print("Age:", age, "-", status)
print("Salary:", salary, "-", income_level)
