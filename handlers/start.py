from aiogram import Router, types, F
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="о нас", callback_data = "about_us"),
                types.InlineKeyboardButton(text="наши вакансии", callback_data = "vacancy"),
            ],
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")
            ]
        ]
    )
    await message.answer(f"Hello {name}", reply_markup=kb)
    # await message.answer("Hi")

@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Текст о нас")