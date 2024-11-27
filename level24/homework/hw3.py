def custom_replace(string, old, new):
    result = ''
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)  # Skip the length of the old string
        else:
            result += string[i]
            i += 1
    return result
string = "Hello World"
print(custom_replace(string, "World", "Python"))  # Output: 'Hello Python'
