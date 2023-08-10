#Calculator
from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Devide
def devide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : devide,
}

def calculator():
  print(logo)
  nbr_1 = float(input("What is the first number?\t"))
  
  for operation in operations:
    print(operation)
  
  repeat = True
  
  while repeat:
    operation_symbol = input("Pick an operation:\t")
    nbr_2 = float(input("What is the next number?\t"))
    
    result = round(operations[operation_symbol](nbr_1, nbr_2), 1)
    print(f"{nbr_1} {operation_symbol} {nbr_2} = {result}")
    
    again = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation.\t")
    if again == "n":
      repeat = False
      calculator()
    elif again == "y":
      nbr_1 = result

calculator()
