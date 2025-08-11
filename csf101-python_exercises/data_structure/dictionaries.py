name = "Rinchen Zangpo"
age = 19
height = 178
is_student = True

person_info = {
    "name": name,
    "age": age,
    "height": is_student
}
print(person_info)
person_info["favorite_color"] = "green"
print(person_info)
try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")
    