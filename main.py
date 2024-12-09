import asyncio
import logging
from dotenv import dotenv_values
from handlers.start import start_router
from handlers.other_messages import echo_router
from handlers.picture import picture_router
from bot_config import dp, bot
from handlers.dialog import opros_router

async def main():
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(echo_router)
    dp.include_router(opros_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())