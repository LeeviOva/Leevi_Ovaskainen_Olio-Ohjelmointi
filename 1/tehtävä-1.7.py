def apmax():
    while True:
        apmax_value = 0
        user_input = input("Please insert an integer divisible by 3: ")
        user_input = int(user_input)

        if user_input % 3 == 0 and user_input != 0:
            apmax_value = user_input
            break
        else:
            print("Integer wasn't divisible by 3")
    return apmax_value

def approg(apmax_value):
    ap = 0
    apsum = 0
    terms = 0
    while ap < apmax_value:
        terms = terms + 1
        ap = ap + 3
        apsum = apsum + ap
    print("Sum of numbers in AP: ", apsum)
    print("Number of terms in AP: ", terms)

def appsqr(apmax_value):
    ap = 0
    apsqr = 0
    while ap < apmax_value:
        ap = ap + 3
        apsqr = apsqr + (ap ** 2)
    print("Sum of squared parts of AP:", apsqr)

# Call apmax and store the result
max_value = apmax()

# Call other functions with the result from apmax
approg(max_value)
appsqr(max_value)
