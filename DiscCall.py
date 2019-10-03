import discord
from discord.ext import commands
import sys
import re

class tagsomeone(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!Look'):
            await client.send_message(message.channel, "check out this recipe {0.author.mention}".format(message))

        if message.content.startswith('hello'):
            msg = 'Hello there {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!Listen'):
            user = discord.utils.get(message.server.members, name = 'ZERO', discriminator = 6885)
            await client.send_message(message.channel, user.mention + 'LISTEN!')
