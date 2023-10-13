import discord
import os
from discord.ext import commands
import requests
import replicate
from dotenv import load_dotenv
import asyncio

load_dotenv()

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def guide(ctx):
    await ctx.send("Coming Soon!")

@bot.command()
async def ask(ctx, *, arg):  # Use * before arg to allow multi-word arguments
    output = replicate.run(
        "meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e",
        input={
            "prompt": arg,
            "max_new_tokens": 500,
            "temperature": 0.5,
            "repetition_penalty": 1,
            }
    )
    answer = ""
    for item in output:
        answer += item
    await ctx.send(answer)

bot.run(DISCORD_TOKEN)