from flask import Flask
#from flask_mongoengine import MongoEngine
import pymongo


app = Flask(__name__)



client = pymongo.MongoClient("mongodb+srv://gtshepard:Garrison092894@ehredf.7wanq.mongodb.net/ehredfd4g?retryWrites=true&w=majority")
db = client.ehredfd4g


# grabbed user collection
print(db.list_collection_names())
print(db.user.find_one())




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