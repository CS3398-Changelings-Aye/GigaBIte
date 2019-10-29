import discord
from discord.ext import commands
import sys
import re
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import aiohttp
import requests

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Image(self, ctx, *, userinput):
        print(userinput)
        searchlist = []
        async with aiohttp.ClientSession() as session:
            url = 'https://www.heb.com/search/?'
            line = " "
            userinput = {'q': line + userinput}
            link = session.get(url, params=userinput)
            x = await link
            search = re.findall(r'(https?://[^)\s]+)', str(x))
            searchlist.append(search)
            for x in range(len(searchlist)):
                y = ''.join(search)
            print(y)
            data = requests.get(y)
            em = discord.Embed(title="Search Results", description="Here is your results")
            em.colour = 0xFFFA
            em.add_field(name="Link to site", value=str(search))
            await ctx.send(embed=em)

            soup = BeautifulSoup(data.text, 'html.parser')
            print(soup)

def setup(bot):
    bot.add_cog(Images(bot))