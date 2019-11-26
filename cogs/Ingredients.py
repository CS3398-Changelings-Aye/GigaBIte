import discord
from discord.ext import commands
import sys
import re
from bs4 import BeautifulSoup
import csv
import json
import aiohttp
import requests



class Ingredients(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Cook(self, ctx, *, userInput):
        print(userInput)
        x = userInput.splitlines()
        em = discord.Embed(title="Types of Recipes", description="Heres a list of Ingredients that includes " + str(userInput))
        em.set_author(name=self.bot.user.name)
        em.colour = 0xFF0000
        dic = {}
        my_list = []
        with open(r"Original Database.txt", "r") as f, open('Recipes-All Recipes.csv', 'r') as r:
            r = csv.reader(r)
            for line1, line2 in zip(f, r):
                # print(line2)
                var = '\n'.join([' '.join(x.split()[:2]) for x in line1.splitlines()])
                # print(var.split()[:1])
                name = line2[0]
                prep = line2[1]
                type = line2[2]
                Time = line2[3]
                Ingredients = line2[4]
                x = '\n'.join([' '.join(n.split()[:1]) for n in Ingredients.splitlines()])
                if userInput in x:
                    print(name)
                    em.add_field(name="__Recipe__\n" + ''.join(name) + "\n__Ingredients__\n" + ''.join(Ingredients), value="⠀", inline=True)
                    # em.add_field(name="__Ingredients__\n\n" + ''.join(Ingredients), value="⠀", inline=True)
                # if (userInput in var):
                #     # print(var)
                #     em.add_field(name="Ingredient", value= var)
                    # await ctx.send(re.sub("\s\s+", " ", "* " + line.lower().title().strip()))
            await ctx.send(embed=em)


        # print(line)
        # if Ingredients in var:
        #     print("OwO" + str(Ingredients))


    def addToDB(self, name, Ingredients):
        with open("JSONS/Recipes.json", 'r') as f:
            Recipes = json.load(f)
        Recipe = name
        # print(Anime)
        if Recipe not in Recipes:
            Recipes[Recipe] = {}
            Recipes[Recipe]['Recipe'] = name
            Recipes[Recipe]['Ingredients'] = Ingredients
            with open('JSONS/Recipes.json', 'w') as f:
                json.dump(Recipes, f, indent=3)
            return True
        elif Recipe in Recipes:
            return False



    @commands.command()
    async def Search(self, ctx, *, userinput):
        global rec, ing, success
        print(userinput)
        searchlist = []

        async with aiohttp.ClientSession() as session:
            url = 'https://www.google.com/search?'
            question = "What can I make with "
            params = {'q': question + userinput}
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}

            # async with session.get(url=url, params=params, headers=headers) as resp:
            #     text = await resp.text()
            #     soup = BeautifulSoup(text, 'html.parser')
            #     search = re.findall(r'(https?://[^)\s]+)', text)
            #     print(search)
            #     # print(soup)
            #     a = soup.find('g-header-menu', {'id': 'ab_options'})
            #     x = a.find('div', {'jsname': 'x107ob'})
            #     print(x)
            link = await session.get(url=url, params=params, headers=headers)
            search = re.findall(r'(https?://[^)\s]+)', str(link))
            actual_link = ''.join(search)
            print(actual_link)
            async with session.get(url=actual_link, headers=headers) as resp:
                text = await resp.text()
                soup = BeautifulSoup(text, 'html.parser')
                heading_text = [x.text for x in soup.findAll('div',{'role':'heading'})]
                recipe_rating = [x.text for x in soup.findAll('span',{'class':'oqSTJd'})]
                recipe_ingredients = [x.text for x in soup.findAll('div',{'class':'LDr9cf L5KuY'})]

                # Recipe1 = heading_text[1]
                # Recipe2 = heading_text[2]
                # Recipe3 = heading_text[3]
                #
                # Recipes = "Recipes: " + Recipe1 + ", " + Recipe2 + ", " + Recipe3 + " Added to Database"
                # # Recipe1_Rating = recipe_rating[0]
                # # Recipe2_Rating = recipe_rating[1]
                # # Recipe3_Rating = recipe_rating[2]
                # # ratings = Recipe1_Rating + ", " + Recipe2_Rating + ", " + Recipe3_Rating
                # Recipe1_Ing = recipe_ingredients[0]
                # Recipe2_Ing = recipe_ingredients[1]
                # Recipe3_Ing = recipe_ingredients[2]
                # Ingred = Recipe1 + ": " + Recipe1_Ing + "\n" + Recipe2 + ": " + Recipe2_Ing + "\n" + Recipe3 + ": " + Recipe3_Ing
        for rec, ing in zip(heading_text[:3], recipe_ingredients[:3]):
            success = self.addToDB(rec, ing)
        if success:
            my_dic = json.load(open('JSONS/Recipes.json'))
            em = discord.Embed(title="Search Results")

            for x in my_dic:

                em.description(my_dic[x]['Recipe'])
                em.add_field(name="Ingredients\n", value=''.join(my_dic[x]['Ingredients']), inline=True)
                em.add_field(name="⠀", value="⠀")
                em.colour = 0xFFFA
            # em.set_image(url=ShowImageLink)
            em.set_author(name=userinput, url=actual_link, icon_url=" ")
            # em.set_thumbnail(url=img_link)

            await ctx.send(embed=em)
        else:
            my_dic = json.load(open('JSONS/Recipes.json'))
            e = discord.Embed(title="Recipe Database")
            for x in my_dic:
                e.add_field(name="Recipe\n", value=''.join(my_dic[x]['Recipe']), inline=True)
                e.add_field(name="Ingredients\n", value=''.join(my_dic[x]['Ingredients']), inline=True)
                e.add_field(name="⠀", value="⠀")
            await ctx.send(embed=e)
        # self.addToDB(Recipe1, Recipe1_Ing)
        # self.addToDB(Recipe2, Recipe2_Ing)
        # self.addToDB(Recipe3, Recipe3_Ing)
        # success = self.addToDB(Recipe1, Recipe1_Ing)
        # if success:
        #     em = discord.Embed(title="Search Results",
        #                        description=Recipes)
        #     em.colour = 0xFFFA
        #     # em.set_image(url=ShowImageLink)
        #     em.set_author(name=userinput, url=actual_link, icon_url=" ")
        #     # em.set_thumbnail(url=img_link)
        #     em.add_field(name="Ratings: \n\n", value=ratings)
        #     em.add_field(name="Ingredients: \n\n", value=Ingred)
        #     await ctx.send(embed=em)
        # elif not success:
        #     await ctx.send("Show already exits")
                # soup = BeautifulSoup(text, 'html.parser')
                # # print(soup)
                # a = soup.find('div', {'class': 'cF4V5c'})

        # async with aiohttp.ClientSession() as session:
        #     url = 'https://www.google.com/search?'
        #     line = "What can I make with "
        #     userinput = {'q': line + userinput}
        #     link = session.get(url, params=userinput)
        #     x = await link
        #
        #     # var = ([''.join(n.split()) for n in str(x)])
        #     search = re.findall(r'(https?://[^)\s]+)', str(x))
        #     searchlist.append(search)
        #     for x in range(len(searchlist)):
        #         y = ''.join(search)
        #     print(y)
        #     data = requests.get(y)
        #     em = discord.Embed(title="Search Results", description="Here is your results")
        #     em.colour = 0xFFFA
        #     em.add_field(name="Link to site", value=str(search))
        #     await ctx.send(embed=em)
        #
        #     soup = BeautifulSoup(data.text, 'html.parser')
        #     recipelist = []
        #     Recipe = soup.find_all('div')
        #     p = (str(Recipe).split())
        #     p.sort()
        #     print(p)
        #     print('\n' + str(Recipe))
        #     recipelist.append(soup)
        #     # for s in range(len(recipelist)):
        #         # print(soup)
        #         # print(soup.get_text('', strip=True))

    @commands.command()
    async def IS(self, ctx, *, userinput):
        searchlist = []
        async with aiohttp.ClientSession() as session:
            url = 'https://www.google.com/search?tbm=isch&q'
            userinput = {'q': userinput}
            link = session.get(url, params=userinput)
            x = await link

            # var = ([''.join(n.split()) for n in str(x)])
            search = re.findall(r'(https?://[^)\s]+)', str(x))
            searchlist.append(search)
            for x in range(len(searchlist)):
                y = ''.join(search)
            print(y)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        star = self.bot.get_emoji(638487897430949918)
        if reaction.emoji == '{star}':
            print("OwO")

        # soup = BeautifulSoup(userinput, 'html.parser')
        # async with aiohttp.ClientSession() as session:
        #     url = 'https://www.google.com/search?q='
        #     userinput = {'q': userinput}
        #     link = session.get(url, params=userinput)
        # em = discord.Embed(title="Search Results", description="Here is your results")
        # em.colour = 0xFFFA
        # em.add_field(name="Link to site", value=str(link))
        # await ctx.send(embed=em)



        #
        # with requests.Session() as k:
        #     url = 'https://www.google.com/search?q='
        #     userinput = {'q': userinput}
        #     link = requests.get(url, params=userinput)
        # em = discord.Embed(title="Search Results", description="Here is your results")
        # em.colour = 0xFFFA
        # em.add_field(name="Link to site", value=link.url)
        # await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Ingredients(bot))