
from functools import reduce


# ============================================================
# 1. Basic Lambda Function
# ============================================================

print("\n1. Basic lambda function:")
square = lambda x: x * x
print("square(5) =", square(5))


# ============================================================
# 2. Multiple Arguments
# ============================================================

print("\n2. Lambda with multiple arguments:")
add = lambda a, b: a + b
print("add(3, 7) =", add(3, 7))


# ============================================================
# 3. Lambda as key in sorted()
# ============================================================

print("\n3. Lambda used as key in sorted():")
pairs = [(1, 4), (3, 1), (5, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted by second element:", sorted_pairs)

students = [
    {"name": "Alice", "score": 82},
    {"name": "Bob", "score": 91},
    {"name": "Eve", "score": 74},
]
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print("Students sorted by score:", sorted_students)


# ============================================================
# 4. Lambda with map()
# ============================================================

print("\n4. Lambda with map():")
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)


# ============================================================
# 5. Lambda with filter()
# ============================================================

print("\n5. Lambda with filter():")
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)


# ============================================================
# 6. Lambda with reduce()
# ============================================================

print("\n6. Lambda with reduce():")
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print("Product:", product)


# ============================================================
# 7. Lambda inside list comprehensions
# ============================================================

print("\n7. Lambda inside list comprehension:")
funcs = [(lambda x, i=i: x + i) for i in range(5)]  # capture i correctly
print("funcs =", funcs)
print("funcs[1](2) =", funcs[1](2))


# ============================================================
# 8. Inline Lambda for callbacks (simulated example)
# ============================================================

print("\n8. Lambda for inline callbacks:")
callback = lambda: print("Callback executed!")
callback()


# ============================================================
# 9. Conditional expression inside lambda
# ============================================================

print("\n9. Conditional expression in lambda:")
compare = lambda x, y: "x>y" if x > y else "x<=y"
print("compare(10, 5) =", compare(10, 5))


# ============================================================
# 10. Lambda in dictionaries for dynamic behavior
# ============================================================

print("\n10. Lambda inside dictionaries:")
actions = {
    "square": lambda x: x * x,
    "cube": lambda x: x * x * x
}
print("cube(3) =", actions["cube"](3))


# ============================================================
# 11. Lambda for closures
# ============================================================

print("\n11. Lambda for closures:")
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
print("double(10) =", double(10))


# ============================================================
# 12. Complex usage with sorted()
# ============================================================

print("\n12. Complex lambda in sorting:")
words = ["apple", "banana", "kiwi", "strawberry"]
sorted_words = sorted(words, key=lambda w: (len(w), w))
print("Sorted words:", sorted_words)


# ============================================================
# 13. Functional pipeline using lambdas
# ============================================================

print("\n13. Lambda pipeline:")
pipe = lambda x: (lambda y: y * 2)(x) + (lambda y: y + 3)(x)
print("pipe(5) =", pipe(5))


# ============================================================
# 14. Lambda inside any() / all()
# ============================================================

print("\n14. Lambda inside any()/all():")
people = [{"age": 15}, {"age": 22}, {"age": 30}]
adult_exists = any(map(lambda p: p["age"] >= 18, people))
print("Is there an adult?", adult_exists)

