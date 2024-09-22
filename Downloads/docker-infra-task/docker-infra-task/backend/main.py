from flask import Flask, jsonify
import MySQLdb  # MySQL client for Python
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Function to establish a connection to the MySQL DB
def get_db_connection():
    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')

    if not all([host, user, password, db_name]):
        raise ValueError("One or more database connection environment variables are not set correctly.")

    conn = MySQLdb.connect(
        host=host,
        user=user,
        passwd=password,
        db=db_name,
        charset='utf8mb4',
        use_unicode=True
    )
    return conn

@app.route('/')
def is_alive():
    return jsonify('live')

# POST Route: Store message in the database
@app.route('/api/msg/<string:msg>', methods=['POST'])
def msg_post_api(msg):
    print(f"msg_post_api with message: {msg}")
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Insert message into the database and return the message ID
        cur.execute("INSERT INTO messages (message) VALUES (%s);", (msg,))
        conn.commit()
        
        # Fetch the last inserted message ID
        cur.execute("SELECT LAST_INSERT_ID();")
        msg_id = cur.fetchone()[0]
        
        # Close the connection
        cur.close()
        conn.close()
        
        # Return the message ID as a response
        return jsonify({'msg_id': msg_id})

    except MySQLdb.Error as e:
        return jsonify({'error': str(e)}), 500

# GET Route: Retrieve message from the database by message ID
@app.route('/api/msg/<int:msg_id>', methods=['GET'])
def msg_get_api(msg_id):
    print(f"msg_get_api > msg_id = {msg_id}")

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Retrieve the message from the database by msg_id
        cur.execute("SELECT message FROM messages WHERE id = %s;", (msg_id,))
        result = cur.fetchone()

        # Close the connection
        cur.close()
        conn.close()

        if result:
            # Return the message if found
            return jsonify({'msg': result[0]})
        else:
            # If message not found, return 404 error
            return jsonify({'error': 'Message not found'}), 404

    except MySQLdb.Error as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

