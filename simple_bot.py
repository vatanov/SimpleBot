import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def start_bot(bot, update):
    my_text = """Hello {}! I'm a simple bot and I understand following commands: 
{} 
{}
""".format(update.message.chat.first_name, '/start', '/choose_planet')
    logging.info('User {} pressed /start'.format(update.message.chat.username))
    update.message.reply_text(my_text)


def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text ('You wrote: "{}"'.format(text))


def choose_planet(bot, update):
    my_text = """Choose planet:
/Mercury
/Venus
/Earth
/Mars
/Jupiter
/Saturn
/Uranus
/Neptune
"""
    logging.info('User {} pressed /choose_planet'.format(update.message.chat.username))
    update.message.reply_text(my_text)


def planet(bot, update):
    selected_planet = update.message.text[1:]
    current_date = datetime.date.today()

    if selected_planet == 'Mercury':
        pln = ephem.Mercury(current_date)
    elif selected_planet == 'Venus':
        pln = ephem.Venus(current_date)
    elif selected_planet == 'Earth':
        pln = ephem.Earth(current_date)
    elif selected_planet == 'Mars':
        pln = ephem.Mars(current_date)
    elif selected_planet == 'Jupiter':
        pln = ephem.Jupiter(current_date)
    elif selected_planet == 'Saturn':
        pln = ephem.Saturn(current_date)
    elif selected_planet == 'Uranus':
        pln = ephem.Uranus(current_date)
    elif selected_planet == 'Neptune':
        pln = ephem.Neptune(current_date)

    pln_position = ephem.constellation(pln)
    my_text = "{} position {}".format(selected_planet, pln_position)
    update.message.reply_text(my_text)


def main():
    updtr = Updater(settings.TELEGRAM_API_KEY)

    updtr.dispatcher.add_handler(CommandHandler('start', start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    updtr.dispatcher.add_handler(CommandHandler('choose_planet', choose_planet))
    updtr.dispatcher.add_handler(CommandHandler('Mars', planet))
    updtr.dispatcher.add_handler(CommandHandler('Venus', planet))
    updtr.dispatcher.add_handler(CommandHandler('Earth', planet))
    updtr.dispatcher.add_handler(CommandHandler('Mercury', planet))
    updtr.dispatcher.add_handler(CommandHandler('Jupiter', planet))
    updtr.dispatcher.add_handler(CommandHandler('Saturn', planet))
    updtr.dispatcher.add_handler(CommandHandler('Uranus', planet))
    updtr.dispatcher.add_handler(CommandHandler('Neptune', planet))

    updtr.start_polling()
    updtr.idle()


if __name__ == '__main__':
    logging.info('Bot started')
    main()
