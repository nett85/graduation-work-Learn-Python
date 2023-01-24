
import sqlalchemy as db

engine = db.create_engine('sqlite:///database.db')
connection = engine.connect()
metadata = db.MetaData()

сhatBot = db.Table('ChatBot', metadata, 
        db.Column('id', db.Integer, primary_key=True),
        db.Column('title', db.String, nullable=False),
        db.Column('token', db.String, nullable=False),
        db.Column('data_create', db.DateTime, nullable=False)
)

users = db.Table('Users', metadata,
        db.Column('id', db.Integer, primary_key=True),
        db.Column('chat_id', db.Integer, nullable=False), #todo nullable=False
        db.Column('username', db.String, nullable=False),
        db.Column('firstname', db.String, nullable=False),
        db.Column('surname', db.String, nullable=False),
        db.Column('chat_bot', db.Integer, db.ForeignKey('ChatBot.id'), index=True, nullable=True)
)

script = db.Table('Script', metadata,
        db.Column('id', db.Integer, primary_key=True),
        db.Column('chat_id', db.Integer, db.ForeignKey('ChatBot.id'), index=True, nullable=True), #todo nullable=False
        db.Column('response_text', db.String, nullable=False),
        db.Column('triger_text', db.String, nullable=False),
        db.Column('chat_bot', db.Integer, nullable=False)
)




if __name__ == '__main__':
    metadata.create_all(engine)











# class ChatBot (db.Model):
#         user_id = db.Column(db.Integer, primary_key=True)
#         title = db.Column(db.String, primary_key=True)
#         token = db.Column(db.String, nullable=False)
#         data_create = db.Column(db.DateTime, nullable=False)








# from sqlalchemy import Column, Integer, String, ForeignKey, Table

# from datetime import datetime

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tab.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# if __name__ == '__main__':
#     app.run(debug=True)


# db = SQLAlchemy(app)

# class Users (db.Model):
#         user_id = db.Column(db.Integer, primary_key=True)
#         chat_id = db.Column(db.Integer, nullable=False)
#         username = db.Column(db.String, nullable=False)
#         last_name = db.Column(db.String, nullable=False)
#         surname = db.Column(db.String, nullable=False)
#         first_contact = db.Column(db.DateTime, nullable=False)

#         def __repr__(self):
#                return f'<Users{self.id}>'        
      
        
# class ChatBot (db.Model):
#         user_id = db.Column(db.Integer, primary_key=True)
#         title = db.Column(db.String, primary_key=True)
#         token = db.Column(db.String, nullable=False)
#         data_create = db.Column(db.DateTime, nullable=False)
                 
#         user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        
#         def __repr__(self):
#                return f'<ChatBot{self.id}>' 