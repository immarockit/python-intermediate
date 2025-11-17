# from collections import Counter

# a = "aaaaaaabbbcccc"
# my_counter = Counter(a)
# print(my_counter)
# e = my_counter.elements()
# while (True):
# 	try:
# 		print(next(e))
# 	except StopIteration:
# 		break
# ################################################
# from collections import Counter

# a = "aaaaaaabbbcccc"
# my_counter = Counter(a)

# for element in my_counter.elements():
#     print(element)

# ################################################
# def p():
# 	print("Hey")

# from collections import namedtuple
# Point = namedtuple('Point', 'x,y,z')
# pt = Point(1, p, 5)
# print(pt.y())


# ################################################
# from collections import OrderedDict

# my_dict = OrderedDict()
# my_dict['a'] = 1
# my_dict['b'] = 2 
# my_dict['c'] = 3 
# my_dict['d'] = 4 
# my_dict['e'] = 5 

# print(my_dict)
# for (k, v) in my_dict.items():
# 	print(f"k={k} v={v}")

# cache = OrderedDict()

# # simulate usage
# cache['a'] = 1
# cache['b'] = 2

# # Access 'a'
# cache.move_to_end('a')
# cache.popitem(last=False)  # pops the first-inserted item

# print(cache)

# ################################################

# from collections import defaultdict

# # default value is int() → 0
# my_dict = defaultdict(int)

# # Manually assigned values (normal behavior)
# my_dict['a'] = "sss"
# my_dict['b'] = 2 
# my_dict['c'] = 3 
# my_dict['d'] = 4 
# my_dict['e'] = 5 

# print("=== Normal Items ===")
# for (k, v) in my_dict.items():
#     print(f"k={k} v={v}")

# print("\n=== Accessing Missing Keys (defaultdict behavior) ===")

# # Access some missing keys to show how defaultdict helps
# print("Accessing missing key 'z':", my_dict['z'])   # becomes 0 automatically
# print("Accessing missing key 'y':", my_dict['y'])   # becomes 0 automatically

# print("\n=== Dictionary After Accessing Missing Keys ===")
# for (k, v) in my_dict.items():
#     print(f"k={k} v={v}")

###########################################################
from collections import deque

dq = deque([1, 2, 3])
print("Initial deque:", dq)

dq.append(4)         # add to end
dq.appendleft(0)     # add to front
print("After append/appendleft:", dq)

dq.pop()             # remove from end
dq.popleft()         # remove from front
print("After pop/popleft:", dq)

dq.extend([5,6,7])   # add multiple to end
dq.extendleft([-2,-1])  # add multiple to front
print("After extend/extendleft:", dq)

dq.rotate(2)         # rotate right by 2
print("After rotate(2):", dq)

dq.rotate(-3)        # rotate left by 3
print("After rotate(-3):", dq)
