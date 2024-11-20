import asyncio
from aiogram import Bot,Dispatcher, F

from app.handler import router



async def main():
    bot = Bot(token='7962043379:AAGXTLRJIlnnDG0nfKHbrGmCkQ_FWo8zdYQ')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')