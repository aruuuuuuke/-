from aiogram import Router, types
from bot_config import dp, bot

echo_router = Router()

@echo_router.message()
async def echo_handler(message: types.Message):
    # await message.answer(txt)
    await bot.send_message(
        chat_id = message.from_user.id,
        text = "I don't understand")

