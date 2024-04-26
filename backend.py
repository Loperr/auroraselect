import psycopg2
from flask import Flask, request, render_template

app = Flask(__auroraselect__)

# Database connection parameters
db_name = "mydb"
db_user = "postgres"
db_password = "postgres"
db_host = "localhost"
db_port = "5432"

# Connect to the database
conn = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
cur = conn.cursor()

# Function to insert form data into the database
def insert_form_data(name, email, phone, job, organisation, employees, economy_sector, deadline, devices, quantity):
    # Insert user data
    cur.execute(
        "INSERT INTO users (name, email, phone, job, organisation, employees, economy_sector, deadline) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (name, email, phone, job, organisation, employees, economy_sector, deadline)
    )

    # Insert device data
    for device in devices:
        cur.execute(
            "INSERT INTO devices (user_id, device, quantity) VALUES (currval('users_id_seq'), %s, %s)",
            (device, quantity)
        )

    # Commit the changes
    conn.commit()

# Use the function to insert form data
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        job = request.form['job']
        organisation = request.form['organisation']
        employees = request.form['employees']
        economy_sector = request.form['economysector']
        deadline = request.form['deadline']
        devices = request.form.getlist('device[]')
        quantity = request.form['quantity']

        insert_form_data(name, email, phone, job, organisation, employees, economy_sector, deadline, devices, quantity)

        return 'Form submitted successfully!'

    return render_template('index.html')
