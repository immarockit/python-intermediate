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

################################################
def p():
	print("Hey")

from collections import namedtuple
Point = namedtuple('Point', 'x,y,z')
pt = Point(1, p, 5)
print(pt.y())
