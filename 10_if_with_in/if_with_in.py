movies_watched = ["The Matrix", "Green Book", "Her"]
user_movie = input("Enter something you're watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} movie too!")
else:
    print(f"I haven't watched that yet.")
print("------------------------------------------------------------------")
number = 7
user_input = input("Enter 'y' if would like to play: ")
if user_input in ("y", "Y", "yes"):
    user_numer = int(input("Guess our number: "))
    if user_numer == number:
        print("You guessed correctly!")
    elif number - user_numer in (1, -1):
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")
