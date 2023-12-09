# write data to files

file = open("testing.txt", "w")                 # opened a file with writing mode
file.write('testing file handling in python')   # added text in file
file.close()                                    # closed the file (imp to avoid mem leaks)

with open("testing.txt", "a+") as file:         # 'with' keyword doesnt require closing the file (using append+ mode here)
    file.write("\nadding some additional text") # appended text to file
    file.seek(0)                                # moved file cursor to first line
    content = file.read()                       # var to store info in file

print(content)                                  # printed file content