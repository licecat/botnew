from aiogram.dispatcher.filters.state import State, StatesGroup

class CardEnter1Usd(StatesGroup):
	card = State()

class GettingBase(StatesGroup):
    base = State()
    bin = State()

class CardEnter1Usd2(StatesGroup):
	card = State()

class Card5usd(StatesGroup):
	card = State()

class CardFormatt(StatesGroup):
	formatt = State()

class CardEnter10usd(StatesGroup):
	card = State()

class Card(StatesGroup):
	charge = State()

class BankerReceipt(StatesGroup):
	receipt = State()

class AntipublicChecker(StatesGroup):
	cards = State()

class AddProxies(StatesGroup):
	proxies = State()

class DelProxies(StatesGroup):
	proxies = State()

# ---- ADMIN STATES ---- #

class AdminGvSub(StatesGroup):
	user_data = State()

class Adminseuser(StatesGroup):
	se_user = State()

class AdminTkSub(StatesGroup):
	user_data = State()

class MakeAdmin(StatesGroup):
	user_data = State()

class KillAdmin(StatesGroup):
	user_data = State()

class SendText(StatesGroup):
	text = State()

class AntipublicCards(StatesGroup):
	cards = State()
