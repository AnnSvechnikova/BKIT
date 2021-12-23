import telebot
from telebot import types
import config
import dbworker

# Создание бота
bot = telebot.TeleBot(config.TOKEN)

# переменная для накопления результата выбора
choice = ''

# надписи на кнопках
mes_yes = "да"
mes_no = "нет"


# вопросы бота
mes_place = "провести встречу на открытом воздухе?"
mes_is_active = "предпочитаете активный отдых?"
mes_quantity = "компания меньше пяти человек?"

#рекомендации бота
recs = {
    '000':'экскурсия в музей',
    '001':'квест',
    '010':'лазертаг',
    '011':'батутный центр',
    '100':'экскурсия по городу',
    '101':'пикник',
    '110':'волейбол',
    '111':'велопрогулка'
}

# создание кнопок
def make_btn_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton(mes_yes)
    itembtn2 = types.KeyboardButton(mes_no)
    markup.add(itembtn1, itembtn2)
    return markup

# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Я подскажу вам идею для встречи с друзьями')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_PLACE.value)
    bot.send_message(message.chat.id, mes_place)
    bot.send_message(message.chat.id, 'Для ответа нажмите одну из кнопок', reply_markup=make_btn_markup())


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_PLACE.value)
    bot.send_message(message.chat.id, mes_place)
    bot.send_message(message.chat.id, 'Для ответа нажмите одну из кнопок')


# обработка первого вопроса
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_PLACE.value)
def get_place(message):
    text = message.text
    if text == mes_yes or text==mes_no:
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_IS_ACTIVE.value)
        # Сохраняем выбранный ответ
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_PLACE.value),
                    '1' if text == mes_yes else '0')
        bot.send_message(message.chat.id, mes_is_active)
    else:
        bot.send_message(message.chat.id, 'Для ответа нажмите одну из кнопок')


# Обработка второго вопроса
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_IS_ACTIVE.value)
def second_num(message):
    text = message.text
    if text == mes_yes or text==mes_no:
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_QUANTITY.value)
        # Сохраняем выбранный ответ
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_IS_ACTIVE.value),
                    '1' if text == mes_yes else '0')
        bot.send_message(message.chat.id, mes_quantity)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, нажмите одну из кнопок')


# Обработка третьего вопроса
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_QUANTITY.value)
def second_num(message):
    text = message.text
    if text == mes_yes or text==mes_no:
        # Сохраняем выбранный ответ
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_QUANTITY.value),
                    '1' if text == mes_yes else '0')
        bot.send_message(message.chat.id, "подходящий вариант досуга")
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, нажмите одну из кнопок')
    # Читаем ответы пользователя из базы данных
    k = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_PLACE.value))
    k += dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_IS_ACTIVE.value))
    k += dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_QUANTITY.value))
    bot.send_message(message.chat.id, recs[k])
    # Меняем текущее состояние
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_PLACE.value)
    # Выводим
    bot.send_message(message.chat.id, "Попробуем еще раз!")
    bot.send_message(message.chat.id, mes_place)


if __name__ == '__main__':
    bot.infinity_polling()
