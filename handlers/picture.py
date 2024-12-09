from aiogram import Router, types
from aiogram.filters import Command


picture_router = Router()

@picture_router.message(Command("picture"))
async def picture_handler(message: types.Message):
    photo = types.FSInputFile("images/DSC09178.JPG")
    await message.answer_photo(
        photo = photo,
        caption = "Garden!"
    )