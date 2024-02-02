def smallest_average(person1: dict, person2: dict, person3: dict):
    avg1 = (person1['result1'] + person1['result2'] + person1['result3']) / 3
    avg2 = (person2['result1'] + person2['result2'] + person2['result3']) / 3
    avg3 = (person3['result1'] + person3['result2'] + person3['result3']) / 3

    if avg1 < avg2 and avg1 < avg3:
        return person1
    elif avg2 < avg1 and avg2 < avg3:
        return person2
    else:
        return person3

def main():
    person1 = {
        'name': "Masa",
        'result1': 1,
        'result2': 2,
        'result3': 3
    }
    person2 = {
        'name': "l",
        'result1': 2,
        'result2': 3,
        'result3': 4
    }
    person3 = {
        'name': "j",
        'result1': 3,
        'result2': 4,
        'result3': 5
    }

    result = smallest_average(person1, person2, person3)
    print(f"The person with the smallest average is: {result['name']} Result 1: {result["result1"]} Result 2: {result["result2"]} Result 3: {result["result3"]}")

if __name__ == "__main__":
    main()
