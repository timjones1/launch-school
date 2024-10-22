def middle_word(string):
    
    words = string.split()

    if len(words) == 0:
        return ""
    
    if len(words) == 1:
        return words[0]

    if len(words) % 2 == 1:
        middle = len(words) // 2 
        return words[middle]
    else:
        middle = len(words) // 2 -1
        return [words[middle],words[middle+1]]

print(middle_word("last word before i sleep"))
print(middle_word("one two three four"))
