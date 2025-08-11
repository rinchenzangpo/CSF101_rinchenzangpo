name="Rinchen Zangpo"
print(name)
greeting_f="hello, " + name + "!"
print(greeting_f)
name_length=len(name)
print(name_length)
non_num_str = "hello"
try:
    non_num_str = int(non_num_str)
    print(non_num_str)
except ValueError as e:
    print(f"Error: {e}")
    