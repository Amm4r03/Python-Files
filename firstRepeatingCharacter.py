def first_repeating_char(s):
    seen_chars = set()
    for char in s:
        if char in seen_chars:
            return char
        seen_chars.add(char)
    return None

s = input("enter a string : ")
result = first_repeating_char(s)

if result is not None:
    print(f"First repeating character: {result}")
else:
    print("No repeating character found.")