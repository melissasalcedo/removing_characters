# Remove first n characters from a string

print("Removing characters from a string")

# Function
def remove_chars(origstring, number_to_remove ):
    print('Original string:', origstring)
    result_string = origstring[number_to_remove:]
    return result_string
    

# Test cases
print(remove_chars("mishkamushka", 9))
print(remove_chars("mishkamushka", 3))
