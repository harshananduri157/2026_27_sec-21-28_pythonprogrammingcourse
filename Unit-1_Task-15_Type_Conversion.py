# print a program for type conversions
print("Type Conversions in Python")

# Implicit Type Conversion
x = 5  # integer
y = 2.0  # float
z = x + y  # result is a float

print(f"Implicit conversion: {x} + {y} = {z}")

# Explicit Type Conversion
a = "10"
b = "20"
c = int(a) + int(b)  # convert strings to integers

print(f"Explicit conversion: {a} + {b} = {c}")

d = 15
e = float(d)  # convert integer to float

print(f"Explicit conversion: {d} -> {e}")

f = 3.14
g = int(f)  # convert float to integer (truncates decimal part)

print(f"Explicit conversion: {f} -> {g}")

h = 0
i = bool(h)  # convert to boolean

print(f"Explicit conversion: {h} -> {i}")
