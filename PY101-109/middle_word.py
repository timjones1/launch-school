def middle_word(string):
    
    words = string.split()

    if len(words) == 0:
        return ""
    
    if len(words) == 1:
        return words[0]

    middle = len(words) // 2 
    
    if len(words) % 2 == 1:
        return words[middle]
    else:
        return [words[middle-1], words[middle]]

print(middle_word("last word before i sleep"))
print(middle_word("one two three four"))
