import requests
import asyncio
import logging
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.filters import CommandStart



bot = Bot(token=tg_bot_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")


dp.message()
async def show_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q=message.text&appid=open_weather_token&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"
        
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())