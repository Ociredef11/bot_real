import discord
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

bot.run("MTMxMjA5NDA4NTUyNzM3NTk4NA.GARxzP.y9iG8iFHlmZqNs9kFzr05y7RYhF57sQSf03A6g")
