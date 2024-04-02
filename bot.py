
import logging
import time
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message             
from aiogram.filters.command import Command   

# 2. Инициализация объектов
TOKEN = os.getenv('TOKEN')
bot = Bot(token='6848157270:AAGZcvamwh0neIvcN5Cb4KbaayRNiCmD6VQ')                        # Создаем объект бота
dp = Dispatcher()                             # Создаем объект диспетчера. Все хэндлеры(обработчики) должны быть подключены к диспетчеру
logging.basicConfig(level=logging.INFO, filename="log.txt", 
                    format='%(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s')

cyril_list = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ы','Ъ','Э','Ю','Я']
latin_list = ['A','B','V','G','D','E','E','ZH','Z','I','I','K','L','M','N','O','P','R','S','T','U','F','KH','TS','CH','SH','SHCH','Y','IE','E','IU','IA']

def letter_trans(string):
    trans_string = ""
    for item in string:
        is_alpha = item.isalpha()    
        if is_alpha:
            is_upper = item.isupper()
            if not is_upper:
                item = item.upper()
            if item in cyril_list:
                ind = cyril_list.index(item)
                if is_upper:
                    trans_string += latin_list[ind]
                else:
                    trans_string += latin_list[ind].lower()
            else:
                trans_string += item
        else:
            trans_string += item

    return trans_string

# 3. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name=} {user_id=} {time.asctime()} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)
    await bot.send_message(chat_id=user_id, text='Введите ФИО:')



    # 4. Обработка/Хэндлер на любые сообщения
@dp.message()
async def trans_name(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    chars=message.text     
    res=letter_trans(chars)
    logging.info(f'{user_name} {user_id}: {res}')
    await message.answer(text=res)


    # 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)