import discord
from discord.ext import commands
from discord.channel import TextChannel
import json
import os


def load_creds():
    with open('credentials.json') as f:
        return json.load(f)


bot = commands.Bot(command_prefix="!")

creds = load_creds()
token = creds['token']
all_extensions = []
id = bot.get_guild(623651335316963339)

@bot.event
async def on_ready():
    print('Welcome to Gigabite: ' + str(bot.user.name) + '\n')
    print('Id: ' + str(bot.user.id))
    print('Guilds: ', str(len(bot.guilds)))
    print('Users: ', str(len(set(bot.get_all_members()))))

@bot.command(pass_context=True, aliases=["Clear"])
@commands.has_permissions(administrator=True)
async def clear(ctx, number: int):
    deleted = await TextChannel.purge(ctx.message.channel, limit=number)
    msg = 'Deleted {} Messages'.format(len(deleted))
    await ctx.send(msg, delete_after=10)

for file in os.listdir('cogs'):
    name = file[:-3]
    print(name)
    try:
        if file.endswith('.py'):
            bot.load_extension("cogs.{}".format(name))
            all_extensions.append(name)
            print("Loaded Cogs: " + name)
    except Exception as e:
        print("Cogs that failed to load {}\n{}: {}".format(name, type(e).__name__, e))

bot.run(token)
