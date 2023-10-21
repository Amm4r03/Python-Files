# code for caesar cipher in python

mode = int(input('1 : encrypt a message\n2 : decrypt a message\nchoose a mode : '))

inputText = input('Enter a message : ')

key = int(input('Enter the encryption/decryption key : '))

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'      # all caps variables are treated as constants

translated = ''

for symbol in inputText:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        
        if mode == 1:
            translatedIndex = symbolIndex + key
        else:
            translatedIndex = symbolIndex - key
        
        # handling index wraparound
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex <0 :
            translatedIndex = translatedIndex + len(SYMBOLS)
            
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol

print("input : {}\nkey : {}\noutput : {}".format(inputText, key, translated))