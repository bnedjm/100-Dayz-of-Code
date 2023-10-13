from art import tprint

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
        morse_code += MORSE_CODE_DICT[char] + " "
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


def main():
    tprint("JUST  MORSE  IT")
    user_op = int(input("Which type of conversion do you want to perform?\n1 - text_morse\n2 - morse_text\n3 - Quit\n"))
    while(user_op != 3):
        if user_op == 1:
            user_message = input("Enter the text that you want to convert.\n")
            print(text_morse_converter(user_message))
        elif user_op == 2:
            user_code = input("Enter the morse code that you want to convert.\n")
            print(morse_text_converter(user_code))
        
        user_op = int(input("What operation do you wanna perform next?\n1 - text_morse\n2 - morse_text\n3 - Quit\n"))

# if "__name__" == "__main__":
#     main()
main()
