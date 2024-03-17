import telebot
from telebot import types

# Replace with your actual bot token obtained from BotFather
token = "YOUR TOKEN"
bot = telebot.TeleBot(token)

help_button = types.InlineKeyboardButton(text="Help", callback_data="help")
query_button = types.InlineKeyboardButton(text="Query", callback_data="query")

# Create keyboard layout
keyboard = types.InlineKeyboardMarkup()
keyboard.add(help_button, query_button)


class TrenBot:
    
    @bot.message_handler(commands=['start'])
    def send_menu(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Hi! What would you like to do?", reply_markup=keyboard)

    @bot.message_handler(commands=['stop'])
    def stop_bot(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Bye! Stopping the bot.")  
        bot.stop_polling()

    def help(message):
        pass

    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):
        if call.data == "help":
            # NotImplemented
            pass
        elif call.data == "query":
            #implement query here
            pass

if __name__ == '__main__':
    bot.polling()
