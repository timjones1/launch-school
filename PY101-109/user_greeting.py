def ends_with_exclamation(name):
    return name[-1] == "!"


input_name = input("what is your name?")

if ends_with_exclamation(input_name):
    print(f"HELLO {input_name.upper()}!, WHY ARE WE YELLING?")
else: print(f"Hello {input_name}")



#def has_exclamation(name):
#    return "!" in name

# checking solutions this has an issue, we are supposed to be checking if 
# the string endswith an !, currently it just checks if there is an ! in the 
# string. update the has_exclamation function to check if the string ends with
# an !. 