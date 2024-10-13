munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"


mess_with_demographics(munsters)

print(f"{munsters = }")

# i predicted that this wouldnt update the underlying data as during line 10 
# the items are unpacked from the dictionary before being updated, but this is
# incorrect and the dictionary objects being unpacked are mutable and are passed
# by Object reference inside Munsters. When they are updated using slicing notation
# the original dictionary is also updated.

