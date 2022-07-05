from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from configurator.config import *

from data.csdb import *


async def admin_menu():
	keyboard = InlineKeyboardMarkup(row_width = 2)
	mass_send_btn = InlineKeyboardButton(text = "🪄 Рассылка", callback_data = "mass_send")
	stats_btn = InlineKeyboardButton(text = "📊 Статистика", callback_data = "stats")
	back_btn = InlineKeyboardButton(text = "⬅️ Обычное меню", callback_data = "back")
	keyboard.add(mass_send_btn, stats_btn)
	keyboard.add(back_btn)
	return keyboard


async def return_menu():
	keyboard = InlineKeyboardMarkup()
	back_btn = InlineKeyboardButton(text = "⬅️ В главное меню", callback_data = "back_admin")

	keyboard.add(back_btn)

	return keyboard


