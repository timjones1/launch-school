def greetings(name_list, job_dict):

    name = " ".join(name_list)
    title = job_dict.get("title")
    occupation = job_dict.get("occupation")

    return f"Hello, {name}! Nice to have a {title} {occupation} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
