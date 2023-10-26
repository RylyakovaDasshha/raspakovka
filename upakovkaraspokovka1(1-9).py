#1
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

print('-' * 50)

#2
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

print('-' * 50)

#3
name, age, company = ("Илья", 18, "НГТУ")
print(name)
print(age)
print(company)

print('-' * 50)

#4
people = ["Андрей", "Екатерина", "Сергей"]
first, second, third = people
print(first)
print(second)
print(third)

print('-' * 50)

#5
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
r, b, g = dictionary
print(r)
print(b)
print(g)
print(dictionary[g])

print('-' * 50)

#6
people = [
    ("Андрей", 17, "НГТУ"),
    ("Екатерина", 17, "НГУ"),
    ("Сергей", 19, "НГУЭУ")
]

for name, age, company in people:
    print(f"Name: {name}, Age: {age}, Company: {company}")

print('-' * 50)

#7
people = ["Андрей", "Екатерина", "Сергей"]
for index, name in enumerate(people):
    print(f"{index}.{name}")

print('-' * 50)

#8
person =("Илья", 18, "НГТУ")
name, _, company = person
print(name)
print(company)

print('-' * 50)

#9
name, _, company = person
print(_)

print('-' * 50)

