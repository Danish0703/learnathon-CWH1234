# Demonstrating various string methods

sample_string = "  Hello, World! 123 "

# upper() - Converts the string to uppercase
upper_string = sample_string.upper()
print("Uppercase:", upper_string)

# lower() - Converts the string to lowercase
lower_string = sample_string.lower()
print("Lowercase:", lower_string)

# partition() - Returns a tuple
partitioned_string = sample_string.partition(";")
print("Partitioned:", partitioned_string)

# replace() - Replaces substring inside
replaced_string = sample_string.replace("World", "hyderabad")
print("Replaced:", replaced_string)

# find() - Returns the index of the first occurrence of substring
found_index = sample_string.find("World")
print("Found index:", found_index)

# rstrip() - Removes trailing characters
rstrip_string = sample_string.rstrip()
print("Rstrip:", rstrip_string)

# split() - Splits string from left
split_string = sample_string.split()
print("Split:", split_string)

# startswith() - Checks if string starts with the specified string
startswith_check = sample_string.startswith("  Hello")
print("Startswith '  Hello':", startswith_check)

# isnumeric() - Checks numeric characters
numeric_check = sample_string.isnumeric()
print("Is numeric:", numeric_check)

# index() - Returns index of substring
index_of_substring = sample_string.index("World")
print("Index of 'World':", index_of_substring)
