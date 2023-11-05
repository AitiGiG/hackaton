
import requests
from bs4 import BeautifulSoup as Bs
import telebot
from telebot import types
from datetime import datetime, timedelta

today = datetime.today()
formatted_today = today.strftime("%d.%m.%Y")
time_today = formatted_today.replace('.', '-')

today = datetime.today()
one_day = timedelta(days=1)
yesterday = today - one_day
yesterday = str(yesterday).split()[0]

news_id_h = 0

bot = telebot.TeleBot('6357969745:AAFiAFkWcSx_NLOYVLDrPenMAIGF2XIXcXM')
url_today = f'https://kaktus.media/?lable=8&date={time_today}&order=time'
url_yesterday = f'https://kaktus.media/?lable=8&date={yesterday}&order=time'

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton('Quit')
button_des = types.KeyboardButton('Description')
keyboard.add(button, button_des)

def get_news(url):
    request = requests.get(url)
    html = Bs(request.text, 'lxml')
    news = html.find_all('div', class_='Tag--article')
    news_card = []

    if len(news) == 0:
        return []

    for i in news:
        time = i.find('div', class_='ArticleItem--time').text.strip()
        img = i.find('img', class_='ArticleItem--image-img').get('data-src')
        text = i.find('a', class_='ArticleItem--name').text.strip()
        news_card.append({'img': img, 'text': f"{time}: {text}"})
    
    return news_card

news_list = get_news(url_today)
if not news_list:
    news_list = get_news(url_yesterday)

@bot.message_handler(commands=['start'])
def hello(message):
    for news_id, news_item in enumerate(news_list, start=1):
        if news_id <= 20:
            bot.send_message(message.chat.id, f"{news_id}: \n{news_item['text']} ")
    
    bot.send_message(message.chat.id, 'Выберите новость по номеру:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.isdigit())
def news_id(message):
    if int(message.text) <= 20:
        bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=keyboard)
    global news_id_h 
    news_id_h = int(message.text)
    # print(news_id_h)

@bot.message_handler(func=lambda message: message.text == 'Description')
def news_description(message):
    user_id = message.from_user.id
    for news_id, news_item in enumerate(news_list, start=1):
        if news_id_h == news_id:
            bot.send_message(user_id, f"{news_id}:\n {news_item['img']} \n{news_item['text']} ")

@bot.message_handler(func=lambda message: message.text == 'Quit')
def quit(message):
    bot.send_message(message.chat.id, 'До свидания')

bot.polling()
