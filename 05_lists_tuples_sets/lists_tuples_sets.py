l_list = ["Marin", "Vadim", "Ion"]

# you can not modify it
# doesn't have append functions
# you can not have duplicate
t_tuple = ("Marin", "Vadim", "Ion")

# you can not have duplicate
s_set = {"Marin", "Vadim", "Ion"}
print("------------------------------------------------------------------")
# select a element from a list
print(l_list)
print(l_list[0])  # select an element from a list using indexing
# modify an element from a list
l_list[0] = "Vasile"
print(l_list[0])
# add an element to a list
l_list.append("Nicu")
print(l_list)
# remove/delete an element from a list
l_list.remove("Nicu")
print(l_list)
print("------------------------------------------------------------------")
print(s_set)
# add an element to a set
s_set.add("Dorin")
print(s_set)
