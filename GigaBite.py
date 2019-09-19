import discord
from discord.ext import commands
import json


def load_creds():
    with open('credentials.json') as f:
        return json.load(f)


bot = commands.Bot(command_prefix="!")

creds = load_creds()
token = creds['token']
id = bot.get_guild(623651335316963339)

@bot.event
async def on_ready():
    print('Welcome to Gigabite: ' + str(bot.user.name) + '\n')
    print('Id: ' + str(bot.user.id))
    print('Guilds: ', str(len(bot.guilds)))
    print('Users: ', str(len(set(bot.get_all_members()))))

@bot.command(pas_context=True)
async def ping(ctx):
    await ctx.send("Pong")


bot.run(token)
