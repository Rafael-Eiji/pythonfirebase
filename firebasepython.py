import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCaoRUxYeAUyS5jLdsc4KKK1FHSbTWM0h4",
  'authDomain': "my-first-project-e9925.firebaseapp.com",
  'databaseURL': 'https://my-first-project-e9925-default-rtdb.firebaseio.com/',
  'projectId': "my-first-project-e9925",
  'storageBucket': "my-first-project-e9925.appspot.com",
  'messagingSenderId': "1040162834788",
  'appId': "1:1040162834788:web:9d9d54bccaf6fab36e5271"
};

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

#------------------------------------------incluir dados
''' data= {'name': 'John', 'age': 20, 'adress': ['New York', 'LA']}

db.push(data) '''

''' data= {'name': 'project', 'deadline':'2pm'}
db.child('todolistB').child('wednesday').set(data)

data= {'name': 'volunteer', 'deadline':'9pm'}
db.child('todolistA').child('wednesday').push(data) '''


#--------------------------------------------Alterar dados

''' db.child('todolistA').child('Monday').child('paper').update({'deadline': '1pm'}) '''

''' data = {'todolistA/Monday/paper':{'details': 'v2'}, 'todolistA/tuesday/filmvideo': {'deadline' : '7pm'}}
db.update(data) '''

''' monday_tasks = db.child('todolistB').child('monday').get()

for task in monday_tasks.each():
    #print(task.val())
    #print(task.key())
    if task.val()['name'] == 'paper' :
        key = task.key()

db.child('todolistB').child('monday').child(key).update({'deadline': '1am'}) '''


#--------------------------------------------Deletar dados

#db.child('todolistA').child('wednesday').child('volunteer').child('deadline').remove()

''' monday_tasks = db.child('todolistB').child('monday').get()

for task in monday_tasks.each():
    #print(task.val())
    #print(task.key())
    if task.val()['name'] == 'paper' :
        key = task.key()

db.child('todolistB').child('monday').child(key).child('deadline').remove() '''

monday_tasks = db.child('todolistB').get()

print(monday_tasks.val()['monday'])
   


