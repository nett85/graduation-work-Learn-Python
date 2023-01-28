
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





