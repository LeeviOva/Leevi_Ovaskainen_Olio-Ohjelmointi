
list = [] 
negatives = 0
i = 0
even = 0

while True:
    user_input = input("Please insert an integer: ")
    user_input = int(user_input)
    list.append(user_input)
    
    if list[i] < 0:
        negatives = negatives + 1
    if list[i] % 2 == 0 and list[i] != 0:
        even = even + 1
    if user_input == 0:
        break
    i = i +1

    
print("Number of negative integers is: ", negatives)
print("Number of even numbers: ", even)