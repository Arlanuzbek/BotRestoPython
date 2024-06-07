import logging
import asyncio
import random

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.utils import markdown
from aiogram.enums import ParseMode


from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder


from aiogram import types
from aiogram.filters import CommandStart, Command


BOT_TOKEN = "7034349236:AAEOwjxUXPaL23-XJcmcxWCISR1iowOflHI"


bot=Bot(token=BOT_TOKEN)
dp=Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.message):
    url = "https://almaty.tv/news_photo/1643036410_news_b.png"
    await message.answer(
        text=f"{markdown.hide_link(url)}Привет! Я бот который найдёт вам пищу которую вы хотите ! {markdown.hbold(message.from_user.full_name)}",

        parse_mode=ParseMode.HTML,
    )
url1 = "https://www.vremena-goda.ru/upload/iblock/c01/kurinaya_lapsha_kuritsa.jpg?2021072301"
url2 = "https://www.vremena-goda.ru/upload/iblock/dbd/borsh.jpg?2021072301"
url3 = "https://www.vremena-goda.ru/upload/iblock/9f5/sup_tom_yam.jpg?2021072301"
url4 = "https://www.vremena-goda.ru/upload/iblock/91d/okroshka_myasnaya_kvas.jpg?2021072301"
url5 = "https://www.vremena-goda.ru/upload/iblock/eb0/okroshka_ovoshnaya_kefir.jpg?2021072301"
url6 = "https://www.vremena-goda.ru/upload/iblock/c69/papardelli_vyrezka_suvid.jpg?2021072301"
url7 = "https://www.vremena-goda.ru/upload/iblock/098/spagetti_moreproducti.jpg?2021072301"
url8 = "https://www.vremena-goda.ru/upload/iblock/b02/pasta_shpinat.jpg?2021072301"
url9 = "https://www.vremena-goda.ru/upload/iblock/78a/burger_telaytina.jpg?2021072301"
url10 = "https://www.vremena-goda.ru/upload/iblock/b8b/burger_kurinnaya.jpg?2021072301"
url11 = "https://www.vremena-goda.ru/upload/resize_cache/iblock/c88/600_400_2d7a58ff99b324185ccb5ad5dfbdb5e85/adzhika.jpg?2021072301"
url12 = "https://www.vremena-goda.ru/upload/resize_cache/iblock/55a/600_400_2d7a58ff99b324185ccb5ad5dfbdb5e85/ketchup.jpg?2021072301"
url13 = "https://www.vremena-goda.ru/upload/resize_cache/iblock/3dd/600_400_2d7a58ff99b324185ccb5ad5dfbdb5e85/narsharab.jpg?2021072301"
url14 = "https://www.vremena-goda.ru/upload/resize_cache/iblock/339/600_400_2d7a58ff99b324185ccb5ad5dfbdb5e85/ketchup.jpg?2021072301"
url15 = "https://www.vremena-goda.ru/upload/resize_cache/iblock/604/600_400_2d7a58ff99b324185ccb5ad5dfbdb5e85/tartar.jpg?2021072301"
url16 = "https://www.vremena-goda.ru/upload/resize_cache/iblock/41d/600_400_2d7a58ff99b324185ccb5ad5dfbdb5e85/hren.jpg?2021072301"
url17 = "https://www.vremena-goda.ru/upload/resize_cache/iblock/892/600_400_2d7a58ff99b324185ccb5ad5dfbdb5e85/olive_oil.jpg?2021072301"

Soup_List=[f"Суп лапша куриная с перепелиным яйцом -- {url1} ", f"Борщ со сметаной -- {url2} ", f"Суп Том Ям -- {url3} ", f"Окрошка мясная на квасе -- {url4} ", f"Окрошка на кефире -- {url5} "]
Pasta_List=[f"Паппарделле с говяжьей вырезкой сувид вешенками и вялеными томатами -- {url6} ", f"Спагетти с морепродуктами в томатном соусе -- {url7} ", f"Паста со шпинатом и курицей -- {url8} "]
Burger_List=[f"Бургер Трюфельный с картофелем фри -- {url9} ", f"Бургер куриный с картофелем фри -- {url10} "]
Sauce_List=[f"Аджика домашняя из томатов с чесноком -- {url11} ", f"Кетчуп томатный -- {url12} ", f"Соус гранатовый Наршараб -- {url13} ", f"Соус Чили сладкий -- {url14} ", f"Соус Тар Тар -- {url15} ", f"Майонез -- {url16} ", f"Оливковое масло -- {url17} "]

@dp.message(CommandStart())
async def handle_start(message: types.message):
    url = "https://cdn.sites.admitad.ru/www.admitad.ru/2023/08/admitad-bot-blog.png"
    await message.answer(
        text=f"{markdown.hide_link(url)}Привет, я бот который найдёт пищу под ваши хотелки! {markdown.hbold(message.from_user.full_name)} \n У меня есть следующие команды:\n/films\n/random",

        parse_mode=ParseMode.HTML,
    )

@dp.message(Command("menu"))
async def films_type(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Супы")],
        [types.KeyboardButton(text="Паста")],
        [types.KeyboardButton(text="Бургер")],
        [types.KeyboardButton(text="Соус")],
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Вот ваше меню!", reply_markup=keyboard)

@dp.message(F.text.lower() == "супы")
async def show_random(message: types.Message):
    await message.answer(
        text=f"{(message.from_user.full_name)} Ваш суп на сегодня- {random.choice(Soup_List)} ",
    )

@dp.message(F.text.lower() == "паста")
async def show_random(message: types.Message):
    await message.answer(
        text=f"{(message.from_user.full_name)} Ваша паста на сегодня- {random.choice(Pasta_List)} ",
    )

@dp.message(F.text.lower() == "бургер")
async def show_random(message: types.Message):
    await message.answer(
        text=f"{(message.from_user.full_name)} Ваш бургер на сегодня- {random.choice(Burger_List)} ",
    )

@dp.message(F.text.lower() == "соус")
async def show_random(message: types.Message):
    await message.answer(
        text=f"{(message.from_user.full_name)} Вот ваш соус - {random.choice(Sauce_List)} ",
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
