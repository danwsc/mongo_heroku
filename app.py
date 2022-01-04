from dotenv import load_dotenv
import os
import pymongo
from flask import Flask, jsonify

load_dotenv() # use dotenv to hide sensitive credential as environment variables
# DATABASE_URL=f'mongodb+srv://user:{os.environ.get("password")}'\
# 			  '@mongo-heroku-cluster-we.kyrhz.mongodb.net/myFirstDatabase?'\
# 			  'retryWrites=true&w=majority' # get connection url from environment
DATABASE_URL=f'mongodb+srv://danwsc:{os.environ.get("password")})@cluster0.x2ocq.mongodb.net/test?retryWrites=true&w=majority'

client=pymongo.MongoClient(DATABASE_URL) # establish connection with database
mongo_db=client.db # assign database to mongo_db

app=Flask(__name__)

@app.route('/')
def index(): 
	return 'Use /all_launches_timeline'

@app.route('/sample_launch/')
def sample():
	results=mongo_db.launches.find_one({}, {'_id': 0})
	return jsonify(results)

if __name__=='__main__': 
	app.run()