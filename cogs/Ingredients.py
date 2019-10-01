import discord
from discord.ext import commands
import sys

class Ingredients(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Cook(self, ctx, userInput):
        IGList = []

        with open(r"IGDBOut.txt", "r") as f:
            # IGList = f.read()
            InputSize = len(userInput)
            for line in f:
                # InputSize = len(line)
                line = line.strip()
                if userInput in line:
                    # await ctx.send(line)
                    print(line)

                # if line:
                    #print(line)
                    # print(line[0])
            # print(IGList)

def setup(bot):
    bot.add_cog(Ingredients(bot))