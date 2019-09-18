import discord
from discord.ext import commands
import json


bot = commands.Bot(command_prefix="!")
def load_creds():
    with open('credentials.json') as f:
        return json.load(f)

creds = load_creds()
token = creds['token']


bot.run(token)