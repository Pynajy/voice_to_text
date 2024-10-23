import subprocess
import asyncio
import logging
import sys
import os
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from data.recognize import recognize_audio

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!\nОтправь/перешли мне голосовое сообщение/кружочек и я отправлю тебе его текстовый вариант")


@dp.message()
async def recognize_handler(message: Message) -> None:
    try:
        file_name_wav = f"{message.from_user.id}_{message.from_user.full_name}.wav"
        if message.voice:
            file_name = f"{message.from_user.id}_{message.from_user.full_name}.mp3"
            await bot.download(message.voice.file_id, file_name)
        elif message.video_note:
            file_name = f"{message.from_user.id}_{message.from_user.full_name}.mp4"
            await bot.download(message.video_note.file_id, file_name)
        
        subprocess.call(["ffmpeg", "-i", file_name, file_name_wav])

        result_recognize = await recognize_audio(file_name_wav)

        await message.answer(result_recognize)

        os.remove(file_name)
        os.remove(file_name_wav)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())