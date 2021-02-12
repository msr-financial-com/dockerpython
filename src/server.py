from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import os

#Initialize Flask
app = Flask(__name__)

#Initialize mysql extension
mysql = MySQL(app)

#MySQL config
app.config['MYSQL_HOST'] = os.environ.get('host')
app.config['MYSQL_PORT'] = os.environ.get('mysql_port')
app.config['MYSQL_USER'] = os.environ.get('mysql_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('mysql_password')
app.config['MYSQL_DB'] = os.environ.get('mysql_db')

mysql.init_app(app)

#Default route to index.html
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

#Route to signup.html
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
   # read the posted values from the UI
   _name = request.form['inputName']
   _email = request.form['inputEmail']
   _password = request.form['inputPassword']

   # validate the received values
   if _name and _email and _password:
       return json.dumps({'html':'<span>All fields good !!</span>'})
   else:
      return json.dumps({'html':'<span>Enter the required fields</span>'})

   #Establish mysql connection
   conn = mysql.connect()
   #Create Cursor
   cursor = conn.cursor()

   #Hash password
   _hashed_password = generate_password_hash(_password)

   #Create User
   cursor.callproc('sp_createUser',(_name,_email,_hashed_password))

   #Make sure everything is good
   data = cursor.fetchall()

   if len(data) == 0:
       conn.commit()
       return json.dumps({'message':'User created successfully !'})
   else:
       return json.dumps({'error':str(data[0])})


#Run app on 0.0.0.0
if __name__ == "__main__":
   app.run(host='0.0.0.0')