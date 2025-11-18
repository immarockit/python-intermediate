"""
Comprehensive Examples of Exception Handling in Python
"""

# ============================================================
# 1. Basic try/except
# ============================================================

print("\n1. Basic try/except:")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")


# ============================================================
# 2. Catching multiple exception types
# ============================================================

print("\n2. Multiple exception types:")
try:
    value = int("hello")
except ValueError:
    print("Error: Could not convert string to int.")
except TypeError:
    print("Error: Wrong type.")


# ============================================================
# 3. Using else (executes only if no exception)
# ============================================================

print("\n3. try/except/else:")
try:
    n = int("42")
except ValueError:
    print("Conversion failed.")
else:
    print("Success! n =", n)


# ============================================================
# 4. Using finally (runs ALWAYS)
# ============================================================

print("\n4. finally always runs:")
try:
    f = open("nonexistent.txt")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Finally block executed.")


# ============================================================
# 5. Catching multiple exceptions in one line
# ============================================================

print("\n5. Multiple exceptions in one line:")
try:
    result = 10 / int("x")
except (ZeroDivisionError, ValueError) as e:
    print("Caught exception:", type(e).__name__)


# ============================================================
# 6. Raising exceptions explicitly
# ============================================================

print("\n6. Raising exceptions:")
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return True

try:
    check_age(-5)
except ValueError as e:
    print("Raised exception caught:", e)


# ============================================================
# 7. Custom exception classes
# ============================================================

print("\n7. Custom exception classes:")

class BankError(Exception):
    pass

class InsufficientFunds(BankError):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds("Not enough balance!")
    return balance - amount

try:
    withdraw(50, 100)
except InsufficientFunds as e:
    print("Bank error:", e)


# ============================================================
# 8. Nested try/except
# ============================================================

print("\n8. Nested try/except:")
try:
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Inner handler: division error.")
        raise  # re-throws the exception
except Exception:
    print("Outer handler caught the re-thrown exception.")


# ============================================================
# 9. Exception chaining: using 'raise ... from ...'
# ============================================================

print("\n9. Exception chaining:")
try:
    try:
        int("hello")
    except ValueError as e:
        raise TypeError("Converted ValueError into TypeError") from e
except Exception as e:
    print("Caught exception:", type(e).__name__)
    print("Original cause was:", type(e.__cause__).__name__)


# ============================================================
# 10. Catching SyntaxError using exec()
# ============================================================

print("\n10. Catching SyntaxError with exec():")
try:
    exec("a = 5 print('bad syntax')")
except SyntaxError:
    print("Caught SyntaxError from exec().")


# ============================================================
# 11. Using try/except in loops
# ============================================================

print("\n11. try/except in loops:")
values = ["10", "5", "x", "7"]

for v in values:
    try:
        num = int(v)
        print("Converted:", num)
    except ValueError:
        print("Skipping invalid:", v)


# ============================================================
# 12. try/except with file handling
# ============================================================

print("\n12. File handling exceptions:")
try:
    with open("not_here.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist.")
except PermissionError:
    print("You lack permission to open this file.")


# ============================================================
# 13. Clean-up example using finally
# ============================================================

print("\n13. Cleanup with finally:")
f = None
try:
    f = open("temp.txt", "w")
    f.write("Hello")
except Exception as e:
    print("Unexpected error:", e)
finally:
    if f:
        f.close()
        print("File closed safely.")


# ============================================================
# 14. Demonstrating the difference between errors & exceptions
# ============================================================

print("\n14. Errors vs Exceptions:")
try:
    print(undefined_variable)   # NameError
except NameError:
    print("A NameError occurred!")




"""
Comprehensive Examples of `raise` and `assert` in Python
"""


# ============================================================
# 1. Basic `raise`
# ============================================================

print("\n1. Basic raise:")
try:
    raise ValueError("Something went wrong!")
except ValueError as e:
    print("Caught:", e)


# ============================================================
# 2. Using raise for input validation
# ============================================================

print("\n2. Input validation with raise:")

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Age set to:", age)

try:
    set_age(-5)
except ValueError as e:
    print("Caught:", e)


# ============================================================
# 3. Raising different exception types
# ============================================================

print("\n3. Raising different exception types:")

try:
    raise TypeError("Expected a string, got something else.")
except TypeError as e:
    print("Caught:", e)


# ============================================================
# 4. Re-raising an exception
# ============================================================

print("\n4. Re-raising exceptions:")

try:
    try:
        10 / 0
    except ZeroDivisionError:
        print("Inner except: division error occurred.")
        raise   # re-raises
except Exception as e:
    print("Outer except caught:", type(e).__name__)


# ============================================================
# 5. Exception chaining using `raise ... from ...`
# ============================================================

print("\n5. Exception chaining:")

try:
    try:
        int("hello")
    except ValueError as e:
        raise RuntimeError("Failed to convert input") from e
except Exception as e:
    print("Caught:", type(e).__name__)
    print("Original cause:", type(e.__cause__).__name__)


# ============================================================
# 6. Basic assert usage
# ============================================================

print("\n6. Basic assert:")

x = 10
try:
    assert x > 0, "x must be positive"
    print("Assert passed, x =", x)
except AssertionError as e:
    print("Assert failed:", e)


# ============================================================
# 7. Assert used for internal logic checks (invariants)
# ============================================================

print("\n7. Using assert for internal logic (invariants):")

def normalize(values):
    total = sum(values)
    assert total != 0, "Sum of values cannot be zero"
    return [v / total for v in values]

try:
    print("Normalized list:", normalize([1, 2, 3]))
    print("Trying to normalize zero-sum list...")
    print(normalize([1, -1]))
except AssertionError as e:
    print("Caught:", e)


# ============================================================
# 8. Demonstrating that assert is NOT for user input validation
# ============================================================

print("\n8. Assert is not for user input validation:")

def deposit(amount):
    # WRONG way to validate (assert can be removed with python -O)
    assert amount > 0, "Amount must be positive"
    print("Deposited:", amount)

try:
    deposit(-10)
except AssertionError as e:
    print("Caught:", e)


# ============================================================
# 9. Correct validation using raise instead of assert
# ============================================================

print("\n9. Correct validation with raise:")

def safe_deposit(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    print("Deposited safely:", amount)

try:
    safe_deposit(-10)
except ValueError as e:
    print("Caught:", e)


# ============================================================
# 10. Assert is removed in optimized mode (informational)
# ============================================================

print("\n10. Assert removal in optimized mode (-O):")
print("Run `python -O raise_assert_examples.py` to see asserts disappear.")

