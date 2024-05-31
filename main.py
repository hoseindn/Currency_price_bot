import telebot
import requests

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "خوش آمدید")
    bot.reply_to(message, "لطفا نماد ارز خود را وارد کنید!")


@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol = message.text.upper()
    res = requests.get(f"TOKEN binance ={symbol}")

    if res.status_code == 200:
        data = res.json()
        bot.reply_to(message, f"نماد = {data['symbol']}\n قیمت =  {data['price']}")
    else:
        bot.reply_to(message, f"   مقدار وارد شده {message.text}  صحیح نیست! ")


bot.infinity_polling()
