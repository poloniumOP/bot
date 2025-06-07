import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
# add token
token = os.getenv('Token')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.auto_moderation = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


# @bot.event
# async def on_reaction_add(reaction, user):
#     if user.bot:
#         return
#     if reaction.emoji == '':
#         role = discord.utils.get(user.guild.roles, name="Batch of 2027'")
        
@bot.command()
async def rol(ctx):
    emb = discord.Embed(title="1. Batch of 2027\n2. Batch of 2028\n3. Batch of 2029", color=0x00ff00)
    rmsg = await ctx.send("React for batch roles", embed=emb)
    await rmsg.add_reaction('1️⃣')
    await rmsg.add_reaction('2️⃣')
    await rmsg.add_reaction('3️⃣')

    global msgid
    msgid= rmsg.id

@bot.event
async def on_raw_reaction_add(rxn):
    if rxn.message_id != msgid:
        return

    gld = bot.get_guild(rxn.guild_id)
    u = gld.get_member(rxn.user_id)

    rldct = {'1️⃣': "Batch of 2027'",'2️⃣': "Batch of 2028'",'3️⃣': "Batch of 2029'"}
    # while editing make sure that the role names end with '
    btc = rldct.get(rxn.emoji.name)
    if btc is not None:
        btchr = discord.utils.get(gld.roles, name = btc)
        if btchr is not None:
            await u.add_roles(btchr)
    
@bot.event
async def on_raw_reaction_remove(rxn):
    if rxn.message_id != msgid:
        return

    gld = bot.get_guild(rxn.guild_id)
    u = gld.get_member(rxn.user_id)

    rldct = {'1️⃣': "Batch of 2027'",'2️⃣': "Batch of 2028'",'3️⃣': "Batch of 2029'"}
    # while editing make sure that the role names end with '
    btc = rldct.get(rxn.emoji.name)
    if btc is not None:
        btchr = discord.utils.get(gld.roles, name = btc)
        if btchr is not None:
            await u.remove_roles(btchr)
bot.run(token)