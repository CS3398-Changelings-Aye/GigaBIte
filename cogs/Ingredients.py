import discord
from discord.ext import commands
import sys
import re
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import requests


class Ingredients(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Cook(self, ctx, *, userInput):
        print(userInput)
        x = userInput.splitlines()
        em = discord.Embed(title="Types of Recipes", description="Heres a list of Ingredients that includes " + str(userInput))
        em.set_author(name=self.bot.user.name)
        em.colour = 0xFF0000
        dic = {}
        my_list = []
        with open(r"Original Database.txt", "r") as f, open('Recipes-All Recipes.csv', 'r') as r:
            r = csv.reader(r)
            for line1, line2 in zip(f, r):
                # print(line2)
                var = '\n'.join([' '.join(x.split()[:2]) for x in line1.splitlines()])
                # print(var.split()[:1])
                name = line2[0]
                prep = line2[1]
                type = line2[2]
                Time = line2[3]
                Ingredients = line2[4]
                x = '\n'.join([' '.join(n.split()[:1]) for n in Ingredients.splitlines()])
                if userInput in x:
                    print(name)
                    em.add_field(name="__Recipe__\n" + ''.join(name) + "\n__Ingredients__\n" + ''.join(Ingredients), value="⠀", inline=True)
                    # em.add_field(name="__Ingredients__\n\n" + ''.join(Ingredients), value="⠀", inline=True)
                # if (userInput in var):
                #     # print(var)
                #     em.add_field(name="Ingredient", value= var)
                    # await ctx.send(re.sub("\s\s+", " ", "* " + line.lower().title().strip()))
            await ctx.send(embed=em)


        # print(line)
        # if Ingredients in var:
        #     print("OwO" + str(Ingredients))

    @commands.command()
    async def Search(self, ctx, *, userinput):

        print(userinput)
        soup = BeautifulSoup(userinput, 'html.parser')
        with requests.Session() as k:
            url = 'https://www.google.com/search?q='
            userinput = {'q': userinput}
            link = requests.get(url, params=userinput)
        em = discord.Embed(title="Search Results", description="Here is your results")
        em.colour = 0xFFFA
        em.add_field(name="Link to site", value=link.url)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Ingredients(bot))