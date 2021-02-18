print("Hello World")

name = "Takashi"
print("Hello", name, "!")
print("Hello "+name+"!")

num = 23
print("Hello", num, "!")
print("Hello "+str(num)+"!")

fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}.")

# other string methods
print(fave_food1.upper())
print(name.lower())
print(fave_food2.count("z"))
print(fave_food1.split("s"))
print(name.find("s"))

new_object = "!%$#"
print(new_object.isalnum())
food = (fave_food1, fave_food2)
print(name.join(food))
print(name.endswith("i"))
