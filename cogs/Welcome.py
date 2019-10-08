import discord
from discord.ext import commands
import json
from collections import OrderedDict


class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Welcome(self, ctx):
        em = discord.Embed()
        with open('JSONS/Welcome.json', encoding='utf-8'):
            Welcome_message = json.load(open('JSONS/Welcome.json', encoding='utf-8'))
            em.colour = 0xf9f9f9
            em.description = ''.join(Welcome_message['Description'])
            em.title = ''.join(Welcome_message["Title"])
            msg = await ctx.send(embed=em)

        msg = ctx.message
        await msg.delete()

def setup(bot):
    bot.add_cog(Welcome(bot))