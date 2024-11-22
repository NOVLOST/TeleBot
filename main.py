import asyncio
from aiogram import Dispatcher

from app.handler import router,bot


#NOTE:доделать фильтрацию ввода ,сделать закачку фото из коложа и в виде документа ,закачка видео и других документов
async def main():

    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
