from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import bot, dp
import logging

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Что является столицей Австралии?"
    answers = [
        "Канберра",
        "Аделаида",
        "Сидней",
        "Мельбурн",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "Как называется самый маленький океан?"
    answers = [
        "Северный Ледовитый океан",
        "Индийский океан",
        "Тихий океан",
        "Атлантический океан",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="ИЗЗИ!",
        open_period=10,
        reply_markup=markup
    )

@dp.message_handler(commands=['mem'])
async def command_start(message: types.Message):
    photo = open('photo/mem.jfif', 'rb')
    await bot.send_photo(message.from_user.id, photo)

@dp.message_handler()
async def echo(messeg:types.Message):
    print(messeg)
    if messeg.text.isnumeric()==True:
        num=int(messeg.text)
        await bot.send_message(messeg.from_user.id, num*num)
    else:
        await bot.send_message(messeg.from_user.id,messeg.text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)