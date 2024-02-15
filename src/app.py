from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/mydomain', methods=['GET'])
def my_function():
    # return 'Hello World!'
    return '<h1>Hello World</h1>'

@app.route('/todos', methods=['GET'])
def new_todo():
    return todos


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print('Incoming request with the following body', request_body)
    return todos

@app.route('/myroute', methods=['GET'])
def hello_world():


    
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print('This is the position to be deleted:', position)
    todos.pop(position)
    return jsonify(todos)

# we need to declare variables AFTER the function declaration
some_data = { "name": "Bobby", "lastname": "Rixer" }
todos = [{"label": "My first task", "done": False},
        {"label": "My second task", "done": False}]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
