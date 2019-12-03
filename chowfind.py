import discord
from discord.ext import commands
import sys
import re
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import aiohttp
import requests

class Chowfind(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Chowfind(self, ctx, *, userinput):
        print(userinput)
        searchlist = []
        async with aiohttp.ClientSession() as session:
            url = 'https://chowdown.io/search'
            line = " "
            userinput = {'q': line + userinput}
            link = session.get(url, params=userinput)
            vid = await link
            finder = re.findall(r'(https?://[^)\s]+)', str(vid))
            vidlist.append(search)
            for x in range(len(vidlist)):
                finv = ''.join(finder)
            print(finv)
            data = requests.get(finv)
            em = discord.Embed(title="Search Results", description="I found some recipes!!!")
            em.colour = 0xFFFA
            em.add_field(name="Link to site", value=str(search))
            await ctx.send(embed=em)

            soup = BeautifulSoup(data.text, 'html.parser')
            print(soup)

def setup(bot):
    bot.add_cog(Chowfind(bot))
