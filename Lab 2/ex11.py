def order_tuples(lst):
    def custom_key(item):
        if len(item) >= 2 and len(item[1]) >= 3:
            return item[1][2]
        else:
            return None

    sorted_lst = sorted(lst, key=custom_key)
    return sorted_lst

# Example usage
tuples_list = [('abc', 'bcd'), ('abc', 'zza')]

sorted_tuples = order_tuples(tuples_list)
print(sorted_tuples)
