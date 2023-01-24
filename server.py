from flask import Flask, render_template, redirect
from bot_1 import mailing
from model import users, script
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')
                        
@app.route("/mailing")
def mailing_page():
    mailing()
    return redirect ("/") 

@app.route("/bd")
def bd_users():
    engine = create_engine("sqlite:///database.db", echo=True) 
    Session = sessionmaker(bind = engine)
    session = Session()
    list_user = session.query(users).all()
    return render_template('bd.html',  list_user= list_user)

@app.route("/bdd")
def bd_script():
    engine = create_engine("sqlite:///database.db", echo=True) 
    Session = sessionmaker(bind = engine)
    session = Session()
    list_script = session.query(script).all()
    return render_template('bdd.html',  list_script= list_script)


if __name__=="__main__":
    app.run()



    # chat_id=chat_id, username=username, firstname=firstname, surname=surname
    # list_user=list_user
     # list_user = users.query.all() 