from logo import logo

MORSE_CODE_DICT = {"A":".-",
                   "B":"-...",
                   "C":"-.-.", 
                   "D":"-..", 
                   "E":".", 
                   "F":"..-.", 
                   "G":"--.", 
                   "H":"....", 
                   "I":"..", 
                   "J":".---", 
                   "K":"-.-",
                   "L":".-..", 
                   "M":"--", 
                   "N":"-.",
                   "O":"---", 
                   "P":".--.", 
                   "Q":"--.-",
                   "R":".-.", 
                   "S":"...", 
                   "T":"-", 
                   "U":"..-", 
                   "V":"...-", 
                   "W":".--", 
                   "X":"-..-", 
                   "Y":"-.--", 
                   "Z":"--..", 
                   "1":".----", 
                   "2":"..---", 
                   "3":"...--", 
                   "4":"....-", 
                   "5":".....", 
                   "6":"-....", 
                   "7":"--...", 
                   "8":"---..", 
                   "9":"----.", 
                   "0":"-----", 
                   ", ":"--..--", 
                   ".":".-.-.-", 
                   "?":"..--..", 
                   "/":"-..-.", 
                   "-":"-....-", 
                   "(":"-.--.", 
                   ")":"-.--.-"
                   }

def text_morse_converter(message):
    message = message.upper()
    morse_code =  ""
    for char in message:
        if char == " ":
            morse_code += " "
            continue
        for key, value in MORSE_CODE_DICT.items():
            if char == key:
                morse_code += value + " "
    return morse_code

def morse_text_converter(morse_code):
    morse_code = morse_code.split(" ")
    message =  ""
    for code in morse_code:
        if code == "":
            message += " "
            continue
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                message += key
    return message

def get_user_operation():
    options = [1, 2, 3]
    try:
        user_op = int(input("Which type of conversion do you want to perform?\n1 - text_morse\n2 - morse_text\n3 - Quit\n"))
        if user_op not in options:
            print("Invalid input. Try again!\n")
            get_user_operation()
    except ValueError:
        print("Invalid input. Try again!\n")
        get_user_operation()
    else:
        return user_op
    
def main():
    print(logo)
    user_op = get_user_operation()
    while(user_op != 3):
        if user_op == 1:
            user_message = input("Enter the text that you want to convert.\n")
            print(f"The morse code from your text is: {text_morse_converter(user_message)}\n")
        elif user_op == 2:
            user_code = input("Enter the morse code that you want to convert.\n")
            print(f"The text from your morse code is: {morse_text_converter(user_code)}\n")
        user_op = get_user_operation()

main()
