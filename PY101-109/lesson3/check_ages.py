'''
check if "Spot" is in the dictionary ages
'''
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print("Spot" in ages.keys())

# this again can be done more simply by just calling the below

"Spot" in ages


# add keys to the dictionary ages

additional_ages = {'Marilyn': 22, 'Spot': 237}

# ORIGINAL SOLUTION

#for key in additional_ages:
#    ages[key] = additional_ages[key]

# print(f"{ages = }")

# and yet again we have a simpler solution, if we want to update a dictionary with another dictionary we can just use the update() method.

ages.update(additional_ages)

print(f"{ages = }")