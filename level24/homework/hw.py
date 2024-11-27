def custom_split(string, delimiter):
    result = []
    word = ''
    for char in string:
        if char == delimiter:
            result.append(word)
            word = ''
        else:
            word += char
    result.append(word)  # To append the last word after the loop ends
    return result
string = "Hello,World,Python"
print(custom_split(string, ','))  # Output: ['Hello', 'World', 'Python']
