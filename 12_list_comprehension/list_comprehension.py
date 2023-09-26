numbers = [1, 3, 5]
double = [num * 2 for num in numbers]
print(double)
print("------------------------------------------------------------------")
friends = ["Rolf", "Sam", "Samanta", "Sabina", "Jan"]
s_friends = [friend for friend in friends if friend.startswith("S")]
print(s_friends)
print("------------------------------------------------------------------")
new_friends = ["Sony", "Sire", "Susan"]
s_new_friends = [friend for friend in new_friends if friend.startswith("S")]
print(new_friends)
print(s_new_friends)
print("s_new_friends in new_friends: ", s_new_friends in new_friends)
print('id new_friends: ', id(new_friends), "id s_new_friends", id(s_new_friends))
