import flask
from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Divyanshu692'
app.config['MYSQL_DB'] = 'registration_db'

mysql = MySQL(app)

@app.route('/')
def registration_form():
    return render_template('registration_form.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        id = request.form['roll']
        Student_name = request.form['name']
        Father_name = request.form['father_name']
        Mother_name = request.form['mother_name']
        Phone_number = request.form['phone_no']
        email = request.form['email']
        Date_of_birth = request.form['DOB']
        Address = request.form['address']
        Blood_Group = request.form['blood_group']
        Department = request.form['department']
        Course = request.form['course']
        Password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("use registration_db")
        cur.execute("INSERT INTO users (id, Student_name, Father_name, Mother_name, Phone_number,email, Date_of_birth, Blood_Group, Address, Department, Course, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (id, Student_name,Father_name,Mother_name,Phone_number,email, Date_of_birth, Blood_Group, Address, Department, Course, Password))
        mysql.connection.commit()
        cur.close()

        return render_template('registered.html')

if __name__ == '__main__':
    app.run(debug=True)