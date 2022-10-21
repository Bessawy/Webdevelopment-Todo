from app import app, db
from app.models import User, Todo, getStatus, Status
from functools import wraps
from flask import jsonify, request, make_response
import jwt
import datetime
from app.utils import *
from werkzeug.security import generate_password_hash, check_password_hash

def delete_table(table):
    with app.app_context():
        db.session.query(table).delete() 
        db.session.commit()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'access_token' in request.headers:
            token = request.headers['access_token']

        if not token:
            return jsonify({'message' : 'Token is missing!'})
        

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(email=data['email']).first()
        except:
            return jsonify({'message' : 'Token cannot be decoded!'})
        
        return f(current_user, *args, **kwargs)
    return decorated


@app.route('/api/v1/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # Check if the email entered is valid
    if not check_email(data['email']):
        return jsonify({'message' :'Invalid email!'})
    
    # Check if it does exist in the database
    user = User.query.filter_by(email=data['email']).first()
    if user:
        return jsonify({'message' :'Email is already used!'})

    current_time = str(datetime.datetime.now().timestamp())
    hashed_password = generate_password_hash(data['password'], method = 'sha256')
    new_user = User(email=data['email'], password=hashed_password,
                     acc_created = current_time, last_updated = current_time)
    
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()

    return jsonify({'message' :'New User Created!'})



@app.route('/api/v1/signin', methods=['POST'])
def signin():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="login required!"'})

    user = User.query.filter_by(email=auth.username).first()

    if not user:
        return make_response('User not found!', 401, {'WWW-Authenticate': 'Basic realm="login required!"'})
    
    if check_password_hash(user.password, auth.password):
        exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        token = jwt.encode({'email': user.email, 'exp': exp_time}, app.config['SECRET_KEY'])
        return jsonify({'token' : token})
    
    return make_response('Wrong password!', 401, {'WWW-Authenticate': 'Basic realm="login required!"'})


@app.route('/api/v1/changePassword', methods=['PUT'])
@token_required
def changePassword(current_user):
    data = request.get_json()

    current_time = str(datetime.datetime.now().timestamp())
    hashed_password = generate_password_hash(data['new_password'], method = 'sha256')
    
    with app.app_context():
        user = User.query.filter_by(email=current_user.email).first()
        user.password = hashed_password
        user.last_updated = current_time
        db.session.commit()

    return jsonify({"message" : "Password was changed!"})


@app.route('/api/v1/todos', methods=['GET'])
@token_required
def get_todos_all(current_user):
    status = request.args.get('status')
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    data = []
    toggle = False

    if getStatus(status) != None:
        toggle = True

    for todo in todos:

        if toggle and getStatus(status) != todo.status:
            continue

        todo_data = {}
        todo_data['id'] = todo.id
        todo_data['description'] = todo.description
        todo_data['created'] = todo.created
        todo_data['last_updated'] = todo.last_updated
        todo_data['status'] = todo.status.value
        data.append(todo_data)

    return jsonify({'todos' : data})


@app.route('/api/v1/todos', methods=['POST'])
@token_required
def create_todos(current_user):
    data = request.get_json()
    current_time = str(datetime.datetime.now().timestamp())

    with app.app_context():
        todo = Todo(name = data['name'], 
            description = data['description'],
            user_id = current_user.id,
            created = current_time,
            last_updated = current_time,
            status = getStatus(data['status']))

        db.session.add(todo)
        db.session.commit()

    return jsonify({'message' : 'Todo item is added!'})


@app.route('/api/v1/todos/<id>', methods=['PUT'])  
@token_required  
def update_todos(current_user, id):

    with app.app_context():
        todo = Todo.query.filter_by(id=id, user_id = current_user.id).first()
        if not todo:
            return jsonify({'message' : 'No todo found!'})

        status = todo.status
        if status == Status.NotStarted:
            todo.status = Status.OnGoing
        else:
            todo.status = Status.Completed

        current_time = str(datetime.datetime.now().timestamp())
        todo.last_updated = current_time
        db.session.commit()

    return jsonify({'message' : 'Task updated!'})


@app.route('/api/v1/todos/<id>', methods =['DELETE'])
@token_required
def delete_todos(current_user, id):
    with app.app_context():

        todo = Todo.query.filter_by(id=id, user_id = current_user.id).first()
        if not todo:
            return jsonify({'message' : 'No todo found!'})

        db.session.delete(todo)
        db.session.commit()
    return jsonify({'message': 'Todo deleted'})