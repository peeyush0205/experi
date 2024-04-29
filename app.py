from flask import Flask,render_template,request
import pymongo
import os

app = Flask(__name__)

db_URL=os.getenv('DATABASE_URL')
client = pymongo.MongoClient(db_URL)
userdb = client['userdb']
users = userdb.customers

@app.route('/', methods = ["GET","POST"])
def index():
    
    if request.method=="POST":
     username = request.form.get("name")
     email = request.form.get("email")
     password1 = request.form.get("pass")


     user_input = {'name': username, 'email': email, 'password': password1}
            #insert it in the record collection
     users.insert_one(user_input)
     return render_template("index.html")
    else:
       return render_template("index.html")