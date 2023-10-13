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
    converted_message =  ""
    for char in message:
        if char == " ":
            converted_message += " "
            continue
        converted_message += MORSE_CODE_DICT[char]
    return converted_message

def morse_text_converter(code):
    pass

user_op = int(input("Which type of conversion do you want to perform?\n1 - text_morse\n2 - morse_text\n3 - Quit\n"))
print(user_op)
while(user_op != 3):
    if user_op == 1:
        user_message = input("Enter the text that you want to convert.\n")
        print(text_morse_converter(user_message))
    elif user_op == 2:
        user_code = input("Enter the morse code that you want to convert.\n")
        print(morse_text_converter(user_code))
    
    user_op = input("What operation do you wanna perform next?\n1 - text_morse\n2 - morse_text\n3 - Quit\n")
