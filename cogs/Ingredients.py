import discord
from discord.ext import commands
import sys
import re

class Ingredients(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Cook(self, ctx, userInput):
        em = discord.Embed(title="Types of Ingredients", description="Heres a list of Ingredients that includes " + str(userInput))
        em.set_author(name=self.bot.user.name)
        em.colour = 0xFF0000
        dic = {}
        my_list = []
        with open(r"IGDBOut.txt", "r") as f:
            for line in f:
                if (userInput in line):
                    print(line)
                    em.add_field(name="Ingredient", value=line)
                    # await ctx.send(re.sub("\s\s+", " ", "* " + line.lower().title().strip()))
            await ctx.send(embed=em)
def setup(bot):
    bot.add_cog(Ingredients(bot))