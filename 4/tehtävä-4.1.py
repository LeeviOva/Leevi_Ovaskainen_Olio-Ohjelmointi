class ListHelper:

    def greatest_frequency(my_list: list()):
        if not my_list:
            return None
        mcount = 0
        most_common_item = None
        for item in my_list:
            count = my_list.count(item)
            if count > mcount:
                max_count = count
                most_common_item = item
        return most_common_item


    def doubles(my_list: list):
        if not my_list:
            return 0 
        unique_items = set(my_list)
        count = 0
        for item in unique_items:
            if my_list.count(item) >= 2:
                count += 1 
        return count


numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))