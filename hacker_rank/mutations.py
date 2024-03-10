def mutate_string(string, position, character):
    x = position 
    y = position + 1
    z = character
    string = string[:x] + z + string[y:]
    return string
