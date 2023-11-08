def my_function(*args, **kwargs):
    values_list = list(kwargs.values())
    count = 0

    for arg in args:
        count += values_list.count(arg)

    return count

result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)  # 3
