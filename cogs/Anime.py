import discord
from discord.ext import commands
import json
from collections import OrderedDict
import re
import aiohttp
from bs4 import BeautifulSoup
import random

# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

class AnimeNights(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Shows = json.load(open('JSONS/Shows.json'), object_pairs_hook=OrderedDict, encoding='UTF-8')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user, msg):
        if str(reaction.emoji) == '\U0001F449':
            await msg.add_reaction('\u25C0')

    def addToDB(self, name, AnimeLink):
        with open("JSONS/Shows.json", 'r') as f:
            shows = json.load(f)
        Anime = name
        # print(Anime)
        if Anime not in shows:
            shows[Anime] = {}
            shows[Anime]['Anime'] = name
            shows[Anime]['Link'] = AnimeLink
            with open('JSONS/Shows.json', 'w') as f:
                json.dump(shows, f, indent=3)
            return True
        elif Anime in shows:
            return False


    @commands.command(aliases=["AS"])
    async def addShow(self, ctx, *, input):
        """How to use: a!addShow <Anime Name>
            or a!AS <Anime Name"""
        animelist = []
        async with aiohttp.ClientSession() as session:
            url = 'https://myanimelist.net/search/all'
            params = {'q': input}
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}

            async with session.get(url, params=params, headers=headers) as resp:
                text = await resp.text()
                soup = BeautifulSoup(text, 'html.parser')
                # div = soup.find('div', {'class': 'information di-tc va-t pt4 pl8'})
                a = soup.find('a', {'class': 'hoverinfo_trigger fw-b fl-l'})
                PageLink = a['href']

                async with session.get(PageLink, headers=headers) as resp2:
                    text = await resp2.text()
                    soup = BeautifulSoup(text, 'html.parser')
                    ShowName = soup.find('span', itemprop='name').text
                    ShowImage = soup.find('img', itemprop='image')
                    ShowImageLink = ShowImage['src']
                    ShowRating = soup.find('span', itemprop='ratingValue').text
                    UserCount = soup.find('span', itemprop='ratingCount').text
                    # ShowImage['src'] for link to image
        success = self.addToDB(ShowName, PageLink)
        if success:
            em = discord.Embed(title="Search Results, ^ Click above to direct you to MAL",
                               description="Show: " + str(ShowName) + " Added to Database")
            em.colour = 0xFFFA
            em.set_image(url=ShowImageLink)
            em.set_author(name=ShowName, url=PageLink, icon_url=ShowImageLink)
            # em.set_thumbnail(url=img_link)
            em.add_field(name="Rating by " + UserCount + " Users\n\n", value=ShowRating)
            await ctx.send(embed=em)
        elif not success:
            await ctx.send("Show is already in the database.")


    @commands.command()
    async def shows(self, ctx):
        """How to use: a!shows"""
        e = discord.Embed(title="List of Shows", description="Displaying show database")
        with open("JSONS/Shows.json", 'r') as f:
            Ashows = json.load(f)
        for show in Ashows:
            e.add_field(name="**Show**\n", value=show)
        e.colour = 0xFFFA
        msg = await ctx.send(embed=e)



def setup(bot):
    bot.add_cog(AnimeNights(bot))

