# bot.py
import os

import discord
from dotenv import load_dotenv
import random
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    albaniafacts = [
        'Albanians do not call home Albania, instead the name for the nation in its mother tongue is Shqipëri.',
        'The Albanian diaspora is vast, stretching from its neighbours such as Greece and Turkey to further afield nations such as the US and Canada – so much so that it is believed that the number of Albanians living outside Albania is greater than the country’s population of nearly 3 million. Hundreds of thousands emigrated following the collapse of the communist regime in 1991 and ensuing economic crisis.',
        'Albanian buses (called furgons) have no timetable, they depart when they are good and ready – or full.',
        'Albanians nod when they mean “no” and shake their head when they mean “yes”. Be careful answering questions with your head.',
        'According to a 2015 World Risk Report compiled by the UN, Albania is one of the countries in Europe most at-risk from natural disasters. Alone in such a category – with the exception of neighbouring Serbia and Netherlands –Albania is deemed to be at risk from flooding. In 2010, the country was hit by major floods, forcing as many as 7,000 families to be evacuated.'
    ]

    if 'albania' in message.content.lower():
        response = random.choice(albaniafacts)
        await message.channel.send(response)
keep_alive()
client.run(TOKEN)