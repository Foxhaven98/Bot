import telebot, wikipedia, re, random
from telebot import types

bot = telebot.TeleBot('5218918358:AAGaIfU5Iv19xQbwXNu0zG9daW62-HYJlZs')

wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Зодиак")
    item2 = types.KeyboardButton("Wiki")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Я могу найти определение любого слова или рассказать анекдот. Если хочешь гороскоп, нажми на кнопку, иначе вводи слово для которого ищешь определение', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Зодиак":
        bot.send_message(message.from_user.id, "Сейчас я расскажу тебе гороскоп на сегодня.")
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_riby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_riby)

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, getwiki(message.text))
first = ["Сегодня — идеальный день для новых начинаний.","Сегодня у вас будет шанс добиться многого.","Сегодня вам многое будет по силам."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Сосредоточьтесь на работе или других полезных делах и помните про"]
second_add = ["отношения с друзьями и близкими.", "отдых."]
third = ["Вторая половина дня принесет хорошие новости и неожиданные открытия. Она обещает заметные успехи в работе. Вы решите непростые задачи, справитесь с тем, что раньше не получалось. Вероятны удачные покупки и сделки.","Вторая половина дня позволит сосредоточиться именно на том, что вам интересно. Могут решиться какие-то важные вопросы, прежде тревожившие и вас, и ваших близких. Это время подойдет для домашних дел: они не покажутся ни утомительными, ни скучными.","Вторая половина дня порадует новостями, касающимися кого-то из членов семьи или других очень близких вам людей. Возможны неожиданные поездки. Вы будете рады возможности отправиться в дорогу в хорошей компании."]

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'zodiac':
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0)
