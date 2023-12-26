

# Creating a dictionary with multiple inputs for keys
data = {
    (1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
    (2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
    (3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
    (4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
}

print(data[(1, "John", "Doe")]["a"])
data[(1, "John", "Doe")]["a"]={"f": "for", "g": 90000}
print(data[(1, "John", "Doe")]["a"])
