# -*- coding: utf-8 -*-
import aiogram, re, traceback, random, json, datetime, aiohttp, aiofiles, flag
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from time import sleep
from datetime import datetime, timedelta
import random
from random import randint
from bs4 import BeautifulSoup
from multiprocessing import Process
import requests
from requests import get
import threading
import asyncio
import os
import string
from threading import Thread
import re
from contextlib import suppress
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)
import time
from aiogram.types import Message, InputFile
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import io
from pyqiwip2p import QiwiP2P
from random import choice
from pycoingecko import CoinGeckoAPI
# Local imports
from configurator.config import *
from filters import IsPrivate
from keyboard import menu, admin
from data.csdb import *
from states.main_states import *

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

profites = ['17000', '2000', '500', '900', '9000', '18000', '0', '100', '4000', '11000', '1000', '15000', '5100', '0', '16000', '12000', '13000', '19000', '50', '0', '20000', '3500', '6700']


prof = ['1700', '400', '15899', '4300', '5400', '1290', '17999', '50', '23000', '1000', '20000', '1300', '6100', '100']

error = ['❌ Стремная ссылка, мамонт слился', '❌ Мамонт оказался воркером по 1.0', '❌ Нет денег на карте', '❌ 900', '❌ Фантом уснул и проебал твой лог']


