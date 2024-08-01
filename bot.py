import discord
from discord.ext import commands
import json
with open("setting.json",mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents=discord.Intents.all()
intents.members= True
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)  #bot是變數 !指令

@bot.event  
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata["welcome_channel"]))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata["welcome_channel"]))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx): #ctx = context (中文叫上下文)
    await ctx.send(f'latency is {int(bot.latency*1000)}(ms)')
"""
@bot.command()
async def picture(ctx):
    pic = discord.file('C:\\Users\\user\\Documents\\GitHub\\Discord-Bott\\picture\\testing picture.jpg')
    await ctx.send(file = pic)
註解上的出問題
""" 
bot.run(jdata["TOKEN"])