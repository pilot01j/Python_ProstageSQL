import datetime
import database

menu = """Please select one of the following options:
1. Add new movie.
2. View upcoming movies.
3. View all movies.
4. Add watched movie
5. View watched movies.
6. Add user to the app.
7. Search for the movie.
8. Exit.

Your selections: """
welcome = " Welcome to the watchlist app!"

print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")  # convert str to datetime
    timestamp = parsed_date.timestamp()  # convert datetime to timestamp
    database.add_movie(title, timestamp)


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


def print_movie_list(heading, movie_table):
    print(f"-- {heading} movies --")
    for _id, title, relase_date in movie_table:
        movie_date = datetime.datetime.fromtimestamp(relase_date)
        human_date = movie_date.strftime("%d %m %Y")
        print(f"{_id}: {title} (on {human_date})")
    print("----------------------------")


def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username, movie_id)


def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list("Watched", movies)
    else:
        print("That users has not watched movies yet!")


def prompt_search_movies():
    search_term = input("ENTER the partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Movies found", movies)
    else:
        print("Found NO movies for that search term!")


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")
