# GigaBite
  ## Project Name:

 [![Logo](https://raw.githubusercontent.com/CS3398-Changelings-Aye/CS3398-Changelings-S2019/master/LogoMakr_3yOZ1T.png)](https://discord.gg/3EWYfUb)
  
  ## Description:
  We are creating a Discord Bot that is able to search for recipes with a certain ingredient. This will be for those who love to cook or what to love to cook but don't have time or the knowledge to find recipes on their own. It is being done in order to offer a simplistic and easy way to obtain a variety of different recipes without the hastle of searching through blogs. 
  
  ## Status
  * InProgress: Beta Testing. 
  * Our bot Currently has functionality on a small number of servers and can complete simple tasks to engage the user and return recipes from a database as well as search the web for more specific ingredients or recipes and return the data.
  
  ## Team Members:
  > Dalton Melville,
  > Nicole Runas,
  > Sebastian Santana,
  > Nisa Lateef,
  > Wilson Benitez

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Contributions](#contributions)

## General Info
  If you would like to invite the bot to your discord, [Please Click Here](https://discordapp.com/api/oauth2/authorize?client_id=623906771500662795&permissions=0&scope=bot)

## Technologies
* PC's
* [Discord Bot](https://discordapp.com/developers/applications/)
* [Python](https://www.python.org/downloads/)
* [Discord API](https://discordpy.readthedocs.io/en/latest/api.html)
* [Digital Ocean](https://www.digitalocean.com)
* [AirTable](https://airtable.com/universe/expHZcS7kWEyq5gUH/recipe-database)

## Features
* Show Searching: Allows the user to search for a show.
* Recipe Searching: Allows the user to search for a recipe with given Ingredients.
* Ingredient choosing: Allows user to search for recipes using one specific ingredient.
* Meats choosing: Allows users to choose a kind of meat additionaly to ingredients and finding the best recipe for you.
* Meal Type Choosing: Allows the user the choose what type of meal they're looking for. Healthy, vegan, protein, etc.
* Recipe Saving: Allows a user to save a limited number of recipes to a Favorites Database.

## Contributions
* Nicole Runas: Help menu and friendly user interface, including friendly repsonses and an icon for the Bot. These help the Bot appear  welcoming to users and serve to make the Bot feel more like an actual person. I also found an ingredient database to be used for the Bot to complete searches against. The databse is used whenever a user send an ingredient to the Bot. Artifacts corresposnging to these can separately be found in the branch Lo and integreated into the cogs file on the master branch.

* Dalton Melivlle: Created/Setup Discord server along with the bot, took a database of ingredients and created a script to only show the ingredients and it's typing. Worked with Wilson to create a script that would look for the users input and return an ingredient matching their input. Implemented a small database of recipes with their ingredients, was able to use what Wilson and I created to search through the recipe database. Created the Search function which allows a user to search for specific things on the web.

* Sebastian Santana: Researching how to implement a .io database so that the discord bot can either use beautiful soup or some other method to find recipes with that database. Also created and helped edit and organize some of the basic discord code as well as researching and learning the varios discord API methods. Lastly coded a basic user calling function for the discord bot to attempt and familiarize myself with the API more. 
 
* Nisa Lateef: Found a database that is used as a way to allow the user to access basic categories that they desire for their recipe. Coded a welcome page that introduces the bot and it's authors. Also found another database that can be used for recipes to expand the amount of ingridents the bot can recommend. Artifacts correspanding to these can be found in the branch Nisa and integrated into cogs.

* Wilson Benitez: Worked closely with Dalton on setting up the cook command of the bot which allows a user to search through a database and return a recipe with the ingredients. 


## Next Steps
 * Dalton Melville: Continue to search for a larger database of recipes/ingredients as well as having the bot only allow for food searching on the web or instead of returning a link, have it return the first 10 search results for the user.
 * Nicole Runas: Continue to learn more about coding in Python and help expand the online searching functionality of the bot. Currently: researching web search through a bot
 * Sebastian Santana: Continue database research and Push more into the programming aspect.
 * Nisa Lateef: Enhancing my skills in python, and further applying them into the project, as well as expanding the bot's                     functionality, by adding a save recipe feature for the user. 
 * Wilson Benitez: Continue to learn more about the discord API and familiarize myself with how commands/events work as well as continue working on the searching of the database such that it will be specific to what the user has available.
