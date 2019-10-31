import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def Ban(self, ctx, user: discord.Member, reason=''):
        if ctx.author == self.bot:
            await ctx.send("Sorry can't ban myself")

        e = discord.Embed(title="Banned", description='Reason' + str(reason))
        e.add_field(name='User Banned: ', value=str(user.mention))
        e.add_field(name='Banned By: ', value=str(ctx.author.mention))
        e.set_footer(text=str(user) + 'UID: '+ str(user.id))
        await ctx.send(embed=e)
        await user.ban(reason=reason)
        msg = ctx.message
        await msg.delete()

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, user: discord.Member, reason=''):
        if ctx.author == self.bot:
            await ctx.send("Sorry can't ban myself")

        e = discord.Embed(title="Kicked", description='Reason' + str(reason))
        e.add_field(name='User Kicked: ', value=str(user.mention))
        e.add_field(name='Kicked By: ', value=str(ctx.author.mention))
        e.set_footer(text=str(user) + 'UID: ' + str(user.id))
        await ctx.send(embed=e)
        await user.ban(reason=reason)
        msg = ctx.message
        await msg.delete()

def setup(bot):
    bot.add_cog(Moderation(bot))