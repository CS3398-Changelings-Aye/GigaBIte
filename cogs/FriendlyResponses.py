import discord
from discord.ext import commands

class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def hello(self, ctx):
        await ctx.send ("Hello! What are we cooking today?")

    async def thankyou(self, ctx):
        await ctx.send("Of course! My pleasure")

    async def question(self, ctx):
        await ctx.send("If you have a question for me, please type '!info' and I'll share what you can ask!")

def setup(bot):
    bot.add_cog(Information(bot))
