from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(update, context):
        print("Вызван /start")
        update.message.reply_text('Привет, пользователь! Ты вызвал компанду /start')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater("2144542659:AAG5xY4n9plb5ugX-DStqndy5--tmJCEfoE"
, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
    
main()