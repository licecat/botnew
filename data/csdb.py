import random
import datetime
import aiosqlite


path = "data/database_file/sacmbot.sqlite"

async def register_user(user_id, user_name):
	async with aiosqlite.connect(path) as db:

		await db.execute("INSERT INTO users "
                         "(user_id, user_name, energi, cooldown_check, team, balanse, oll_bal, profit) "
                         "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                         [user_id, user_name, 10, 0, 0, 0, 0, 0])

		await db.commit()

async def get_user(user_id):
	async with aiosqlite.connect(path) as db:

		profile = await db.execute(f"SELECT * FROM users WHERE user_id = ?", (user_id,))

		return await profile.fetchone()


async def get_all_users():
	async with aiosqlite.connect(path) as db:
		users = await db.execute("SELECT * FROM users")
		return await users.fetchall()

async def buy_energ(balanse, stoimost, star_energy, energybuy, user_id):
	async with aiosqlite.connect(path) as db:
		try:
			user = await db.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
			user = await user.fetchone()
			buy = int(balanse) - int(stoimost)
			energy = int(star_energy) + int(energybuy)
			await db.execute(f"UPDATE users SET balanse = {buy} WHERE user_id = '{user_id}'")
			await db.execute(f"UPDATE users SET energi = {energy} WHERE user_id = '{user_id}'")
			await db.commit()
		except Exception as e:
			print(e)




async def update_profits(oll_profit, user_id):
	async with aiosqlite.connect(path) as db:
		try:
			user = await db.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
			user = await user.fetchone()
			pr = int(oll_profit) + int(1)
			await db.execute(f"UPDATE users SET profit = {pr} WHERE user_id = '{user_id}'")
			await db.commit()
		except Exception as e:
			print(e)



async def add_oll_balanse(summa, user_id):
	async with aiosqlite.connect(path) as db:
		try:
			user = await db.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
			user = await user.fetchone()
			await db.execute(f"UPDATE users SET oll_bal = '{summa}' WHERE user_id = '{user_id}'")
			await db.commit()
		except Exception as e:
			print(e)


async def add_cooldown_check(user_id):
	async with aiosqlite.connect(path) as db:
		await db.execute(f"UPDATE users SET cooldown_check = '{1}' WHERE user_id = '{user_id}'")
		await db.commit()

async def dell_cooldown_check(user_id):
	async with aiosqlite.connect(path) as db:
		await db.execute(f"UPDATE users SET cooldown_check = '{0}' WHERE user_id = '{user_id}'")
		await db.commit()

async def add_balanse(summa, user_id):
	async with aiosqlite.connect(path) as db:
		try:
			user = await db.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
			user = await user.fetchone()
			await db.execute(f"UPDATE users SET balanse = '{summa}' WHERE user_id = '{user_id}'")
			await db.commit()
		except Exception as e:
			print(e)

async def update_energy(star_energy, user_id):
	async with aiosqlite.connect(path) as db:
		try:
			user = await db.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
			user = await user.fetchone()
			energy = int(star_energy) - int(1)
			await db.execute(f"UPDATE users SET energi = {energy} WHERE user_id = '{user_id}'")
			await db.commit()
		except Exception as e:
			print(e)

async def create_tables():
	async with aiosqlite.connect(path) as db:
		await db.execute("CREATE TABLE IF NOT EXISTS users("
						"user_id TEXT, user_name TEXT, energi INTEGER, "
						"cooldown_check INTEGER, team TEXT, balanse INTEGER, oll_bal INTEGER, profit INTEGER)")

		await db.commit()

