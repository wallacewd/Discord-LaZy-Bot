#########################################
# "LaZy Bot" for Discord                #
# Author: Dan Wallace                   #
# www.brick.technology                  #
#########################################

## To run at its best, follow the advice below  ##
# 1. Works well with XavinBot. Users can Emoji react to XavinBot posts to add roles to their name. 
# 2. Add a role for every game you want your server to promote.
# 3. This bot works by filtering the ignore list vs the users total roles.
# 4. Whatever remains the bot will randomly pick from and select a game.

# Type !lazy for the bot to select a game. Type !lazystats to see how many times your bot has been used.

# Start Code:
# 1.0 Imports
import os
import random
import discord
from discord.ext import commands
import pandas as pd

## Steps 2-4: Server Admin Controls

# 2.0 Obtain your Discord token from Discords Developer Portal
TOKEN = 'DISCORD TOKEN HERE'
# 2.1 Enter your Guild name 
GUILD = 'GUILD NAME'
# 2.2 Enter your YouTube Api Key Here
Youtube_Api_Key = 'YOUTUBE API KEY HERE'

# 3.0 Insert the names of Roles that are not video game roles:
ignore = ['GameBot','XavinBot','@everyone','Chaos','Nemesis','Eros','Co-owner','Cronos','Helios','Aether','Hades','Hermes','Dionysus','Poseidon','Gods','Hecate','Banished to Tartarus','Aristoi','Chaos Seeds','Server Booster','Streaming','Gods','YourAnus','Discgolf','UrAnus','Tabletop','Uranus']

# 4.0 Bot Prefix Command
bot = commands.Bot(command_prefix='!')

## Steps 5-6: Bot Code

# 5.0 Stat Counter Function
def counter():
    csv_open = pd.read_csv('data/counter.csv')
    df_open = pd.DataFrame(csv_open)
    counter = int(df_open['count'][0])
    new_counter = (counter + 1)
    df_open['count'].at[0] = new_counter
    df_open.to_csv('data/counter.csv', index = False, header=True)

# 6.0 Lazy Command Handle 
@bot.command(name='lazy', help='Responds with and random game you have reacted to in Role-Assign',pass_context=True)
async def test(ctx):
    csv_open = pd.read_csv('data/counter.csv')
    df_open = pd.DataFrame(csv_open)
    counter = int(df_open['count'][0])
    new_counter = (counter + 1)
    df_open['count'].at[0] = new_counter
    df_open.to_csv('data/counter.csv', index = False, header=True)
    game = "Go to the Role-Assign channel and emoji react to games you own!"
    try:
        count = 0
        role_list = []
        for role in ctx.author.roles:
            if role.name not in ignore:
                role_mem = ctx.author.roles[count]
                role_list.append(role)
                count += 1
        set_difference = set(role_list) - set(ignore)
        list_difference = list(set_difference)
        difference_len = len(list_difference)
        random_game = random.randrange(0,difference_len)
        print(ctx.author," picked: ", list_difference[random_game])
        game = str(list_difference[random_game])        
    except Exception as e:
        print('LaZy Bot Error: ',e)
    msg = "You should play: " + game + "."
    await ctx.send(msg)
    
# 6.1 Lazystats Command Handle 
@bot.command(name='lazystats', help='Responds with the total times the bot has been used',pass_context=True)
async def test(ctx):
    random_message = ['This sever is so lazy. I have been called on ','I\'m so lazyyyy. I just want to sleep yet y\'all have used me ','I have been called on ', 'I heard you like bots...well, get in line. I\'ve been hit on ','I\'ve been run over by a bus ']
    rm_len = len(random_message)
    choice = random.randrange(0,rm_len)
    result = random_message[choice]
    csv_open = pd.read_csv('data/counter.csv')
    df_open = pd.DataFrame(csv_open)
    stats = str(df_open['count'][0])
    msg = result + stats + " times."
    await ctx.send(msg)
    
# 6.2 Bored Command Handle
@bot.command(name='bored', help='Responds with and random youtube video',pass_context=True)
async def test(ctx):
    import json
    import urllib.request
    import string
    try:
        random_message = ['Oh..my game ideas aren\'t good enough for you? Fine.. here is a random video for you to watch: ','I\'m too lazy to find a good video, so here is a random one for you: ','Bored? Try watching this: ', 'Remember to like, comment and subscribe on this random video: ','LikE oMg YoU GuYs, WHAT IS UP LAZY GANG!!??! I\'m back with ANOTHER random video: ', 'Can we get this random video to 10 likes?? Make sure to say who sent you: ']
        rm_len = len(random_message)
        choice = random.randrange(0,rm_len)
        result = random_message[choice]
        counter()
        count = 1
        API_KEY = Youtube_Api_Key
        random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

        urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,random)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        results = json.loads(data.decode(encoding))
        video_result = []
        for data in results['items']:
            videoId = (data['id']['videoId'])
            link = 'https://www.youtube.com/watch?v=' + videoId
            video_result.append(link)
        print(ctx.author," watched: ",video_result[0])
        final_link = result + video_result[0]
        await ctx.send(final_link)
    except Exception as e:
        print(e)
bot.run(TOKEN)
