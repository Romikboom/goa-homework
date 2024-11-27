list_of_odd = []
list_of_even = []
for number in range(1, 1001):
    if number % 2 == 0: 
        list_of_even.append(number)
    else: 
        list_of_odd.append(number)
print("კენტი ციფრები:", list_of_odd)
print("ლუწი ციფრები:", list_of_even)
