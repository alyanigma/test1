import pandas as pd
from aiogram import F, Router, Dispatcher, Bot, types, Form
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os
import asyncio
import logging
import sys

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(token= TOKEN)
dp = Dispatcher()
data = None
router = Router()

class Form(StatesGroup):
   stata = State()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.reply("Привет! Пришли мне файл для чтения данных.")

@form_router.message(F.document)
async def take_doc(message: Message, state: FSMContext):
   global data
   try:
      await message.answer('Подождите, загрузка файла может занять некоторое время')
      file_id  = message.document.file_id
      file = await bot.get_file(file_id)
      file_path = file.file_path
      my_object = io.BytesIO()
      MyBinaryIO = await bot.download_file(file_path, my_object)
      data = pd.read_excel(MyBinaryIO)
      await message.answer('Файл успешно загружен!')
   except Exception as e:
      await message.answer(f"Произошла ошибка при загрузке файла. {e}")
   return

@router.message(F.text == 'Выбрать группу')
async def report(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.name)
    await message.answer("Введите номер группы: ")

@router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    if data is None:
        await message.answer('Вы не отправили документ для обработки!')
    else:
        await state.update_data(name=message.text)
        await message.answer(f"Номер вашей группы: {html.quote(message.text)}")
skore = data['Группа'].str.contains(str(message.text)).sum()

@router.message()
async def process_name(message: Message, state: FSMContext) -> None:
    if skore == 0:
        await message.answer(f'К сожалению по группе с таким номером нет данных.', reply_markup=kb.main)
    else:
        await message.answer(f'Если хотите получить отчет по группе: {html.quote(message.text)}. Нажмите кнопку отчет', reply_markup=kb.report1)
    


@router.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def process_document(message: types.Message, state: FSMContext):
    # Получаем информацию о файле
    document = message.document
    file_id = document.file_id
    file_name = document.file_name
    
    # Скачиваем файл
    file_path = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_path.file_path)
    
    try:
        # Обрабатываем файл и извлекаем данные
        data = process_file(downloaded_file)

maindata = pd.read_excel("lab_pi_101.xlsx")
CEst = maindata.shape[0]
CEst1 = maindata['Группа'].str.contains('ПИ101').sum()
UN = maindata[maindata['Группа'] == "ПИ101"]
N = len(UN['Личный номер студента'].unique())
U = maindata.loc[maindata["Группа"] == "ПИ101", "Личный номер студента"].unique()

SC = maindata['Уровень контроля'].unique()
date = maindata['Год'].unique()

print('В исходном датасете содержалось', CEst, 'оценок, из них', CEst1, 'оценок относятся к группе ПИ101.')
print("В датасете находятся оценки студентов ПИ101 с следующими личными номерами:", U)
print("Используемые формы контроля:" , SC)
print("Данные представлены по следующим учебным годам:", date)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())