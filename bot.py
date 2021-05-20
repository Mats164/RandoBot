import random
import os
# pip install discord.py
import discord
from discord import colour
from discord import embeds
from discord.ext import commands
import json
# pip install requests
from requests import get
# pip install discord-py-slash-command
from discord_slash import SlashCommand, SlashContext

botPrefix = '$'

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=botPrefix, intents=intents)
slash = SlashCommand(bot, sync_commands=True)

guildList = []
for guild in bot.guilds:
    guildList.append(bot.get_guild[guild])

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord!')

'''@bot.command(name='grill', help=' - Griller deg med et tilfeldig Amir quote')
async def grill(ctx):
    amirQuotes = [
        'Er det teori eller hypotese da?', 'Jeg skal grille deg!', 
    ]

    response = random.choice(amirQuotes)
    await ctx.send(response)'''

@bot.command(name='status')
async def status(ctx):
    await ctx.send(f'{bot.user.name} is connected to discord!')

@bot.command(name='xkcd', help=' - Posts a comic from xkcd, parameters: latest or random')
async def xkcd(ctx, comic: str):
    if comic == 'latest':
        jsonGet = get("http://xkcd.com/info.0.json")
        latest = jsonGet.json()['img']
        title = jsonGet.json()['title']
        latestComNum = str(jsonGet.json()['num'])
        embed = discord.Embed(title=f'{title} (xkcd {latestComNum})', url=('http://xkcd.com/' + latestComNum), color=0xFF5733)
        embed.set_image(url=latest)
        await ctx.send(embed=embed)
    elif comic == 'random':
        jsonGet = get("http://xkcd.com/info.0.json")
        maxNum = jsonGet.json()['num']
        randomComNum = str(random.randint(1, maxNum))
        # label: link
        randomLink = 'http://xkcd.com/' + randomComNum + '/info.0.json'
        jsonGet = get(randomLink)
        randomComic = jsonGet.json()['img']
        title = jsonGet.json()['title']
        embed = discord.Embed(title=f'{title} (xkcd {randomComNum})', url=('http://xkcd.com/' + randomComNum), color=0xFF5733)
        embed.set_image(url=randomComic)
        message = await ctx.send(embed=embed)
        await message.add_reaction('◀️')
        # randomComNum = randomComNum - 1
        # goto link
        await message.add_reaction('▶️')

'''@bot.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji

    if user.bot:
        return

    if emoji == '◀️':
        print('Left')
    elif emoji == '▶️':
        print('right')
    else:
        return'''

@bot.command(name='pop')
async def bubble(ctx, dimensions: str):
    bubbles = ''
    dimensions = dimensions.split('x')
    width = int(dimensions[0])
    height = int(dimensions[1])

    for i in range(height):
        for i in range(width):
            bubbles = bubbles + '||pop||'
        bubbles = bubbles + '\n'

    if len(bubbles) < 2000:
        message = await ctx.send(bubbles)
        await message.add_reaction('🔄')
    else:
        await ctx.send("That's too big of a bubblewrap, you wouldn't be able to pop them all!")

'''@bot.command(name='embed')
async def embed(ctx):
    embed = discord.Embed(title="Sample Embed", url="https://xkcd.com/", color=0xFF5733)
    embed.set_image(url='https://imgs.xkcd.com/comics/astrophotography.png')
    await ctx.send(embed=embed)'''

'''@bot.command(name='mention')
async def mention(ctx):
    author = ctx.message.author
    await ctx.send(f'{author.mention} mentioned')'''

@bot.command(name='foaas')
async def foaas(ctx, target: str):
    sender = (ctx.message.author).mention
    to = target
    foaasUrls = [
    f'/asshole/{sender}',
    f'/back/{to}/{sender}', 
    f'/bag/{sender}', 
    f'/because/{sender}', 
    f'/blackadder/{to}/{sender}', 
    f'/bucket/{sender}', 
    f'/bus/{to}/{sender}', 
    f'/bye/{sender}', 
    f'/chainsaw/{to}/{sender}', 
    f'/cocksplat/{to}/{sender}', 
    f'/cool/{sender}', 
    f'/cup/{sender}', 
    f'/off/{to}/{sender}', 
    f'/nugget/{to}/{sender}', 
    f'/madison/{to}/{sender}', 
    f'/looking/{sender}', 
    f'/linus/{to}/{sender}', 
    ]
    headers = {'Accept': 'application/json'}
    foaas = get(f"https://foaas.com{random.choice(foaasUrls)}", headers=headers)
    await ctx.send(foaas.json()['message'] + '\n' + foaas.json()['subtitle'])
    # await ctx.send(foaas.json()['subtitle'])

