import discord
import os,random
from bot_logic import *
from discord.ext import commands
# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')
@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')
@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

#COMANDO HEH
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

#TESTA O CROCE 
@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())

#GENERAZZIONE EMOJI
@bot.command()
async def emodji(ctx):
     await ctx.send(gen_emodji())

#GENERAZIONE PASSWORD
@bot.command()
async def gen_pas(ctx):
    await ctx.send(gen_pass())

#RIPTIZIONE DI PAROLE 
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

#INDOVINO DEI NUMERI 
@bot.command()
async def guess(ctx, number: int):
    """indovina un numero tra 1 e 6."""
    # explained in a previous example, this gives you
    # a random number from 1-6
    value = random.randint(1, 6)
    # with your new helper function, you can add a
    # green check mark if the guess was correct,
    # or a red cross mark if it wasn't
    await ctx.send(number == value) 

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog(')
async def dog(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)


def get_pockemon_image_url():    
    url = ' https://pokeapi.co'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('pockemon')
async def pockemon(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_pockemon_image_url()
    await ctx.send(image_url)

bot.run("IL MIO TAG")
