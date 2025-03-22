
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
'''
# MongoDB Connection
MONGO_URI = "mongodb+srv://Vishal:Vishal1103@cluster0.ae135.mongodb.net/mydatabase?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["ParticipantDB"] # database
collection = db["Participant"]  # collection in it'''

@app.route("/")
def home():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)
