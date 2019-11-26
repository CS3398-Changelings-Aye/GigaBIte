from distutils import config
import discord
from discord.ext import commands
import youtube_dl
from urllib import request
import re


players = {}

class music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context = True)
    async def connect(ctx):
        channel = ctx.message.author.voice.voice_channnel
        await discord.client.join_voice_channel(channel)

    @bot.command(pass_context=True)
    async def disconnnect(ctx):
        server = ctx.message.server
        voice_client = discord.client.voice_client_in(server)
        await voice_client.disconnect()

    @bot.command(pass_context=True)
    async def play(ctx, url):
        server = ctx.message.server
        voice_client = discord.client.voice_client_in(server)
        player = await voice_client.create_ydl_player(url)
        players[server.id] = player
        player.start()
'''
    @commands.command()
    async def lofi(self, ctx, *, userinput):
        print(userinput)


        await ctx.send("finding lofi...")


'''

def setup(bot):
    bot.add_cog(music(bot))
