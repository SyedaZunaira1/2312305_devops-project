import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database Connection Function (Credentials from Environment Variables)
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        database=os.environ.get('DB_NAME', 'student_db'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'password')
    )
    return conn

# Database Table Setup (if table doesn't exist)
def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                roll_no VARCHAR(50) NOT NULL
            );
        ''')
        conn.commit()
        cur.close()
        conn.close()
        print("Database table ready!")
    except Exception as e:
        print("Database connection error. Retrying later...", e)

# 1. Health Check Endpoint (Aapki Requirement)
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "Healthy",
        "registration_number": "2312305" 
    }), 200

# 2. Add Student (POST Request)
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    roll_no = data.get('roll_no')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO students (name, roll_no) VALUES (%s, %s) RETURNING *;',
        (name, roll_no)
    )
    new_student = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({
        "id": new_student[0], 
        "name": new_student[1], 
        "roll_no": new_student[2]
    }), 201

# 3. Get Students (GET Request)
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students;')
    students = cur.fetchall()
    cur.close()
    conn.close()
    
    # Format the data
    result = [{"id": s[0], "name": s[1], "roll_no": s[2]} for s in students]
    return jsonify(result), 200

if __name__ == '__main__':
    # App start hone se pehle DB check karegi
    init_db()
    # App port 8000 par chalegi
    app.run(host='0.0.0.0', port=8000)