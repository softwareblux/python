import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="pylogin",
    password="Sneakyturtle2108"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute a simple query
cur.execute("SELECT * FROM student where id = '2'")

# Fetch all the results
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
