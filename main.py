from flask import Flask
from flask_mongoengine import MongoEngine
#import pymongo


app = Flask(__name__)


DB_URI = "mongodb+srv://gtshepard:Garrison092894@ehredf.7wanq.mongodb.net/ehredfd4g?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI
#client = pymongo.MongoClient("mongodb+srv://gtshepard:Garrison092894@ehredf.7wanq.mongodb.net/ehredfd4g?retryWrites=true&w=majority")
#db = client.ehredfd4g
db = MongoEngine(app)

class user(db.Document):
    name = db.StringField(reuired=True, max_length=50)
    email = db.StringField(reuired=True, max_length=50)

users = user.objects()
for x in users:
    print(x.name)
# grabbed user collection
#print(db.list_collection_names())
#print(db.user.find_one())

#new_user = {"name": "steve", "email":"steve@gmail.com"}
#db.user.insert(new_user)
#my_query = { "name": "steve" }
#users = db.user.find(my_query)
#for x in users:
#    print(x)
#app.config["MONGODB_HOST"] = DB_URI
# mongodb+srv://garrison:<password>@test.ej3zh.mongodb.net/<dbname>?retryWrites=true&w=majority

@app.route("/")
def homepage():
    return f'home page!'

@app.route("/docs")
def docs():
    names = "NOTHING"
  
    
    

    return f'{names}'

@app.route("/about")
def about():
    return 'about page!'

if __name__ == "__main__":
    app.run(debug=True)