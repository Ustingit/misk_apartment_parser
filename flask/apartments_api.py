from flask import Flask, jsonify, abort
import dblite

app = Flask(__name__)
db = dblite.ApartmentsDb()

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/apartments/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in db.get_apartments() if task[0] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'apartment': task[0]})


@app.route('/apartments', methods=['GET'])
def get_apartments():
    return jsonify({'apartments': db.get_apartments()})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/')
def index():
    return "Hello, World! It's open API of minsk rent-apartments by Yuryi Ustinovich."


if __name__ == '__main__':
    app.run(debug=True)
