name = "Marin"
greeting = f"Hello, {name}"
print(greeting)
name = "Vadim"
print(greeting)

print(f"Hello, {name}")

name = "Ion"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

with_name_2 = greeting.format("Ana")
print(with_name_2)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Mihaela", "Luni")
print(formatted)
