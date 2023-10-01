import discord
import random
import os
from discord.ext import commands
import requests    

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

data = ['ЭКОНОМЬТЕ РЕСУРСЫ', 'РАЗДЕЛЯЙТЕ МУСОР', 'СДАВАЙТЕ ВТОРСЫРЬЁ', 'ВЫБИРАЙТЕ ЭКОЛОГИЧНЫЙ ТРАНСПОРТ', 'ИСПОЛЬЗУЙТЕ ПОВТОРНО И НЕ БЕРИТЕ ЛИШНЕЕ', 'ВНЕДРЯЙТЕ ЭКО-ПРИВЫЧКИ НА РАБОТЕ', 'ОБРАТИТЕ ВНИМАНИЕ НА ПИТАНИЕ', 'ПОСТАРАЙТЕСЬ ОТВЫКНУТЬ ОТ ПЛАСТИКА']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def eco(ctx):
    eco_message = random.choice(data)
    await ctx.send(eco_message)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def choise(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content="repeating"):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi, im bot {bot.user}!')   

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture) 

def get_duck_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def data_fox():
    image = 'https://randomfox.ca/floof/'
    res = requests.get(image)
    data = res.json()
    return data['image']

@bot.command('fox')
async def fox(ctx):
    image_fox = data_fox()
    await ctx.send(image_fox)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)

bot.run("Here is your token")
