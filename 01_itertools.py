################################################################
# from itertools import product
# A = [1, 2]
# B = ['x', 'y']
# for pair in product(A, B):
#     print(pair)

################################################################
# from collections import defaultdict, deque
# from itertools import product

# # Step 1: Group items into categories using defaultdict
# categories = defaultdict(deque)
# categories['fruits'].extend(['apple', 'banana', 'orange'])
# categories['colors'].extend(['red', 'yellow', 'green'])

# print("Categories:")
# for cat, items in categories.items():
#     print(f"{cat}: {list(items)}")

# # Step 2: Compute the Cartesian product between 'fruits' and 'colors'
# pairs = list(product(categories['fruits'], categories['colors']))

# print("\nAll possible fruit-color pairs (Cartesian product):")
# for p in pairs:
#     print(p)

################################################################
# from collections import defaultdict, deque
# from itertools import product

# # Step 1: Create a cache using defaultdict(deque)
# # Each key will store recent items (maxlen=3)
# cache = defaultdict(lambda: deque(maxlen=3))

# # Simulate adding some data to cache
# cache['user1'].append('pageA')
# cache['user1'].append('pageB')
# cache['user1'].append('pageC')

# cache['user2'].append('pageX')
# cache['user2'].append('pageY')

# print("Cache content:")
# for user, pages in cache.items():
#     print(f"{user}: {list(pages)}")

# # Step 2: Generate all possible pairs of recently visited pages for each user
# print("\nAll possible pairs of recently visited pages (Cartesian product):")
# for user, pages in cache.items():
#     pairs = list(product(pages, repeat=2))  # pairs including duplicates
#     print(f"{user}: {pairs}")



##################################################################
# from itertools import permutations

# items = [1, 2, 3]

# # All permutations of length 2
# for p in permutations(items, 2):
#     print(p)



##################################################################
# from itertools import permutations, product

# items = [1, 2, 3]

# # Permutations of length 2 (no repetition)
# perm = list(permutations(items, 2))
# print("Permutations of length 2 (no repetition):")
# print(perm)
# print(f"Total tuples: {len(perm)}\n")

# # Cartesian product of length 2 (repetition allowed)
# prod = list(product(items, repeat=2))
# print("Product of length 2 (repetition allowed):")
# print(prod)
# print(f"Total tuples: {len(prod)}")



##################################################################
# from itertools import combinations

# items = [1, 2, 3]

# # All combinations of length 2
# comb = list(combinations(items, 2))
# print("Combinations of length 2 (order doesn't matter):")
# print(comb)
# print(f"Total tuples: {len(comb)}")


##################################################################
# from itertools import combinations_with_replacement

# items = [1, 2, 3]

# comb_wr = list(combinations_with_replacement(items, 2))
# print("Combinations with replacement of length 2:")
# print(comb_wr)
# print(f"Total tuples: {len(comb_wr)}")


##################################################################
# from itertools import accumulate
# import operator

# nums = [1, 3, 2, 5, 4]

# # ---------------------------
# # Running sum
# running_sum = list(accumulate(nums))
# print("Running sum:     ", running_sum)

# # ---------------------------
# # Running product
# running_product = list(accumulate(nums, func=operator.mul))
# print("Running product: ", running_product)

# # ---------------------------
# # Running maximum
# running_max = list(accumulate(nums, func=max))
# print("Running max:     ", running_max)

# # ---------------------------
# # Running minimum
# running_min = list(accumulate(nums, func=min))
# print("Running min:     ", running_min)

# # ---------------------------
# # Running custom function: difference
# # Each step: previous - current
# running_diff = list(accumulate(nums, func=lambda x, y: x - y))
# print("Running difference:", running_diff)


##################################################################
# from itertools import groupby

# data = [1, 1, 2, 2, 2, 3, 1, 1]

# print(list(groupby(data)))
# # Group consecutive identical elements
# for key, group in groupby(data):
#     print(key, list(group))

# # Group by even or odd
# for key, group in groupby(data, key=lambda x: x % 2):
#     print(key, list(group))

# # Group by smaller_than_3 function
# def smaller_than_3(x):
#     return x < 3

# numbers = [1, 2, 3, 1, 4, 2, 5]
# grouped_custom = [(key, list(group)) for key, group in groupby(numbers, key=smaller_than_3)]
# print("Group by smaller_than_3:", grouped_custom)



# ##################################################################
# from itertools import groupby

# # Example data: list of people with ages
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 27},
#     {"name": "Charlie", "age": 35},
#     {"name": "David", "age": 22},
#     {"name": "Eve", "age": 40},
#     {"name": "Frank", "age": 28},
# ]

# # Sort by age to make groupby meaningful
# people.sort(key=lambda x: x["age"])

# # Custom function: True if age < 30
# def younger_than_30(person):
#     return person["age"] < 30

# # Group by age < 30
# grouped = [(key, list(group)) for key, group in groupby(people, key=younger_than_30)]

# # Print results
# for key, group in grouped:
#     status = "<30" if key else ">=30"
#     names = [p["name"] for p in group]
#     print(f"Age group {status}: {names}")


########################################################
# from itertools import count

# # Count from 10, step 2
# for i in count(10, 2):
#     if i > 20:
#         break
#     print(i, end=" ")

########################################################
# from itertools import cycle

# colors = ["red", "green", "blue"]
# n = 7
# i = 0
# for c in cycle(colors):
#     if i >= n:
#         break
#     print(c, end=" ")
#     i += 1


########################################################
# from itertools import repeat

# # Repeat a value 5 times
# for x in repeat("hello", 5):
#     print(x, end=" ")




