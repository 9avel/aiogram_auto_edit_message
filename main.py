import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from conf import BOT_TOKEN

# bot
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    """
     func command /start
    """
    await message.delete()
    await message.answer(f"Hi User!")
    # add in file chat id and message id
    with open('data.txt', 'a') as file:
        file.write(f'{message.chat.id},{message.message_id + 1}\n')


async def random_num(bo_t: Bot):
    """
    edit message chance number 0 to 10
    """
    with open('data.txt') as file:
        for line in file.readlines():
            line = line.strip().split(',')
            # try and except use for if text=new text, throwing an exception
            try:
                await bo_t.edit_message_text(text=f'Hi User! Your number {random.randint(0, 10)}',
                                             chat_id=line[0],
                                             message_id=line[-1])
            except:
                pass


async def task_random_num(sec):
    """
    start while True with an interval sleep
    """
    while True:
        await asyncio.sleep(sec)
        await random_num(bot)


async def run() -> None:
    """
    start bot and task
    :return:
    """
    loop = asyncio.get_event_loop()
    loop.create_task(task_random_num(5))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run())
