'''
count the number of occurences of the letter 't' in a string.
'''

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(sum([1 for i in statement1 if i == 't']))

# again there is an easier built-in solution to this using a string method. this time it is .count().

print(statement1.count('t'))
print(statement2.count('t'))