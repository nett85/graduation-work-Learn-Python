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



# bot = telebot.TeleBot('5708232763:AAFnpeiVxaUcOyEAVO7Wf1Snp_-gyun3rcw', parse_mode=None)
# logging.basicConfig(filename='bot.log', level=logging.INFO)


# @bot.message_handler(commands=['start'])
# def start(message):
#     engine = create_engine("sqlite:///database.db", echo=True) #создание файла базы данных
#     db_connection = engine.connect() #подключение к базе данных
#     Session = sessionmaker(bind = engine) #настраиваем сессию
#     session = Session() #подключаем  сессию
#     result = session.query(users).filter_by(username = message.from_user.username).one_or_none() #запрос к базе данных на проверку наличия пользователя в ней
#     if not result: #пользователя нет в базе данных, создаем его
#         db_connection.execute(
#             users.insert(), 
#             [
#                 {'username':message.from_user.username, 'firstname':message.from_user.first_name, 'surname':message.from_user.last_name},
#                 ],
#             return_defaults=True
#         ) #запрос в базу данных на создание нового пользователя
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}{message.from_user.last_name}!')





# @bot.message_handler()
# def message(message):    
#     if message.text == 'id':
#         bot.send_message(message.chat.id, f'Вся информация о Вас:{message.chat.id, str(message)}') 
#     else:
#         bot.send_message(
#                 message.chat.id, 
#                 '''К сожалению, я не могу поддержать беседу. 
#                 Но все актуальные новости и акции представлены на нашем сайте. 
#                 Вызовите команду "/website" для перехода на него.'''
#                 ) 




# engine = create_engine("sqlite:///database.db", echo=True)
# db_connection = engine.connect()


   # bot.send_message(message.chat.id, 'Привет,{message.from_user.first_name}{message.from_user.last_name}')


# insertion_query = users.insert().values([{'username':'username', 'firstname':'first_name', 'surname':'last_name'}])
#         insertion_query.commit()


# import telebot

# bot = telebot.TeleBot('5933334625:AAFaGMGaD2k3zQeeSkVuGJY8xmPmVb4QOmM')
# parse_mode=None

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет')

# # bot.infinity_polling()
# # bot.polling()
# # bot.idle()   
# bot.polling(none_stop=True, interval=0)


# markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    # website = types.KeyboardButton('Веб сайт нашего магазина')
    # markup.add(website)
    # bot.send_message(message.chat.id, 'Вся самая актуальная информация по нашим услугам и их стоимости представлена на нашем сайте. Переходи на него скорей!', reply_markup=markup)
# if message.text == '/start':
# {message.from_user.first_name}{message.from_user.last_name}



# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")





# @bot.message_handler()
# def start_message(message):
#     engine = create_engine("sqlite:///database.db", echo=True)
#     db_connection = engine.connect()
#     instance = db_connection.query(users).filter(users.username == message.from_user.username).one_or_none()
#     if message.text == '/start':
#         db_connection.execute(
#             users.insert(), 
#             [
#                 {'username':message.from_user.username, 'firstname':message.from_user.first_name, 'surname':message.from_user.last_name},
#                 ],
#             return_defaults=True
#         )
#         bot.send_message(message.chat.id, f'Приветствую Вас, {message.from_user.first_name} {message.from_user.last_name}!')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Вся информация о Вас:{message.chat.id, str(message)}') 
#     else:
#         bot.send_message(message.chat.id, 'К сожалению, я не могу поддержать беседу. Но все актуальные новости и акции представлены на нашем сайте. Вызовите команду "/website" для перехода на него.') 
    