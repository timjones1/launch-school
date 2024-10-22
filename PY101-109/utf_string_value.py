def utf16_value(utf_string):
    
    total_value = 0
    
    for character in utf_string:
        total_value+= ord(character)
    
    return total_value

print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

# again many user solutions used list comprehensions.

def utf16_value_usr(utf_string):
    return sum([ord(utf_char) for utf_char in utf_string])

print(utf16_value_usr(OMEGA) == 937)
print(utf16_value_usr(OMEGA + OMEGA + OMEGA) == 2811)