import discord
import os,random
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

dizionario = {
    "carta": "va nel bidone della carta ,quello bianco"
    "bottiglia di plastica " : "va nel bidone della plastica  ,quello giallo"
    "buccia di banana " : "va nel bidone dell'umido ,quello marrone"
    "bottiglia di vetro" : "va nel bidone del vetro ,quello grigio"
    "lattina" : "va nel bidone del vetro ,quello grigio"
    "pennarelli " : "va nel bidone del secco  ,quello rosso"}
                                    

@bot.command(name="ricicla")
async def reuse(ctx,*,oggeto:str):
    oggetto = oggeto.lower
    if oggetto in dizionario:
        await ctx.send(dizionario[oggetto])
    else:
         await ctx.send("non so come si ricicla questooggeto")


bot.run("Il Mio Token")
