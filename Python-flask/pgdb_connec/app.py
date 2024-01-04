from flask import Flask, render_template,request,redirect,url_for,jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="12345"
    )
    return conn  # Return the database connection object

@app.route('/')
def home():
    return 'it works'

@app.route('/tab')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM emp_data;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=data)
 
@app.route('/createtable')
def createtable():
   conn = get_db_connection()
   cur = conn.cursor()
   cur.execute('CREATE TABLE student (id serial PRIMARY KEY,'
               'name varchar (150) NOT NULL,'
               'marks integer,'
               'result varchar)'
   )

   cur.execute('INSERT INTO student(name, marks, result)'
               'VALUES (%s, %s, %s)',
               ('abiii', 450, 'Pass')
               )
   cur.execute('INSERT INTO student(name, marks, result)'
               'VALUES (%s, %s, %s)',
               ('uvaa', 430, 'Pass')
               )
   conn.commit()
   cur.close()
   conn.close()
   return 'Successfully created new table on postgresdb'

@app.route('/newtable')
def shownewtable():
   conn = get_db_connection()
   cur = conn.cursor()
   cur.execute('SELECT * FROM student;')
   data1 = cur.fetchall()
   cur.close()
   conn.close()
   return (data1)

@app.route('/update/<name>', methods=['PUT'])
def update(name):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        data = request.json
        marks = data.get('marks')
        result = data.get('result')
        cur.execute(
            'UPDATE student SET marks=%s, result=%s WHERE name=%s',
            (marks, result, name)
        )
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'message': f'Data for name {name} updated successfully.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)