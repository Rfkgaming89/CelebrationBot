import discord
from discord.ext import commands, tasks
from discord import app_commands
from datetime import datetime, timedelta
import sqlite3
import configparser
import random

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['DISCORD']['TOKEN']
GUILD_ID = config['DISCORD']['GUILD_ID']
BIRTHDAY_CHANNEL_ID = config['DISCORD']['BIRTHDAY_CHANNEL_ID']
BIRTHDAY_ROLE = 'Birthday'  # The name of the birthday role

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Database setup
conn = sqlite3.connect('birthdays.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS birthdays (id INTEGER PRIMARY KEY, user_id TEXT, birthday DATE)''')
conn.commit()

birthday_messages = [
    "Happy Birthday, {user}!",
    "🎉🎂 Happy Birthday, {user}! 🎂🎉",
    "Wishing you a fantastic birthday, {user}!",
    "It's your special day, {user}! Happy Birthday!",
    "Cheers to you on your birthday, {user}!"
]

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    guild = discord.Object(id=GUILD_ID)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)
    check_birthdays.start()
    send_birthday_wishes.start()

@tasks.loop(hours=24)
async def check_birthdays():
    await bot.wait_until_ready()
    today = datetime.utcnow().date()
    guild = bot.get_guild(int(GUILD_ID))
    birthday_role = discord.utils.get(guild.roles, name=BIRTHDAY_ROLE)

    if not birthday_role:
        print("Birthday role not found")
        return

    # Remove the birthday role from all members
    for member in guild.members:
        if birthday_role in member.roles:
            try:
                await member.remove_roles(birthday_role)
            except discord.Forbidden:
                print(f"Failed to remove role from {member.display_name}, missing permissions.")
            except Exception as e:
                print(f"Unexpected error when removing role from {member.display_name}: {e}")

    # Add the birthday role to members with today's birthday
    c.execute("SELECT user_id FROM birthdays WHERE strftime('%m-%d', birthday) = ?", (today.strftime('%m-%d'),))
    results = c.fetchall()
    for user_id in results:
        member = guild.get_member(int(user_id[0]))
        if member:
            try:
                await member.add_roles(birthday_role)
            except discord.Forbidden:
                print(f"Failed to add role to {member.display_name}, missing permissions.")
            except Exception as e:
                print(f"Unexpected error when adding role to {member.display_name}: {e}")

@tasks.loop(hours=24)
async def send_birthday_wishes():
    await bot.wait_until_ready()
    today = datetime.utcnow().date()
    guild = bot.get_guild(int(GUILD_ID))
    channel = guild.get_channel(int(BIRTHDAY_CHANNEL_ID))

    c.execute("SELECT user_id FROM birthdays WHERE strftime('%m-%d', birthday) = ?", (today.strftime('%m-%d'),))
    results = c.fetchall()
    for user_id in results:
        member = guild.get_member(int(user_id[0]))
        if member:
            message = random.choice(birthday_messages).format(user=member.mention)
            try:
                await channel.send(message)
            except Exception as e:
                print(f"Unexpected error when sending birthday message to {member.display_name}: {e}")

@bot.tree.command(name='add_birthday', description="Add a birthday in Month Day Year format")
@app_commands.describe(user='The user to add a birthday for', date='The birthday in Month Day Year format')
async def add_birthday(interaction: discord.Interaction, user: discord.User, date: str):
    """Add a birthday for a user in Month Day Year format"""
    try:
        birthday = datetime.strptime(date, '%B %d %Y').date()  # Parsing 'Month Day Year'
        c.execute("INSERT OR REPLACE INTO birthdays (user_id, birthday) VALUES (?, ?)", (str(user.id), birthday))
        conn.commit()
        await interaction.response.send_message(f'Birthday for {user.mention} added: {birthday.strftime("%B %d %Y")}', ephemeral=True)
    except ValueError:
        await interaction.response.send_message('Invalid date format. Please use "Month Day Year".', ephemeral=True)

if not TOKEN:
    print("Error: DISCORD_BOT_TOKEN environment variable not set.")
else:
    bot.run(TOKEN)
