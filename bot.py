from _parser import parse_recipe  # импортируем функцию для парсинга
import config  # файл с токеном
import telebot  # библиотека для написания бота
from telebot import types  # для создания кнопок

bot = telebot.TeleBot(config.token)  # создаём бота


@bot.message_handler(commands=['start'])  # обработчик реагирующий на команду '/start'
def start(message):  # функция для приветствия
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создаём разметку кнопок
    btn1 = types.KeyboardButton('Хочу коктейль!')  # создаём кнопку
    markup.add(btn1)  # добавляем кнопку на панель
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Хочешь коктейль?)'.format(message.from_user),
                     reply_markup=markup)  # отправляем приветствие


@bot.message_handler(content_types=['text'])  # обработчик реагирующий на текстовые сообщения
def main(message):  # функция для выбора алкоголя
    if message.text == 'Хочу коктейль!' or message.text == 'Хочу другой коктейль.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Алко')
        btn2 = types.KeyboardButton('Безалко')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Алкогольный/Безалкогольный?', reply_markup=markup)
        bot.register_next_step_handler(message,
                                       how_alco)  # метод, который ждёт сообщение от пользователя и потом вызывает указанную функцию с аргументом 'message'


def how_alco(message):  # логика работы бота в зависимости от выбранного алкоголя
    if message.text == "Безалко":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn6 = types.KeyboardButton(text='Классический лимонад')
        btn7 = types.KeyboardButton(text='Малиновый лимонад')
        btn4 = types.KeyboardButton(text='Холодный латте с орео')
        btn5 = types.KeyboardButton(text='Безалкогольный мохито')
        btn8 = types.KeyboardButton(text='Клубничный лимонад')

        markup.add(btn4, btn5, btn6, btn7, btn8)

        bot.send_message(message.chat.id, text='Выбери коктейль)', reply_markup=markup)
        bot.register_next_step_handler(message, nalc_cocktails)

    elif message.text == "Алко":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('белый ром')
        btn2 = types.KeyboardButton('водка')
        btn3 = types.KeyboardButton('ликер')
        btn4 = types.KeyboardButton('просекко')
        btn5 = types.KeyboardButton('лимончелло')
        btn6 = types.KeyboardButton('тёмное пиво')
        btn7 = types.KeyboardButton('бурбон')
        btn8 = types.KeyboardButton('текила')
        btn9 = types.KeyboardButton('джин')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id, text='Какой алкоголь у тебя есть?', reply_markup=markup)
        bot.register_next_step_handler(message, alc_cocktails)


def alc_cocktails(message):  # функция для отправки рецепта в зависимости от выбранного алкоголя
    if message.text == 'белый ром':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/57-mohito')  # функция, которая парсит рецепт с сайта
        text2 = parse_recipe('https://ru.inshaker.com/cocktails/35-long-aylend-ays-ti')
        bot.send_message(message.chat.id, text='Можно попробовать мохито)\n' + text, reply_markup=markup)
        bot.send_message(message.chat.id, text='Можно попробовать Лонг айленд айс ти)\n' + text2, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'водка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/314-golubaya-laguna')
        text2 = parse_recipe('https://ru.inshaker.com/cocktails/563-malinovoe-puteshestvie')
        text3 = parse_recipe('https://ru.inshaker.com/cocktails/15-belyy-russkiy')
        text4 = parse_recipe('https://ru.inshaker.com/cocktails/29-kosmopoliten')
        text5 = parse_recipe('https://ru.inshaker.com/cocktails/35-long-aylend-ays-ti')
        text6 = parse_recipe('https://ru.inshaker.com/cocktails/814-seks-na-plyazhe')
        bot.send_message(message.chat.id, text='Можно попробовать коктейль "Голубая лагуна"\n' + text,
                         reply_markup=markup)
        bot.send_message(message.chat.id, text='Можно попробовать малиновое путешевствие)\n' + text2,
                         reply_markup=markup)
        bot.send_message(message.chat.id, text='Можно попробовать белый русский)\n' + text3, reply_markup=markup)
        bot.send_message(message.chat.id, text='Можно попробовать Космополитен)\n' + text4, reply_markup=markup)
        bot.send_message(message.chat.id, text='Можно попробовать Лонг айленд айс ти)\n' + text5, reply_markup=markup)
        bot.send_message(message.chat.id, text='Можно попробовать Секс на пляже)\n' + text6, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'ликер':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/164-b-52')
        text2 = parse_recipe('https://ru.inshaker.com/cocktails/814-seks-na-plyazhe')
        bot.send_message(message.chat.id, text='Можно попробовать б-52)\n' + text, reply_markup=markup)
        bot.send_message(message.chat.id, text='Можно попробовать Секс на пляже)\n' + text2, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'просекко':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/17-bellini')
        text2 = parse_recipe('https://ru.inshaker.com/cocktails/41-mimoza')
        bot.send_message(message.chat.id, text='Можно попробовать беллини)\n' + text, reply_markup=markup)
        bot.send_message(message.chat.id, text='Можно попробовать мимоза)\n' + text2, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'лимончелло':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/829-skitls')
        bot.send_message(message.chat.id, text='Можно попробовать скитлс)\n' + text, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    if message.text == 'тёмное пиво':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/271-vishnevoe-pivo')
        bot.send_message(message.chat.id, text='Можно попробовать вишнёвое пиво)\n' + text, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'бурбон':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/53-old-feshen')
        text2 = parse_recipe('https://ru.inshaker.com/cocktails/18-viski-sauer')
        bot.send_message(message.chat.id, text='Можно попробовать Олд фешен)\n' + text, reply_markup=markup)
        bot.send_message(message.chat.id, text='Можно попробовать Виски сауэр)\n' + text2, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'текила':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/35-long-aylend-ays-ti')
        bot.send_message(message.chat.id, text='Можно попробовать Лонг айленд айс ти)\n' + text, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'джин':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/35-long-aylend-ays-ti')
        bot.send_message(message.chat.id, text='Можно попробовать Лонг айленд айс ти)\n' + text, reply_markup=markup)
        bot.register_next_step_handler(message, main)


def nalc_cocktails(message):  # функция для отправки рецепта в зависимости от выбранного алкоголя
    if message.text == 'Классический лимонад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/473-klassicheskiy-limonad-v-kuvshine')
        bot.send_message(message.chat.id, text=text, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'Малиновый лимонад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/566-malinovyy-limonad')
        bot.send_message(message.chat.id, text=text, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'Холодный латте с орео':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/1124-holodnyy-latte-s-oreo')
        bot.send_message(message.chat.id, text=text, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'Безалкогольный мохито':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/679-mohito-bezalkogolnyy')
        bot.send_message(message.chat.id, text=text, reply_markup=markup)
        bot.register_next_step_handler(message, main)

    elif message.text == 'Клубничный лимонад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Хочу другой коктейль.')
        markup.add(btn1)
        text = parse_recipe('https://ru.inshaker.com/cocktails/480-klubnichnyy-limonad')
        bot.send_message(message.chat.id, text=text, reply_markup=markup)
        bot.register_next_step_handler(message, main)


if __name__ == '__main__':
    bot.infinity_polling()  # ждём-с сообщений
