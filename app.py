from flask import Flask, request, render_template
import mysql.connector
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS
CORS(app, supports_credentials=True)

# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Root12345",
    database="zahara"
)

# Initialize bcrypt for password hashing
bcrypt = Bcrypt(app)

# Route for the sign-in page
@app.route('/')
def home():
    return render_template('signin.html', message=None)


# Route to handle sign-in form submission
@app.route('/signin', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']

    # Check if email already exists
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM info WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.close()
        return render_template('signin.html', error="Email already exists. Please log in.")

    # Hash the password for secure storage
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    try:
        # Insert data into the `info` table
        query = "INSERT INTO info (email, password) VALUES (%s, %s)"
        cursor.execute(query, (email, hashed_password))
        db.commit()
        message = "Account created successfully!"
    except mysql.connector.Error as e:
        db.rollback()
        message = f"MySQL Error: {e}"
    except Exception as e:
        message = f"Error: {e}"
    finally:
        cursor.close()

    return render_template('scheme.html', message=message)



if __name__ == '__main__':
    app.run(debug=True)
