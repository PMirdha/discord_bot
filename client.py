from discord.ext import commands
from googlesearch import search

from db_backend import QMODELOBJECT

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Yo Bot")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hi':
        await message.channel.send("hello")
    await client.process_commands(message)


@client.command()
async def google(ctx, *args, **kwargs):
    query = " ".join(args)
    for url in search(query, stop=5):
        await ctx.send(url)
    query_list = []
    for arg in args:
        query_list.append({"name": arg})
    QMODELOBJECT.insert_data(query_list)


@client.command()
async def recent(ctx, *, query):
    data = QMODELOBJECT.filter_name(query="%{}%".format(query))
    for row in data:
        await ctx.send(row[0])