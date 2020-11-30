from flask import Flask, request, render_template,flash
import re

from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'python_login'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['SECRET_KEY']='random string'
mysql.init_app(app)

@app.route('/')
def form():
    return render_template('Login_Register.html')

@app.route('/login',methods =['POST'])
def Authenticate():
    print('jelo')
    username = request.form['Login_Username']
    password = request.form['Login_Password']
    cursor = mysql.connect().cursor()
    cursor.execute('SELECT * from accounts where username = %s AND password = %s', (username, password))
    data = cursor.fetchone()
    if data is None:
        flash('Invalid credentials')
        return render_template('Login_Register.html')
    else:
        return "LOGGED IN"

@app.route('/signup', methods=['GET','POST'])
def Registration():
    msg = ''
    conn = mysql.connect()
    cursor = conn.cursor()
    print('hello')
    # if request.method == 'POST' and 'name' in request.form and 'username' in request.form and 'password' in request.form and 'email' in request.form:
    if request.method == 'POST':
        name = request.form['SignUp_Name']
        username = request.form['SignUp_Username']
        email = request.form['SignUp_Email']
        password = request.form['SignUp_Password']
        cursor.execute(f"SELECT * from accounts where name = '{name}'")
        # cursor.execute('SELECT * from acccounts where name = %s')
        # cursor.execute('SELECT * from accounts WHERE (name,username,password,email) values(%s,%s,%s,%s)',[name,username,password,email])
        account = cursor.fetchone()
        print(type(account))
        print(account)
        if account:
            msg = "ACCOUNT ALREADY EXISTS!"
        
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = "INVALID EMAIL ADDRESS!"
        elif not re.match(r'[0-9]+', username):
            msg = "PLEASE FILL THE CORRECT FORM OF SYSTEM ID"
        elif not name or not username or not password or not email:
            msg = "PLEASE FILL THE FORM"
        else:
            cursor.execute('insert into accounts (name,username,password,email) values(%s,%s,%s,%s)',[name,username,password,email])
            conn.commit()
            msg = "REGISTERED SUCCESSFULLY"
    
    return render_template('Login_Register.html',msg=msg)
    # else:
    #     name = request.form['SignUp_Name']
    #     username = request.form['SignUp_Username']
    #     email = request.form['SignUp_Email']
    #     password = request.form['SignUp_Password']
    #     cursor.execute('insert into accounts (name,username,password,email) values(%s,%s,%s,%s)',[name,username,password,email])
    #     conn.commit()
    #     return "REGISTERED SUCCESSFULLY"
        

if __name__ == '__main__':
    app.debug = True
    app.run()





    
