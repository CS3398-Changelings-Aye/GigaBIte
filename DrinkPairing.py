import discord
from discord.ext import commands

class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def drinks(self, ctx):
        em = discord.Embed(title="Drink Pairing", description="Here are a few recommendations for drinks to pair with your meals.")
        em.set_author(name=str(self.bot.user.name))
        em.colour = 0x000000
        em.add_field(name="Red Meat", value="Beers such as porters and stouts, red wine, whiskey, unsweetened iced tea.")
        em.add_field(name= "White Meat", value="Pale Ales, Sake, full bodied red wine, full bodied white wine, gin and tonic, sparkling white grape juice.")
        em.add_field(name= "Seafood",  value="Citrus Margaritas, Bloody Mary, Bourbon, lemonade, ginger ale, Shirley Temple.")
        em.add_field(name= "Pasta",  value="For red sauces, classic red wine, dry wines, flavored sparkling water. For white sauces, IPA beer, Chardonay, sweet wines, citrus flavored sparkling water.")
        em.add_field(name= "Vegetables",  value=" Merlot, Chardonay, dry wines, grape juice, sparking water.")
        await ctx.send(embed=em)
        //from the simple database

def setup(bot):
    bot.add_cog(Information(bot))
