# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello")
  print("How do you do?")
  print("The weather is nice today, innit?")

greet()

#Function that allows for input
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
  print("The weather is nice today, innit?")

greet_with_name("Angie")

#Function with more than 1 input

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"How is the weather in {location}")

greet_with("Tina", "Frankfurt")

#positional arguments
greet_with("Somewhere", "ME") 

#keyword arguments
greet_with(location = "somewhere",name = "Nedjm")
