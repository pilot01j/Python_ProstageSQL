import psycopg2
# first you need to install psycopg2 using File/Settings/Python Interpreter/pip - and find psycopg2 -binary
# on web page https://customer.elephantsql.com/ create an account and table , and copy the URL

url = "postgres://wgdoscdd:E59xP0XqsCPLENH75yk5_PCmn4fiw6SC@tai.db.elephantsql.com/wgdoscdd"
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()
print(first_user)

connection.close()
