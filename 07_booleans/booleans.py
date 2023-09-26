print("Comparison num")
print(5 == 5)
print(1 + 2 == 3)
print(0.1 + 0.2 == 0.3)
print("------------------------------------------------------------------")
print(10 != 10)
print("------------------------------------------------------------------")
# Comparisons : == , != , <, >, <=, >=
print("Comparison list")
friends = ["Marin", "Vadim"]
abroad = ["Marin", "Vadim"]
print(friends == abroad)
print(friends is abroad)  # different address
print("------------------------------------------------------------------")
friends = ["Marin", "Vadim"]
abroad = friends
print(friends is abroad)  # the same address

