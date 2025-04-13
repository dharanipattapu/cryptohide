from flask import Flask, render_template, json, request, jsonify
import mysql.connector
import logging

app = Flask(__name__)

# MySQL configurations
mysql_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Nsbv(czKXoh-MKS6',
    'database': 'crypto'
}

# Connect to MySQL database
db_connection = mysql.connector.connect(**mysql_config)


# Define User model
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

@app.route('/')
def main():
    # Render index.html template and pass showEn variable to it
    return render_template('index.html')

@app.route('/signup')
def showSignUp():
    return render_template('signup.html')

@app.route('/encryption')
def showencrpt():
    return render_template('encryption.html')

@app.route('/decryption')
def showdecry():
    return render_template('decryption.html')


@app.route('/about')
def showabout():
    return render_template('aboutus.html')

@app.route('/documentation')
def showdoc():
    return render_template('documentation.html')

@app.route('/consideration')
def showcon():
    return render_template('consideration.html')


# API endpoint for user signup
@app.route('/api/signup', methods=['POST'])
def signUp():
    try:
        # Get data from request
        name = request.form['inputName']
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        logging.info("Inside APi")
        # Create a new User object
        new_user = User(name, email, password)

        # Insert user data into the database
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                       (new_user.name, new_user.email, new_user.password))
        db_connection.commit()
        cursor.close()
        return jsonify({"message": "User registered successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
