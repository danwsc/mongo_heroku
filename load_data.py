from dotenv import load_dotenv
import json
import os
import pymongo

load_dotenv() # use dotenv to hide sensitive credential as environment variables
# DATABASE_URL=f'mongodb+srv://user:{os.envirosn.get("password")}'\
# 			  '@mongo-heroku-cluster-we.kyrhz.mongodb.net/myFirstDatabase?'\
# 			  'retryWrites=true&w=majority' # get connection url from environment
DATABASE_URL=f'mongodb+srv://danwsc:{os.environ.get("password")}@cluster0.x2ocq.mongodb.net/test?retryWrites=true&w=majority'

client=pymongo.MongoClient(DATABASE_URL) # establish connection with database
mongo_db=client.test # assign database to mongo_db
mongo_db.launches.drop() # clear the collection

with open('static/data/launches.json') as file: # opening the json file
    file_data = json.load(file)

if isinstance(file_data, list):
    mongo_db.launches.insert_many(file_data) # if data is a list
else:
    mongo_db.launches.insert_one(file_data) # if data is a document object