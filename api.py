# # import requests
# # import prettyjson

 

# # def get_json_from_api(url):

# #     response = requests.get(url)

   

# #     if response.status_code == 200:

# #         json_data = response.json()

# #         return json_data

# #     else:

# #         print("Error: ", response.status_code)

# #         return None

 

# # # Example usage:

# # api_url = "http://10.0.0.50:5000/api/data"

# # json_data = get_json_from_api(api_url)

 

# # if json_data is not None:

# #     # Process the JSON data

# #     print(prettyjson(json_data))

# import requests
# import json

# def get_json_from_api(url):
#     response = requests.get(url)
   
#     if response.status_code == 200:
#         json_data = response.json()
#         return json_data
#     else:
#         print("Error:", response.status_code)
#         return None

# # Example usage:
# api_url = "http://192.168.0.6:5000/api/data"
# json_data = get_json_from_api(api_url)

# if json_data is not None:
#     # Process the JSON data
#     print(json.dumps(json_data, indent=4))

# a = json_data['item']['batters']['batter'][2]['type']
# print(a)

from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Endpoint for executing the database query
@app.route('/query', methods=['GET'])
def execute_query():
    try:
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
        cur.execute("SELECT * FROM student")

        # Fetch all the results
        rows = cur.fetchall()

        # Close the cursor and connection
        cur.close()
        conn.close()

        # Convert the results to a JSON response
        results = [{'id': row[0], 'name': row[1]} for row in rows]

        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)})


# Endpoint for inserting data into the database
@app.route('/insert', methods=['POST'])
def insert_data():
    try:
        # Extract the data from the request payload
        data = request.get_json()

        # Extract the values
        column1 = data['id']
        column2 = data['name']

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

        # Insert data into the table
        cur.execute("INSERT INTO student (id, name) VALUES (%s, %s)", (column1, column2))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

        return jsonify({'message': 'Data inserted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()


# {
#     "id":"j",
#     "name":"kåre"
# }
