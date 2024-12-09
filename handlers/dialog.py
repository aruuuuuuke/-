from aiogram import Router, types, F
from aiogram.filters import Command

opros_router = Router()

@opros_router.message(Command("opros"))
async def start_opros(message: types.Message):
    await message.answer("Как вас зовут?")