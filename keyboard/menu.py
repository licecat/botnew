from aiogram.types import ReplyKeyboardRemove, \
	ReplyKeyboardMarkup, KeyboardButton, \
	InlineKeyboardMarkup, InlineKeyboardButton
from configurator.config import admin as config

from data.csdb import *

async def main_menus(user_id):
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	working = KeyboardButton("💼 Ворк")
	store = KeyboardButton("🛒 Магазин")
	profile_bot = KeyboardButton("👤 Профиль")

	keyboard.add(working, profile_bot, store)

	return keyboard



async def buy_energy():
	keyboard = InlineKeyboardMarkup()
	back_btn = InlineKeyboardButton(text = "🛒 Купить", callback_data = "buy_energy1")

	keyboard.add(back_btn)

	return keyboard

async def buy_energy2():
	keyboard = InlineKeyboardMarkup()
	back_btn = InlineKeyboardButton(text = "🛒 Купить", callback_data = "buy_energy2")

	keyboard.add(back_btn)

	return keyboard

async def buy_energy3():
	keyboard = InlineKeyboardMarkup()
	back_btn = InlineKeyboardButton(text = "🛒 Купить", callback_data = "buy_energy3")

	keyboard.add(back_btn)

	return keyboard

async def buy_energy4():
	keyboard = InlineKeyboardMarkup()
	back_btn = InlineKeyboardButton(text = "🛒 Купить", callback_data = "buy_energy4")

	keyboard.add(back_btn)

	return keyboard

async def store():
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	energy025 = KeyboardButton("🔋 Энергетик 0.25л")
	energy050 = KeyboardButton("🔋 Энергетик 0.5л")
	pizza25 = KeyboardButton("🍕 Пицца 25см")
	pizza50 = KeyboardButton("🍕 Пицца 50см")
	backmenu = KeyboardButton("🔙 В Главное меню")

	keyboard.add(energy025, energy050, pizza25, pizza50, backmenu)

	return keyboard














async def admin_menu():
	keyboard = InlineKeyboardMarkup(row_width = 2)
	mass_send_btn = InlineKeyboardButton(text = "🪄 Рассылка", callback_data = "mass_send")
	stats_btn = InlineKeyboardButton(text = "📊 Статистика", callback_data = "stats")
	keyboard.add(mass_send_btn, stats_btn)
	return keyboard