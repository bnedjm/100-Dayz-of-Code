# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

with open("./Input/Names/invited_names.txt") as names_file:
    names_contents = names_file.readlines()

for name in names_contents:
    stripped_name = name.strip("\n ")
    new_letter = letter_contents.replace(PLACEHOLDER, f"{stripped_name}")
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as RTSend:
        RTSend.write(new_letter)