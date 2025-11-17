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
from collections import OrderedDict

my_dict = OrderedDict()
my_dict['a'] = 1
my_dict['b'] = 2 
my_dict['c'] = 3 
my_dict['d'] = 4 
my_dict['e'] = 5 

print(my_dict)
for (k, v) in my_dict.items():
	print(f"k={k} v={v}")