@dp.message_handler(IsPrivate(), commands=['start'])
async def start_command(message: types.Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    a = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
    if user is None:
        await register_user(message.from_user.id, message.from_user.username)
    await message.answer(f"<b><i>Добро пожаловать в лучшую игру в скам сфере.</i></b>\n<b><i>Скамь мамонтов, занимай место в топе и будь лучшим!</i></b>\n\n<b><i>Разработчик: @liceyeah</i></b>", reply_markup = await menu.main_menus(message.from_user.id))

@dp.message_handler(commands=['admin'])
async def admin_command(message: types.Message):
	if message.from_user.id == 5374895788:
		await message.answer(f"<b>👋🏻 Добро пожаловать!</b>", reply_markup = await menu.admin_menu())



@dp.message_handler(lambda message: message.text == '👤 Профиль')
async def process_callback_button1(message: types.Message):
    profile = await get_user(message.from_user.id)
    await message.answer(f"<b><i>👤 Профиль скамера {message.from_user.mention} ({profile[2]}⚡️)</i></b>\n\n<b><i>💰 Текущий баланс: {profile[5]}</i></b>\n<b><i>💵 Cумма профитов: {profile[6]}</i></b>\n<b><i>📊 Успешных профитов: {profile[7]}</i></b>")

@dp.message_handler(lambda message: message.text == '🔙 В Главное меню')
async def working_mess(message: types.Message):
	await message.answer(f"<b><i>Добро пожаловать в лучшую игру в скам сфере.</i></b>\n<b><i>Скамь мамонтов, занимай место в топе и будь лучшим!</i></b>\n\n<b><i>Разработчик: @liceyeah</i></b>", reply_markup = await menu.main_menus(message.from_user.id))

@dp.message_handler(lambda message: message.text == '💼 Ворк')
async def working_mess(message: types.Message):
	profile = await get_user(message.from_user.id)
	if profile[3] == 1:
		await message.answer(f"<b><i>Вы уже заняты другим мамонтом</i></b>")
	else:
		await add_cooldown_check(message.from_user.id)
		energy = profile[2]
		oll_profit = profile[7]
		if profile[2] == 0:
			await message.answer(f"<b><i>У вас недостаточно енергии</i></b>")
			await dell_cooldown_check(message.from_user.id)
		else:	
			balanses = profile[5]
			messageFirst = await message.answer(f"<b><i>⏳ Ищу мамонта</i></b>")
			await asyncio.sleep(2)
			m = await messageFirst.edit_text(text='<b><i>⏳ Ищу мамонта.</i></b>')
			await asyncio.sleep(2)
			s = await m.edit_text(text='<b><i>⏳ Ищу мамонта...</i></b>')
			await asyncio.sleep(2)
			k = await s.edit_text(text='<b><i>⏳ Кидаю ссылку на оплату.</i></b>')
			await asyncio.sleep(2)
			a = await k.edit_text(text='<b><i>⏳ Кидаю ссылку на оплату..</i></b>')
			await asyncio.sleep(2)
			z = await a.edit_text(text='<b><i>⏳ Получаю результат.</i></b>')
			await asyncio.sleep(2)
			x = await z.edit_text(text='<b><i>⏳ Получаю результат..</i></b>')
			await asyncio.sleep(2)
			r = await x.edit_text(text='<b><i>⏳ Получаю результат...</i></b>')
			await asyncio.sleep(2)
			proff = int(random.choice(profites))
			if proff == 0:
				await update_energy(energy, message.from_user.id)
				err = random.choice(error)
				profiles = await get_user(message.from_user.id)
				await s.edit_text(text=f'<b><i>{err}</i></b>\n\n<b><i>Осталось  {profiles[2]}⚡️ (ед. энергии)</i></b>')
				await dell_cooldown_check(message.from_user.id)
			else:
				await update_energy(energy, message.from_user.id)
				summa = int(proff)
				balanse = int(balanses) + int(summa)
				balanse = str(balanse)
				await add_balanse(balanse, message.from_user.id)
				await add_oll_balanse(balanse, message.from_user.id)
				profiles = await get_user(message.from_user.id)
				await s.edit_text(text=f'<b><i>🤑 Успешная оплата!</i></b>\n<b><i>💰 Сумма оплаты - {proff}</i></b>\n<b><i>Твоя доля - {proff} (100%)</i></b>\n\n<b><i>Осталось  {profiles[2]}⚡️ (ед. энергии)</i></b>')
				await dell_cooldown_check(message.from_user.id)
				await update_profits(oll_profit, message.from_user.id)

@dp.callback_query_handler(lambda c: c.data == 'buy_energy1')
async def callback_func(callback_query: types.CallbackQuery):
	profile = await get_user(callback_query.from_user.id)
	if profile[2] == 10 or profile[2] > 10:
		await bot.answer_callback_query(callback_query.id, text=f'❗️ Твоя енергия и так на максимальном уровне {profile[2]}⚡️', show_alert=True)
	else:
		if profile[5] < 5000:
			await bot.answer_callback_query(callback_query.id, text=f'❗️ У вас недостаточно денег, баланс - {profile[5]}₽', show_alert=True)
		else:			
			profile = await get_user(callback_query.from_user.id)
			stoimost = 5000
			energybuy = 1
			balanses = profile[5]
			energy = profile[2]
			balanse = int(balanses)
			await buy_energ(balanse, stoimost, energy, energybuy, callback_query.from_user.id)
			profiles = await get_user(callback_query.from_user.id)
			await bot.answer_callback_query(callback_query.id, text=f'Отличный энергетик, енергия пополнена и составляет {profiles[2]}⚡️\n\nДенег осталось - {profiles[5]}₽', show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'buy_energy2')
async def callback_func(callback_query: types.CallbackQuery):
	profile = await get_user(callback_query.from_user.id)
	if profile[2] > 8:
		await bot.answer_callback_query(callback_query.id, text=f'❗️ Твоя енергия и так на максимальном уровне {profile[2]}⚡️', show_alert=True)
	else:
		if profile[5] < 10000:
			await bot.answer_callback_query(callback_query.id, text=f'❗️ У вас недостаточно денег, баланс - {profile[5]}₽', show_alert=True)
		else:
			profile = await get_user(callback_query.from_user.id)
			stoimost = 10000
			energybuy = 2
			balanses = profile[5]
			energy = profile[2]
			balanse = int(balanses)
			await buy_energ(balanse, stoimost, energy, energybuy, callback_query.from_user.id)
			profiles = await get_user(callback_query.from_user.id)
			await bot.answer_callback_query(callback_query.id, text=f'Отличный энергетик, енергия пополнена и составляет {profiles[2]}⚡️\n\nДенег осталось - {profiles[5]}₽', show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'buy_energy3')
async def callback_func(callback_query: types.CallbackQuery):
	profile = await get_user(callback_query.from_user.id)
	if profile[2] > 5:
		await bot.answer_callback_query(callback_query.id, text=f'❗️ Твоя енергия и так на максимальном уровне {profile[2]}⚡️', show_alert=True)
	else:
		if profile[5] < 25000:
			await bot.answer_callback_query(callback_query.id, text=f'❗️ У вас недостаточно денег, баланс - {profile[5]}₽', show_alert=True)
		else:
			profile = await get_user(callback_query.from_user.id)
			stoimost = 25000
			energybuy = 5
			balanses = profile[5]
			energy = profile[2]
			balanse = int(balanses)
			await buy_energ(balanse, stoimost, energy, energybuy, callback_query.from_user.id)
			profiles = await get_user(callback_query.from_user.id)
			await bot.answer_callback_query(callback_query.id, text=f'Вкусно покушал,, енергия пополнена и составляет {profiles[2]}⚡️\n\nДенег осталось - {profiles[5]}₽', show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'buy_energy4')
async def callback_func(callback_query: types.CallbackQuery):
	profile = await get_user(callback_query.from_user.id)
	if profile[2] > 1:
		await bot.answer_callback_query(callback_query.id, text=f'❗️ Твоя енергия и так на максимальном уровне {profile[2]}⚡️', show_alert=True)
	else:
		if profile[5] < 50000:
			await bot.answer_callback_query(callback_query.id, text=f'❗️ У вас недостаточно денег, баланс - {profile[5]}₽', show_alert=True)
		else:
			profile = await get_user(callback_query.from_user.id)
			stoimost = 50000
			energybuy = 10
			balanses = profile[5]
			energy = profile[2]
			balanse = int(balanses)
			await buy_energ(balanse, stoimost, energy, energybuy, callback_query.from_user.id)
			profiles = await get_user(callback_query.from_user.id)
			await bot.answer_callback_query(callback_query.id, text=f'Вкусно покушал, енергия пополнена и составляет {profiles[2]}⚡️\n\nДенег осталось - {profiles[5]}₽', show_alert=True)


@dp.message_handler(lambda message: message.text == '🛒 Магазин')
async def working_mess(message: types.Message):
	await message.answer(f"<b><i>🛒 С помощью товаров из магазина ты cможешь дольше работать и получать больше профитов</i></b>", reply_markup = await menu.store())

@dp.message_handler(lambda message: message.text == '🔋 Энергетик 0.25л')
async def working_mess(message: types.Message):
	await message.answer(f"<b><i>🔋 Энергетик 0.25л</i></b>\n\n<b><i>Цена: 5000₽</i></b>\n<b><i>Описание: Заряжает энергией и дает 1⚡️</i></b>", reply_markup = await menu.buy_energy())

@dp.message_handler(lambda message: message.text == '🔋 Энергетик 0.5л')
async def working_mess(message: types.Message):
	await message.answer(f"<b><i>🔋 Энергетик 0.5л</i></b>\n\n<b><i>Цена: 10000₽</i></b>\n<b><i>Описание: Заряжает энергией и дает 2⚡️</i></b>", reply_markup = await menu.buy_energy2())

@dp.message_handler(lambda message: message.text == '🍕 Пицца 25см')
async def working_mess(message: types.Message):
	await message.answer(f"<b><i>🍕 Пицца 25см</i></b>\n\n<b><i>Цена: 25000₽</i></b>\n<b><i>Описание: Восстанавливает силы и дает 5⚡️</i></b>", reply_markup = await menu.buy_energy3())

@dp.message_handler(lambda message: message.text == '🍕 Пицца 50см')
async def working_mess(message: types.Message):
	await message.answer(f"<b><i>🍕 Пицца 50см</i></b>\n\n<b><i>Цена: 50000₽</i></b>\n<b><i>Описание: Восстанавливает силы и дает 10⚡️</i></b>", reply_markup = await menu.buy_energy4())


@dp.message_handler(commands=['scm'])
async def echo_message(message: types.Message):
	proff = random.choice(prof)
	await bot.send_message(message.from_user.id, f'<b><i>🤑 Успешная оплата!</i></b>\n<b><i>💰 Сумма оплаты - {proff}</i></b>\n<b><i>Твоя доля - {proff} (100%)</i></b>')










# ADMN

@dp.callback_query_handler(text="stats", state="*")
async def bot_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    users = await get_all_users()
    await bot.send_message(call.message.chat.id, f"📈 <b>Статистика бота:</b>\n\n<b>Всего пользователей:</b> <code>{len(users)}</code>")

@dp.callback_query_handler(lambda c: c.data == "mass_send", state="*")
async def mass_send(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.answer_callback_query(callback_query.id)
    await SendText.text.set()
    await callback_query.message.edit_text(text="<b>Введите текст рассылки:</b>")


@dp.message_handler(IsPrivate(), state=SendText.text)
async def accept_text(message: types.Message, state: FSMContext):
    users = await get_all_users()
    count = 0
    count_no = 0
    for user in users:
        try:
            await bot.send_message(user[0], message.text)
            count += 1
        except:
            count_no += 1
    await message.answer(f"<b>Рассылка закончена.\nДошло:</b> <code>{count}</code>\n<b>Не получили:</b> <code>{count_no}</code>")
    await state.finish()







async def on_startup(dp):
    await create_tables()



if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)