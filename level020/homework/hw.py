import time

# დეფინირება ტექსტისა და რაოდენობის
text = "love"
count = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000  # მილიარდი

# პროცედურა, რაც დაწერს "love" დიდ რაოდენობით
def write_love():
    result = text *count
    return result



# გაწვდეთ "love"-ი დიდ რაოდენობით
write_love()

end_time = time.time()

