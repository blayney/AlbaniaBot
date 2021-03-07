import discord
import os

client = discord.Client()

@bot.event
async def on_message(message):
  if 'albania' in message.content.lower():
    channel = member.guild.get_channel(message.channel.id)

    await channel.send('A new member joined.')