'''
Created on 31 Mar 2017

@author: user
'''
from flask import Flask

from sqlalchemy import create_engine
import pymysql  
app =Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()


    
def connect_to_database():
    engine = create_engine("mysql+pymysql://DavidSurridge:MyGerryAdams@dublinbikesmysql.cqcpf75mkbbq.us-west-2.rds.amazonaws.com:3306/myDublinBikes", echo = True)
    return engine

