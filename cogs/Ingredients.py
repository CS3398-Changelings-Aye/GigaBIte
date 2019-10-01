import discord
from discord.ext import commands
import sys
import re

class Ingredients(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Cook(self, ctx, userInput):

        with open(r"IGDBOut.txt", "r") as f:
            for line in f:
                if (userInput.upper() or userInput.lower()) in line:
                    await ctx.send(re.sub("\s\s+", " ", "* " + line.lower().title().strip()))
                    # print(re.sub("\s\s+", " ", "* " + line.lower().title().strip()))

def setup(bot):
    bot.add_cog(Ingredients(bot))