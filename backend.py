import psycopg2

def insert_user(name, email, phone, job, organisation, employees, economy_sector, deadline, devices, quantity):
    conn = psycopg2.connect(database="mydb", user="postgres", password="postgres", host="localhost")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, email, phone, job, organisation, employees, economy_sector, deadline, devices, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (name, email, phone, job, organisation, employees, economy_sector, deadline, devices, quantity),
    )
    conn.commit()
    cur.close()
    conn.close()

def insert_device(user_id, device, quantity):
    conn = psycopg2.connect(database="mydb", user="postgres", password="postgres", host="localhost")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO devices (user_id, device, quantity) VALUES (%s, %s, %s)",
        (user_id, device, quantity),
    )
    conn.commit()
    cur.close()
    conn.close()
