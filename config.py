## -*- coding: utf-8 -*-
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# BOT TOKEN
TOKEN = '#TOKEN'

# LINKS CONSTANTS
db_path = './database/test.db'
companies_path = './documents/companies.xlsx'

# DATABASE COMMANDS
create_db_command = '''CREATE TABLE COMPANY
                        (id INT PRIMARY KEY NOT NULL,
                        name TEXT ,
                        category TEXT,
                        subcategory TEXT,
                        description TEXT,
                        address TEXT,
                        phone TEXT,
                        schedule TEXT,
                        links TEXT
                        );'''
search_column = "SELECT * FROM COMPANY WHERE category = {}"

# TEXT CONSTANTS
menu_text = "Выберите категорию:"
category_text = "Выберите следующую категорию:"
no_handler_text = "На данный момент я не могу обрабатывать такие запросы"
help_text = 'Я собираюсь помочь тебе. Для перезапуска бота напиши /start'
func_dev_text = 'Функция находится в разработке'
chose_text = '<b>Выберите организацию:</b>'
start_text = '''Я помогу тебе найти информацию о всех организациях в Иннополисе. Если ты не нашел нужной информации,
то можешь позвонить в Консьерж-сервис: 
☎️: 8-800-222-22-87 
📩: helpme@innopolis.ru 
telegram: @InnopolisHelp! '''


# BUTTONS FOR KEYBOARDS
buttons = {
    'back': u'🔙' + ' Back',
}
