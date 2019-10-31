import discord
from discord.ext import commands
import sys
import re
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import aiohttp
import requests

class Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Youtube(self, ctx, *, userinput):
        print(userinput)
        searchlist = []
        async with aiohttp.ClientSession() as session:
            url = 'https://www.youtube.com/search/?'
            line = " "
            userinput = {'q': line + userinput}
            link = session.get(url, params=userinput)
            vid = await link
            search = re.findall(r'(https?://[^)\s]+)', str(vid))
            searchlist.append(search)
            for x in range(len(searchlist)):
                finv = ''.join(search)
            print(finv)
            data = requests.get(finv)
            em = discord.Embed(title="Search Results", description="I found what you're looking for!")
            em.colour = 0xFFFA
            em.add_field(name="Link to site", value=str(search))
            await ctx.send(embed=em)

            soup = BeautifulSoup(data.text, 'html.parser')

def setup(bot):
    bot.add_cog(Youtube(bot))