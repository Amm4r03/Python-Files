# taking input from user
message = input("enter the encrypted message to be decrypted : ")

# initialising set of all allowed characters
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# brute forcing all possible keys
for key in range(len(SYMBOLS)):                 # code runs for the length of all symbols in SYMBOLS
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            # handle wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    # print all iterations
    print("key : {} message : {}\n".format(key, translated))