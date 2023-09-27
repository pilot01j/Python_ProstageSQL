
- Implement the following options using Python:
1. Add new movie
2. View upcoming movies.
3. View all movies.
4. Add watched movie
5. View watched movies.
6. Add user to the app.
7. Exit

- Connect to ProstageSQL db , import psycopg2

- Create dotenv file to store the URL of ProstageSQL db
    .env: store de url - don't share it
    .env.example: store only the name "DATABASE_URL="

- Autoincrementing columns: instead to use id INTEGER , use id SEQUENCE and SERIAL
