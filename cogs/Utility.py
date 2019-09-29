import discord
from discord.ext import commands



class Help(commands.Cog):
    """Display a list of commands and their descriptions"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def HelpMe(self, ctx):
        if ctx.author == self.bot:
            await ctx.send("OwO")


def setup(bot):
    bot.add_cog(Help(bot))