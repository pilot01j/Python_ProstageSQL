from database import create_table, add_entry, get_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome to the programming diary!"
create_table()

def prompt_new_entry():
    content = input("What have you learned today?")
    date = input("Enter the date:")

    add_entry(content, date)


def view_entrires(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n")
        # print(f"{entry[1]}\n{entry[0]}\n\n")
        # folosim indexarea 0 si 1 in caz daca nu implementam connection.row_factory = sqlite3.Row

print(welcome)
while (user_input := input(menu)) != "3":
    print("------------------------------------------------------------------")
    if user_input == "1":
        prompt_new_entry()
        print("------------------------------------------------------------------")
    elif user_input == "2":
        view_entrires(get_entries())
    else:
        print("Invalid option, please try again!")
