from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

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
    return render_template('signin.html')

# Route to handle sign-in form submission
@app.route('/signin', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']
    
    # Hash the password for secure storage
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    try:
        # Insert data into the `info` table
        cursor = db.cursor()
        query = "INSERT INTO info (email, password) VALUES (%s, %s)"
        cursor.execute(query, (email, hashed_password))
        db.commit()
        flash('Account created successfully!', 'success')
    except mysql.connector.Error as e:
        flash(f'Database Error: {e}', 'danger')
    except Exception as e:
        flash(f'Error: {e}', 'danger')
    finally:
        cursor.close()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
