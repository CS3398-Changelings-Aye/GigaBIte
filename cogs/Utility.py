import discord
from discord.ext import commands

class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def info(self, ctx):
        em = discord.Embed(title="Chef G Information!", description="How may I help you today? PLease spell out the number for your question.")
        em.set_author(name=str(self.bot.user.name))
        em.colour = 0x000000
        em.add_field(name="One", value="My name is Chef G and I am here to help you find recipes with the ingredients you have!")
        em.add_field(name= "Two", value="Simply send me the name of an ingredient that you have! I'll take care of the rest.")
        em.add_field(name= "Three",  value="I'll send you a few recipes that I find with the ingredient you listed.")
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Information(bot))