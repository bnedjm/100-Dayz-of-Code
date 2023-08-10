alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift):
  cipher_text = ''
  for char in plain_text:
      org_idx = alphabet.index(char)
      shifted_idx = org_idx + shift
      if shifted_idx >= len(alphabet):
          shifted_idx -= len(alphabet)
      cipher_text += alphabet[shifted_idx]
  print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for char in cipher_text:
    org_idx = alphabet.index(char)
    shifted_idx = org_idx - shift
    if shifted_idx < 0:
      shifted_idx += len(alphabet)
    plain_text += alphabet[shifted_idx]
  print(f"The decoded text is {plain_text}")
  
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
direction = direction.lower()
if direction == 'encode':
  encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
  decrypt(cipher_text = text, shift_amount = shift)
