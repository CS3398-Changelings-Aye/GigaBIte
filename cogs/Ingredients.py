import discord
from discord.ext import commands
import sys
import re

class Ingredients(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Cook(self, ctx, userInput):

        # if userInput == "Me" or userInput == "me":
        #     hi = "Okay bby cakes"
        #     await ctx.send(hi)

        with open(r"IGDBOut.txt", "r") as f:
            for line in f:
                if (userInput.upper() or userInput.lower()) in line:
                    await ctx.send(re.sub("\s\s+", " ", "* " + line.lower().title().strip()))
                    # print(re.sub("\s\s+", " ", "* " + line.lower().title().strip()))

def setup(bot):
    bot.add_cog(Ingredients(bot))