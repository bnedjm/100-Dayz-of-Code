#Functions with outputs.

def format_name_1(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name_1("leo", "MESSI"))

#Functions with multiple return values.

def format_name_2(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You did not provide a valid input!"
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result : {formated_f_name} {formated_l_name}"

print(format_name_2(input("What is your first name?\t"), input("What is your last name?\t")))

#Already used functions with outputs.

formatted_name = format_name_2(input("What is your first name?\t"), input("What is your last name?\t"))
length = len(formatted_name)