@bot.command(name='insult')
async def insult(ctx):
    jsonGet = get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    insult = jsonGet.json()['insult']
    # await ctx.send(f'Hey {ctx.messaage.author}, {insult}')
    await ctx.send(insult) 

@bot.command(name='howgay')
async def gay(ctx):
    response = f'You are {random.randint(0, 100)}% gay!'
    await ctx.send(response)

@bot.command(name='compendium')
async def compendium(ctx, entry: str):
    compendium = get(f'https://botw-compendium.herokuapp.com/api/v1/entry/{entry}')

    if compendium.json()['data'] == {}:
        embed = discord.Embed(title='No results', description='Invalid entry :(', colour=0xFF5733)
        embed.set_author(name='Hyrule Compendium')
        await ctx.send(embed=embed)
        return

    location = compendium.json()['data']['common_locations']
    name = compendium.json()['data']['name']
    img = compendium.json()['data']['image']
    about = compendium.json()['data']['description']
    category = compendium.json()['data']['category']
    embed = discord.Embed(title=name, description=about, colour=0x6bebff)

    if category == 'creatures':
        drops = compendium.json()['data']['drops']
        if isinstance(drops, list):
            drops = ', '.join(drops)
        embed.add_field(name='**Drops**', value=drops, inline=True)
    elif category == 'treasure':
        drops = compendium.json()['data']['drops']
        if isinstance(drops, list):
            drops = ', '.join(drops)
        embed.add_field(name='**Drops**', value=drops, inline=True)
    elif category == 'monsters':
        drops = compendium.json()['data']['drops']
        if isinstance(drops, list):
            drops = ', '.join(drops)
        embed.add_field(name='**Drops**', value=drops, inline=True)
    elif category == 'materials':
        cookingEffect = compendium.json()['data']['cooking_effect']
        hearts = compendium.json()['data']['hearts_recovered']
        embed.add_field(name='**Cooking Effects**', value=cookingEffect, inline=True)
        embed.add_field(name='**Hearts Recovered**', value=hearts, inline=True)
    elif category == 'equipment':
        attack = compendium.json()['data']['attack']
        defense = compendium.json()['data']['defense']
        embed.add_field(name='**Attack/Defense**', value=(f'{attack}/{defense}'), inline=True)

    embed.set_author(name='Hyrule Compendium')
    embed.set_thumbnail(url=img)
    if isinstance(location, list):
        location = ', '.join(location)
    embed.add_field(name='**Locations**', value=location, inline=True)
    embed.add_field(name='**Category**', value=category, inline=True)
    await ctx.send(embed=embed)

@bot.command(name='nugget')
async def nugget(ctx):
    query = 'nugget'
    offset = random.randint(0, 5)
    giphyParameters = {
        'api_key': 'UIX3RcfF8cUJGSBwbJAeSfuuaPeRITTx',
        'q': query,
        'limit': 1,
        'offset': offset
    }

    giphy = get('https://api.giphy.com/v1/gifs/search', params=giphyParameters)

    gifUrl = giphy.json()['data'][0]['url']
    await ctx.send(gifUrl)

@bot.command(name='slap')
async def slap(ctx, target):
    query = 'slap'
    offset = random.randint(0, 5)
    giphyParameters = {
        'api_key': 'UIX3RcfF8cUJGSBwbJAeSfuuaPeRITTx',
        'q': query,
        'limit': 1,
        'offset': offset
    }

    giphy = get('https://api.giphy.com/v1/gifs/search', params=giphyParameters)

    gifUrl = giphy.json()['data'][0]['url']
    '''embed = discord.Embed(title=f'{ctx.message.author.mention} slaps {target}')
    embed.set_image(url=gifUrl)
    await ctx.send(embed=embed)'''
    await ctx.send(f'{ctx.message.author.mention} slaps {target}')
    await ctx.send(gifUrl)

@bot.command(name='gay')
async def nou(ctx):
    await ctx.send('No U')

@slash.slash(name='insult', guild_ids=guildList)
async def slashInsult(ctx: SlashContext):
    jsonGet = get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    insult = jsonGet.json()['insult']
    # await ctx.send(f'Hey {ctx.message.author}, {insult}')
    await ctx.send(insult) 

bot.run(TOKEN)