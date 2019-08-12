from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'semantix'
app.config['MYSQL_DB'] = 'alunosDB'

mysql = MySQL(app)



@app.route('/alunos', methods=['GET'])
def get_all():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM alunos')
    return jsonify(cursor.fetchall())


@app.route('/alunos/<int:student_id>', methods=['GET'])
def by_id(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM alunos WHERE id={}'.format(student_id))
    return jsonify(cursor.fetchall())


@app.route('/alunos/<string:student_name>', methods=['GET'])
def by_name(student_name):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM alunos WHERE nome LIKE "%{}%"'.format(student_name))
    return jsonify(cursor.fetchall())


if __name__ == '__main__':
    app.run(port=80, debug=True)
