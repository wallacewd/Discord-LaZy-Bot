import os
import random
import discord
from discord.ext import commands
import pandas as pd

TOKEN = 'NzgzMTU4NzE4MDQwNTA2NDE4.X8WrZA.qTTqpO1LfDCkPjQFcxEv7i_9oAs'
GUILD = 'Butcher\'s Mod Madness'

ignore = ['GameBot','XavinBot','@everyone','Chaos','Nemesis','Eros','Co-owner','Cronos','Helios','Aether','Hades','Hermes','Dionysus','Poseidon','Gods','Hecate','Banished to Tartarus','Aristoi','Chaos Seeds','Server Booster','Streaming','Gods','YourAnus','Discgolf','UrAnus','Tabletop','Uranus']

bot = commands.Bot(command_prefix='!')

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
        #role = discord.utils.find(lambda r: r.name == 'Member', ctx.user.server.roles)
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
        print(e)
    msg = "You should play: " + game + "."
    await ctx.send(msg)

@bot.command(name='lazystats', help='Responds with and random game you have reacted to in Role-Assign',pass_context=True)
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
"""
@bot.command(name='compare', help='Responds with and random game you have reacted to in Role-Assign',pass_context=True)
async def test(ctx):
    voice_channel2 = ctx.guild.channels

    #print(voice_channel)
    count = 0
    for item in voice_channel2:
        voice_channel = discord.utils.get(ctx.message.guild.channels, id=ctx.guild.channels[count].id, type=discord.ChannelType.voice)
        print(ctx.guild.channels[count] ,ctx.guild.channels[count].id)
        try:
            members = ctx.guild.channels[count].voice_members

            memids = []

            for member in members:
                memids.append(member.id)
            print(memids)
        except:
            print('Empty.')
        count += 1


    await ctx.send('hi')
"""

bot.run(TOKEN)