from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values

token= dotenv_values(".env").get("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()