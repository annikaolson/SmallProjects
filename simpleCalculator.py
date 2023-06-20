#####################
## Calculator tool ##
#####################
import random

# addition of two numbers (1)
def add(num1, num2):
  sum = num1 + num2
  return sum

# subtraction of two numbers (2)
def sub(num1, num2):
  diff = num1 - num2
  return diff

# multiply two numbers (3)
def mult(num1, num2):
  product = num1 * num2
  return product

# divide two numbers (4)
def div(num1, num2):
  quotient = num1 / num2
  return quotient

# factorial (5)
def factorial(num):
  product = 1
  for i in range(1, num + 1):
    product*=i
  return product

# take a number to the nth power (6)
def toThePower(num, n):
  power = num ** n
  return power

# take the nth root of any number (7)
def root(num, n):
  root = num ** (1/n)
  return root

# create wording at the top
intro = "**Welcome to your Calculator app!**"
starMsg = ''
for i in range (len(intro)):
  starMsg+="*"
print(starMsg)
print(intro)
print(starMsg)
# the options of operations
menu = "Menu:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Factorial\n6. Exponentiation\n7. Find the nth root\nAny other number: Random operation!"
print(menu)
op = int(input("What operation would you like to perform? "))
res = 0
# choose random operation
if (op != 1 and op != 2 and op != 3 and op != 4 and op != 5 and op != 6 and op!= 7):
  op = random.randint(1,7)
# choose operation
if (op == 1 or op == 2 or op == 3 or op == 4):
  num1 = float(input("Provide the first number of the operation: "))
  num2 = float(input("Provide the second number of the operation: "))
  if (op == 1):
    res = add(num1, num2)
  elif (op == 2):
    res = sub(num1, num2)
  elif (op == 3):
    res = mult(num1, num2)
  elif (op == 4):
    res = div(num1, num2)
elif (op == 5):
  num = int(input("Provide the number you would like to take the factorial of: "))
  res = factorial(num)
elif (op == 6):
  num = float(input("Provide the base: "))
  n = float(input("Provide the exponent: "))
  res = toThePower(num, n)
elif (op == 7):
  num = float(input("Provide the base: "))
  n = float(input("Provide the root number: "))
  res = root(num, n)

# show the user what the answer is
print("Your result is " + str(res) + ".\nThank you for using the app! See you next time!")