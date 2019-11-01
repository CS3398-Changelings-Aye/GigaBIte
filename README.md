# GigaBite
  ## Project Name:

 [![Logo](https://raw.githubusercontent.com/CS3398-Changelings-Aye/CS3398-Changelings-S2019/master/LogoMakr_3yOZ1T.png)](https://discord.gg/3EWYfUb)
  
  ## Description:
  We are creating a Discord Bot that is able to search for recipes with a certain ingredient. This will be for those who love to cook or what to love to cook but don't have time or the knowledge to find recipes on their own. It is being done in order to offer a simplistic and easy way to obtain a variety of different recipes without the hastle of searching through blogs. 
  
  ## Status
  * InProgress: Beta Testing. 
  * Our bot Currently has functionality on a small number of servers and can complete simple tasks to engage the user as well as allow the user to search through Youtube, HEB, Google, and Google Images to find pictures of food that the user may want.
  
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
* [Retrospective](#Retrospective)
* [Next Steps](#Next-Steps)
* [Contributions2](#contributions-2)
* [Retrospective 2](#Retrospective-2)
* [Next Steps 2](#Next-Steps-2)


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


## Retrospective
 What Went Well or maybe not?
 * Team needs to communicate more as well as outline tasks and assess what everyone can and can not do. The basic creation of the bot went relatively well but we need to work on overall group understanding. The group should try and meet every week to discuss goals and updates on the project outside of class for at least 1 hour. 


(Team) Four or more team bullets
* We were able to get a considerable amount done, even though we had more we wanted to do. We were able to get some fully functional code and have the bot work.
* We had many great ideas that need to be expanded upon and borken down more into workable points for the next sprint.
* Different team memebers not familiar with the programming language stepped up and contributed code to the overall project, furthering the team's progress and their own understanding.
* Team memebers were individually proactive and assigned themseles previously unassigned tasks to further along the project.


(Individual) One bullet per team member.
* Dalton Melivlle: I feel like I was able to expand my knowledge of Pyhton along with with a wider range of what bots are capable of. Unfortunately I feel like we could manage our times better in order to communicate well.

* Nicole Runas: I feel like I was able to get more comfortable wokring in a new coding language and trying to utilize using new design patterns.

* Sebastian Santana: I feel like I learned a lot of the basic fundamentals during this sprint but due to a lack of communication I feel like a lot of time was not very well spent on my end. I need to push for better communication with my team and learn to manage time better.

* Nisa Lateef: I had coded in python before for a bit, but applying the skills I had learned to code a discord bot was interesting. I was able to feel more comfortable with using a different language then the ones I normally use. In the future, I would like to manage my time better, and communicate better with the team whenever I am stuck.

* Wilson Benitez: 

What Might Be Impeding Us from Performing Better?
  (Team) One or more team bullets
  * The team need to find time where everyone can meet outside of class to discuss the project.

What Can We do to Improve?

(Team) One or more team bullets
* Meet outside of class
* Communicate when commits/changes are being made
* Notify the team when struggling with a certain aspect of their assigned task
* Ask teammates questions and communicate about any roadblocks


(Individual) One bullet per team member with specific,
measurable improvement action described

* Nicole Runas: To improve my skills, I will attempt to create my own dscord bots outside of the class and try to expand their functionality to learn more about integrating bots with apis and utilizing other design patters. I will upload key bits of working code onto my personal repositories to track my progress.

* Dalton Melville: Get better at Communicating with the team to ensure we know what each other is working on

* Sebastian Santana: Communicate and meet up more. We need to be able to understand where and what everyone is doing or how they are understanding the project. 

* Nisa Lateef: Once a week, it's important to meet up with the team so we can discuss the project and help out whenever someone doesn't understand something. 

* Wilson Benitez: Get more familiarized with the discord api, get better at time management to contribute to the project.

## Contributions 2
* Nicole Runas: 
* Dalton Melivlle: Created Moderation for the bot so that members that can't behave will be kicked/banned. Was working on the user made database but ran into a roadblock concerning the html code to parse.

* Sebastian Santana: 
 
* Nisa Lateef: 

* Wilson Benitez: 
## Retrospective 2
What Went Well or maybe not?
 * Team needs to communicate more as well as outline tasks and assess what everyone can and can not do. The basic creation of the bot went relatively well but we need to work on overall group understanding. The group should try and meet every week to discuss goals and updates on the project outside of class for at least 1 hour. 


(Team) Four or more team bullets
* We were able to get a considerable amount done, even though we had more we wanted to do. We were able to get some fully functional code and have the bot work.
* We had many great ideas that need to be expanded upon and borken down more into workable points for the next sprint.
* Different team memebers not familiar with the programming language stepped up and contributed code to the overall project, furthering the team's progress and their own understanding.
* Team memebers were individually proactive and assigned themseles previously unassigned tasks to further along the project.


(Individual) One bullet per team member.
* Dalton Melivlle: What didn't go well was being able to be up to par on having Categories completed, as well as being able to create a database based on user input. What went well was being able to add miscellaneous, and moderation. 
* Nicole Runas: What went well for me was expanding my knowledge on creating and implementing cogs. I also think the team communication was a lot stronger this time around, as well. What did not go well was splitting up larger tasks instead of tackling them as a team.
* Sebastian Santana: 
* Nisa Lateef: What went well was that I learned more about programming using discord.py from my other team members which ended up helping all of us. What did not go well was it was quite difficult to figure out the save recipe feature for this sprint, and therefore, it couldn't be implemented the way we wanted it to be implemented. 
* Wilson Benitez: What went smooth for me was finding the link to search images on google, but having to put it in discord was difficult

What Might Be Impeding Us from Performing Better?
  (Team) One or more team bullets
  * The team need to find time where everyone can meet outside of class to discuss the project.
  * We should be more comfortable to reach out to other team members whenever one of us hits a roadblock
  * We should be able to error check commands on discord

What Can We do to Improve?

(Team) One or more team bullets
* Meet outside of class
* Communicate when commits/changes are being made
* Notify the team when struggling with a certain aspect of their assigned task
* Ask teammates questions and communicate about any roadblocks


(Individual) One bullet per team member with specific,
measurable improvement action described

* Nicole Runas: My improvement stemmed from team communication and taking the time to build my own bot separately from the team. Currently, I am researching using a drink database.
* Dalton Melville: Work on time management and team communications, be able to communicate with the team when we should be able to meet. What I've improved on is being able to communicate a bit better with the team. I've improved being able to learn about api's and discord bots.
* Sebastian Santana: 
* Nisa Lateef: To improve, I'm going to work on reaching out to my teammembers whenever I hit a roadblock. I was able to enhance my knowledge in discord.py and was able to contribute more to this sprint.  
* Wilson Benitez: Improvment came from asking help from my team, help me use the right API function to get it to display properly.

## Next Steps 2
 * Dalton Melville: Next step is to look into Databases and be able to complete the user search database, as well as the Image search database.
 * Nicole Runas: My next step is to expand the drink options that the bot give and research how to add specificality to each entre.
 * Sebastian Santana: 
 * Nisa Lateef: My next step is to figure out a way to save favorited recipes for the user to access later and to work on the youtube search function so we could add more functionality.
 * Wilson Benitez: My next steps is to put images in a package and have us pull from that packet if it has been search.
