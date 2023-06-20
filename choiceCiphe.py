# project to convert to either ASCII or morse code to get practice with functions, loops, conditionals, dictionaries, and ciphers.

# morse dictionary for lowercase letters
morseDict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}

# execute ASCII encryption; no return type due to multiple steps
def translateAscii(msg):
  encryptedMsg = ''
  # converts each character to ASCII
  for i in range(len(msg)):
    ascii = ord(msg[i])
    encryptedMsg += str(ascii) + " "
  # asks user to add a key
  keyYN = input("Your encrypted message is: " + encryptedMsg + ". \nWould you like to add an encryption key? ")
  if (keyYN == "yes" or keyYN == "Yes" or keyYN == "YES"):
    key = int(input("What key would you like to use? "))
    # adds the key to each ASCII number for each character
    newMsg = ''
    newMsgLetters = ''
    for i in range (len(msg)):
      # ensure spaces stay the same; only translates letters
      if (msg[i] == " "):
        newMsg += " "
        newMsgLetters += " "
      else:
        asciiKey = ord(msg[i]) + key
        # wraps around to make sure everything is a letter
        while asciiKey > ord('z'):
          asciiKey -= 26
        newMsg += str(asciiKey) + " "
        newMsgLetters += chr(asciiKey)
    print("Your new message is: " + str(newMsg) + ". In letters, your new message is: " + str(newMsgLetters))
  else:
    print("You have chosen not to add a key.")

# execute Morse code encryption
def translateMorse(msg):
    morseMsg = ""
    for char in msg:
      if char == " ":
        morseMsg += "  "
      else:
        morseMsg += morseDict[char] + " "
    return morseMsg

method = input("You can either make a message in ASCII or morse code. By default, the encryption type will be morse code. Type in your preferred encryption method: ")
msg = input("What is the message you want to encrypt? (please type in all lowercase) ")
print("Encrypting...")
if (method == "ASCII" or method == "ascii"):
  translateAscii(msg)
else:
  print("Your morse code message is: " + translateMorse(msg))