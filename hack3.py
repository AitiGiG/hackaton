import requests
from bs4 import BeautifulSoup as Bs
import telebot
import datetime
today = datetime.date.today()
formatted_today = today.strftime("%d.%m.%Y")
time = formatted_today.replace('.','-')

bot = telebot.TeleBot('6357969745:AAFiAFkWcSx_NLOYVLDrPenMAIGF2XIXcXM')
url = f'https://kaktus.media/?lable=8&date=2023-11-03&order=time'


def parsing(url):
    request = requests.get(url)
    html= Bs(request.text , 'lxml')
    news = html.find_all('div' , class_ = 'Tag--article')
    news_card = []
    for i in news:
        # id  = i.find('a').get('href')
        time = i.find('div', class_ = 'ArticleItem--time').text.strip()
        img = i.find('img', class_ = 'ArticleItem--image-img').get('data-src')
        text = i.find('a' , class_ = 'ArticleItem--name').text.strip()

        news_card.append({'img': img, 'text': f"{time}: {text}"})
    
    return news_card
news_list = parsing(url)

@bot.message_handler(commands=['start'])
def hello(message):
    for news_id, news_item in enumerate(news_list, start=1):
        if news_id <= 20:
            bot.send_message(message.chat.id, f"{news_id}: \n {news_item['img']}\n{news_item['text']} ")
    bot.send_message(message.chat.id, 'Выберите новость по номеру: ')

@bot.message_handler()
def news_id(message):
    for news_id, news_item in enumerate(news_list, start=1):
        if news_id <= 20:
            if int(message.text) == news_id:
                bot.send_message(message.chat.id, f"{news_id}: \n {news_item['img']}\n{news_item['text']}") 
                break
            if news_id > 20:
                bot.send_message(message.chat.id,  'Выберите существующее id: ')




                
bot.polling()

