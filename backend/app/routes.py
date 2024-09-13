from flask import Blueprint, jsonify
from app.db import get_db_connection

hello_bp = Blueprint('hello', __name__)
main_bp = Blueprint('main', __name__)

# Define the route for '/'
@hello_bp.route('/api')
def hello_world():
    return 'Hello, World!'

@main_bp.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT message FROM test_table")
    # row = cursor.fetchone() # Fetch one row
    rows = cursor.fetchall()  # Fetch all rows
    cursor.close()
    conn.close()
    
    messages = [row[0] for row in rows]  # Extract messages from rows
    return jsonify({"messages": messages})

