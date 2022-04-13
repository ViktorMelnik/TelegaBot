import telebot
from random import choice
from telebot import types

bot = telebot.TeleBot('5139034803:AAFbtkNzDThnVlK9quds0TyqxQD344TUkPg')

@bot.message_handler(commands=['start'])
def start(message):
    mass = f'<b>{message.from_user.first_name}</b>, <b> you should ask a question</b>'
    bot.send_message(message.chat.id, mass, parse_mode='html')
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Answer Yes or No")
    item2 = types.KeyboardButton("Answer with a taro-card")
    item3 = types.KeyboardButton("Answer whith a number")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '<b>and choose type of answer</b>', parse_mode='html', reply_markup=markup)
    
    stiker = open('static/big.webp', 'rb')
    bot.send_sticker(message.chat.id, stiker)
    
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.chat.type == 'private':
        if message.text == 'Answer Yes or No':
            bot.send_message(message.chat.id, str(choice(['Yes', 'No'])))
        elif message.text == 'Answer with a taro-card':
            f01 = open('static/Tower.webp', 'rb')
            f02 = open('static/ThreeOfWands.webp', 'rb')
            f03 = open('static/TwoOfCups.webp', 'rb')
            f04 = open('static/TwoOfPentacles.webp', 'rb')
            f05 = open('static/TwoOfSwords.webp', 'rb')
            f06 = open('static/TwoOfWands.webp', 'rb')
            f07 = open('static/WheelOfFortune.webp', 'rb')
            f08 = open('static/World.webp', 'rb')
            f09 = open('static/AceOfCups.webp', 'rb')
            f10 = open('static/AceOfPentacles.webp', 'rb')
            f11 = open('static/AceOfSwords.webp', 'rb')
            f12 = open('static/AceOfWands.webp', 'rb')
            f13 = open('static/Chariot.webp', 'rb')
            f14 = open('static/Death.webp', 'rb')
            f15 = open('static/Devil.webp', 'rb')
            f16 = open('static/EightOfCups.webp', 'rb')
            f17 = open('static/EightOfPentacles.webp', 'rb')
            f18 = open('static/EightOfSwords.webp', 'rb')
            f19 = open('static/EightOfWands.webp', 'rb')
            f20 = open('static/Emperor.webp', 'rb')
            f21 = open('static/Empress.webp', 'rb')
            f22 = open('static/FiveOfCups.webp', 'rb')
            f23 = open('static/FiveOfPentacles.webp', 'rb')
            f24 = open('static/FiveOfSwords.webp', 'rb')
            f25 = open('static/FiveOfWands.webp', 'rb')
            f26 = open('static/Fool.webp', 'rb')
            f27 = open('static/FourOfCups.webp', 'rb')
            f28 = open('static/FourOfPentacles.webp', 'rb')
            f29 = open('static/FourOfSwords.webp', 'rb')
            f30 = open('static/FourOfWands.webp', 'rb')
            f31 = open('static/HangedMan.webp', 'rb')
            f32 = open('static/Hermit.webp', 'rb')
            f33 = open('static/Hierophant.webp', 'rb')
            f34 = open('static/HighPriestess.webp', 'rb')
            f35 = open('static/Judgement.webp', 'rb')
            f36 = open('static/Justice.webp', 'rb')
            f37 = open('static/KingOfCups.webp', 'rb')
            f38 = open('static/KingOfPentacles.webp', 'rb')
            f39 = open('static/KingOfSwords.webp', 'rb')
            f40 = open('static/KingOfWands.webp', 'rb')
            f41 = open('static/KnightOfCups.webp', 'rb')
            f42 = open('static/KnightOfPentacles.webp', 'rb')
            f43 = open('static/KnightOfSwords.webp', 'rb')
            f44 = open('static/KnightOfWands.webp', 'rb')
            f45 = open('static/Lovers.webp', 'rb')
            f46 = open('static/Magician.webp', 'rb')
            f47 = open('static/Moon.webp', 'rb')
            f48 = open('static/NineOfCups.webp', 'rb')
            f49 = open('static/NineOfPentacles.webp', 'rb')
            f50 = open('static/NineOfSwords.webp', 'rb')
            f51 = open('static/NineOfWands.webp', 'rb')
            f52 = open('static/PageOfCups.webp', 'rb')
            f53 = open('static/PageOfPentacles.webp', 'rb')
            f54 = open('static/PageOfSwords.webp', 'rb')
            f55 = open('static/PageOfWands.webp', 'rb')
            f56 = open('static/QueenOfCups.webp', 'rb')
            f57 = open('static/QueenOfPentacles.webp', 'rb')
            f58 = open('static/QueenOfSwords.webp', 'rb')
            f59 = open('static/QueenOfWands.webp', 'rb')
            f60 = open('static/SevenOfCups.webp', 'rb')
            f61 = open('static/SevenOfPentacles.webp', 'rb')
            f62 = open('static/SevenOfSwords.webp', 'rb')
            f63 = open('static/SevenOfWands.webp', 'rb')
            f64 = open('static/SixOfCups.webp', 'rb')
            f65 = open('static/SixOfPentacles.webp', 'rb')
            f66 = open('static/SixOfSwords.webp', 'rb')
            f67 = open('static/SixOfWands.webp', 'rb')
            f68 = open('static/Star.webp', 'rb')
            f69 = open('static/Strength.webp', 'rb')
            f70 = open('static/Sun.webp', 'rb')
            f71 = open('static/ThreeOfCups.webp', 'rb')
            f72 = open('static/ThreeOfPentacles.webp', 'rb')
            f73 = open('static/ThreeOfSwords.webp', 'rb')
            f74 = open('static/Temperance.webp', 'rb')
            f75 = open('static/TenOfCups.webp', 'rb')
            f76 = open('static/TenOfPentacles.webp', 'rb')
            f77 = open('static/TenOfSwords.webp', 'rb')
            f78 = open('static/TenOfWands.webp', 'rb')
            bot.send_photo(message.chat.id, choice([f01, f02, f03, f04, f05, f06, f07, f08, f09, f10,
                                                    f11, f12, f13, f14, f15, f16, f17, f18, f19, f20,
                                                    f21, f22, f23, f24, f25, f26, f27, f28, f29, f30,
                                                    f31, f32, f33, f34, f35, f36, f37, f38, f39, f40,
                                                    f41, f42, f43, f44, f45, f46, f47, f48, f49, f50,
                                                    f51, f52, f53, f54, f55, f56, f57, f58, f59, f60,
                                                    f61, f62, f63, f64, f65, f66, f67, f68, f69, f70,
                                                    f71, f72, f73, f74, f75, f76, f77, f78]))
        elif message.text == 'Answer whith a number':
            bot.send_message(message.chat.id, choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))



bot.polling(non_stop=True)