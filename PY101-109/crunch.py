def crunch(input_string):
    
    prev_char = ""
    return_string = ""
    for c in input_string:
        if c != prev_char:
            return_string = return_string + c   
        prev_char = c

    return return_string

# print(crunch("ddaaiilly") == "daily")
# # These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

print("!" + "     text with spaces          ".strip() + "!")