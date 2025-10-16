import random
rand_list = [random.randint(1, 20) for _ in range(10)]

list_comprehension_below_10 = [num for num in rand_list if num < 10]

list_comprehension_below_10_with_filter = list(filter(lambda n: n < 10, rand_list))

print(rand_list, list_comprehension_below_10, list_comprehension_below_10_with_filter)