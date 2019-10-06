import discord
from discord.ext import commands
import sys
import re

class tagsomeone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        if message.content.startswith('Look'):
            await channel.send("check out this recipe {0.author.mention}".format(message))

        if message.content.startswith('hello'):
            msg = 'Hello there {0.author.mention}'.format(message)
            await channel.send(msg)

def setup(bot):
    bot.add_cog(tagsomeone(bot))