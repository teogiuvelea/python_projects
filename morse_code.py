# Step 1: Create a dictionary with numbers 0-9 and all alphabet letters and assign for each corresponding letter/number its counter part morse symbol as value.
# import string


# print(list(string.digits))
# print(list(string.ascii_lowercase))
# print(list(string.punctuation))

from symbols import morse_symbols


def encode_message(message): 
    encoded_msg = ''
    for letter in message.lower():
        if letter in morse_symbols:
            symbol = morse_symbols[letter] + ' '
            encoded_msg += symbol
    return encoded_msg       


def decipher_morse_code(message):
    symbols_tuple = [(item, morse_symbols[item]) for item in morse_symbols]
    decoded_message = ''
    message = message.split('  ')
    msg_ls = [item.split() for item in message]
    for item in msg_ls:
        for symbol in item:
            for item in symbols_tuple:
                if item[1] == symbol:
                    decoded_message += item[0] 
        decoded_message += ' '             
    return decoded_message


def command():
    while True:
        print("Morse Code \nType encode to encrypt message or \nType decode to decrypt message or \nType quit to exit program")
        cmd = input('>>> ')
        if cmd == 'encode':
            message_to_encode = input("Message to encode: ")
            print(encode_message(message_to_encode)) 
            print('\n')
        elif cmd == 'decode':
            message_to_decode = input("Message to decode: ")  
            print(decipher_morse_code(message_to_decode))  
            print('\n') 
        elif cmd == 'quit':
            break    
        else:
            print("Don't understand your command. Let's try again!")


command()