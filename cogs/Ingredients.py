import discord
from discord.ext import commands
import sys
import re
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import aiohttp
import requests

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
                    
var cheerio = require("cheerio"); 
var request = require("request"); 
 
var discord = require("discord.js");
var client = new discord.Client();

client.login("private token");
 
client.on("ready", function() {
    console.log("logged in");
});
 
client.on("message", function(message) {
 
    var parts = message.content.split(" ");
    
    if (parts[0] === "!Search") { // Check if first part of message is image command
 
        image(message, parts); // Pass requester message to image function
 
    }
 
});
 
function image(message, parts) {
 
    var search = parts.slice(1).join(" "); 
 
    var options = {
        url: "http://results.dogpile.com/serp?qc=images&q=" + search,
        method: "GET",
        headers: {
            "Accept": "text/html",
            "User-Agent": "Chrome"
        }
    };
    request(options, function(error, response, responseBody) {
        if (error) {
            // handle error
            return;
        }
  
        $ = cheerio.load(responseBody); 
 
        var links = $(".image a.link");
 
        var urls = new Array(links.length).fill(0).map((v, i) => links.eq(i).attr("href"));
        console.log(urls);
        if (!urls.length) {
            return;
        }
 
        message.channel.send( urls[0] );
    });
 
}
/*                    
@commands.command()
    async def Search(self, ctx, *, userinput):
        print(userinput)
        searchlist = []
        async with aiohttp.ClientSession() as session:
            url = 'https://www.google.com/search?'
            line = "What can I make with "
            userinput = {'q': line + userinput}
            link = session.get(url, params=userinput)
            x = await link

            # var = ([''.join(n.split()) for n in str(x)])
            search = re.findall(r'(https?://[^)\s]+)', str(x))
            searchlist.append(search)
            for x in range(len(searchlist)):
                y = ''.join(search)
            print(y)
            data = requests.get(y)
            em = discord.Embed(title="Search Results", description="Here is your results")
            em.colour = 0xFFFA
            em.add_field(name="Link to site", value=str(search))
            await ctx.send(embed=em)

            soup = BeautifulSoup(data.text, 'html.parser')
            recipelist = []
            Recipe = soup.find_all('div')
            p = (str(Recipe).split())
            p.sort()
            print(p)
            print('\n' + str(Recipe))
            recipelist.append(soup)
*/

def setup(bot):
    bot.add_cog(Ingredients(bot))
