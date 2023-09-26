friends = {"Marin", "Vadim", "Ion"}
abroad = {"Vadim", "Ion"}
local = {"Nicu"}
# local_friends = {"Marin"}
print("Friends: ", friends)
print("Abroad: ", abroad)
print("Local: ", local)
local_friends = friends.difference(abroad)
print("Difference from all friends and abroad friend", local_friends)
# set() - empty set
print("------------------------------------------------------------------")
total_friends = local.union(abroad)
print("Union local and abroad friends:", total_friends)
print("------------------------------------------------------------------")
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
print("------------------------------------------------------------------")
both = art.intersection(science)
print("Art:", art)
print("Science: ", science)
print("Intersection from art and science: ", both)
