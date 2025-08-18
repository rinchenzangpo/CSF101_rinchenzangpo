def greet_with_default(name="guest"):
    print(f"hello, {name}!")

greet_with_default()
greet_with_default("Zangpo")  

def calculate_rectangle_area(width, height):
    return width * height

area = calculate_rectangle_area(5, 3)
print(f"the are of the rectangle is: {area}")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Zangpo", age=19, city="Thimphu")

def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([5, 2, 8, 1, 9])
print(f"min: {result[0]}, max: {result[1]}")

def safe_divide(a, b):
    if b== 0:
        return "cannot divide by zero"
    return a / b

print(safe_divide(10, 2))
print(safe_divide(5, 0))
