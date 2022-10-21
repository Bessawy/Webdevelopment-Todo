# **Todo Web development - Integrify**

## Software used:

* Postman
* pgAdmin4

### python version: 3.10
---

## Setup dataset table for the first time

* Create a new database using pgAdmin4. The name is set to: Todo, and password: 1234. You can also change the URL in the **config.py**.

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/Todo'
```

* Create the database by running the below script in a terminal or through **db_init.py**.
```python
from app import app, db
from app.models import User, Todo

with app.app_context():
    db.create_all()
```
----
## Start the application and the server from **run.py**
----
## Features

-- Sign up as an user of the system : 

*  [POST]-- URL : http://127.0.0.1:5000/api/v1/signup .
*  Send a JSON through the body with a valid email and any passward.

```javascript
{ "email": "random@any.com" , "password": "1234"}
```
* Nothing will be added if the email is already in use.

-- Sign in as a user :

* [POST]-- URL : http://127.0.0.1:5000/api/v1/signin .
* Send email and passward through Basic Authorization
* A token will be returned if the email and password are valid. The token will expire after 30 minutes.

-- To pass the <font color='yellow'>token </font> add a header with the key : 
<font color='red'>access_token</font> and add the <font color='yellow'>token </font> as a value.

-- The <font color='yellow'>token </font> is used to access the remaining APIs.

-- Change the user password : 
* [PUT]-- URL : http://127.0.0.1:5000/api/v1/changePassword .
* Send a JSON through the body with the new passward.
```javascript
{ "new_password": "12345"}
```
--  Create a new todo :
* [POST]-- URL : http://127.0.0.1:5000/api/v1/todos

* Send a JSON through the body with the 
<font color='red'> **name** </font> and <font color='red'> **description** </font> of the task, and the <font color='red'> **status** </font> whcih can either be NotStarted (<font color='red'> **NS** </font>), OnGoing (<font color='red'> **OG** </font>), or Completed (<font color='red'> **CP** </font>).


```javascript
{"name": "Cooking", "description": "cook chicken with rice", "status": "NS"}
```

-- Update a todo list :

* [PUT]-- URL :  http://127.0.0.1:5000/api/v1/todos/id

* Update the todo with given id from  (<font color='red'> **NS** </font>) to (<font color='red'> **OG** </font>), and from (<font color='red'> **OG** </font>) to (<font color='red'> **CP** </font>). If the todo status is (<font color='red'> **CP** </font>) nothing will change.

-- Delete a todo list :
* [Delete]-- URL : http://127.0.0.1:5000/api/v1/todos/id

-- Get a list of todo :

* [GET]-- URL : http://127.0.0.1:5000/api/v1/todos
* [GET]-- URL : http://127.0.0.1:5000/api/v1/todos?status=NS
* The argument passed can be <font color='red'> **NS** </font>, <font color='red'> **OG** </font>, or <font color='red'> **CP** </font>.
* Return the all todos, or todos with the specified status. 

---
## References & Resources :
* https://www.youtube.com/watch?v=WxGBoY5iNXY&list=WL&index=4&ab_channel=PrettyPrinted
* https://www.youtube.com/watch?v=w25ea_I89iM&t=1392s&ab_channel=TraversyMedia
* https://jtuto.com/python/flask-sqlalchemy-got-unexpected-argument/
