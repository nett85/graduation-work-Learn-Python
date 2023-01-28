import logging
import telebot
import config
from sqlalchemy.orm import sessionmaker
from telebot import types
from model import users,script
from sqlalchemy import create_engine


bot = telebot.TeleBot(config.API_KEY, parse_mode=None)
logging.basicConfig(filename='bot.log', level=logging.INFO)


@bot.message_handler(commands=['pogoda'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Переход на сайт', url='https://yandex.ru/pogoda/?via=hl'))       
    bot.send_message(message.chat.id, 'Переходите скорее на сайт!', reply_markup=markup)
 
 
@bot.message_handler(commands=['id'])
def id(message):    
   bot.send_message(message.chat.id, f'Вся информация о Вас:{message.chat.id, str(message)}') 
   

@bot.message_handler()
def user_text(message):
    engine = create_engine("sqlite:///database.db", echo=True) 
    Session = sessionmaker(bind = engine)
    session = Session()
    # если пользователя нет в базе, то мы его создаем 
    db_connection = engine.connect()
    result = session.query(users).filter_by(username = message.from_user.username).one_or_none() #запрос к базе данных на проверку наличия пользователя в ней
    if not result: #пользователя нет в базе данных, создаем его
        db_connection.execute(
            users.insert(), 
            [
                {'chat_id':message.chat.id, 'username':message.from_user.username, 'firstname':message.from_user.first_name, 'surname':message.from_user.last_name},
                ],
            return_defaults=True
        ) #запрос в базу данных на создание нового пользователя
    # отвечаем пользователю
    response = session.query(script).filter_by(triger_text=message.text).one() #в таблице scrip по столбцу triger делаем поиск соответствия сообщения пользователя тригеру  
    bot.send_message(message.chat.id, response[2]) 
    
def mailing():
    engine = create_engine("sqlite:///database.db", echo=True) 
    Session = sessionmaker(bind = engine)
    session = Session()
    db_connection = engine.connect()
    list_user = session.query(users).all() 
    for user in list_user:
        print(user)
        bot.send_message(user[1], 'Я рассылка!') 




if __name__ == '__main__':      
    logging.info("Bot start")
    bot.infinity_polling()

