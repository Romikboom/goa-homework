def custom_join(lst, delimiter):
    result = ''
    for i in range(len(lst)):
        result += lst[i]
        if i != len(lst) - 1:  # Don't add delimiter after the last element
            result += delimiter
    return result
lst = ['Hello', 'World', 'Python']
print(custom_join(lst, ','))  # Output: 'Hello,World,Python'
