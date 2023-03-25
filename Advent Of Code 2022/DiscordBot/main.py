# bot.py
import os
import requests
import discord
from datetime import datetime, time, timedelta
from discord.ext import commands
import asyncio
from pytz import timezone
import discord

# Create a new Discord client
client = discord.Client()

# Define a function that will be called when the bot is ready
@client.event
async def on_ready():
    # Print a message to the console
    print("Bot is ready!")

    # Set the current channel
    channel = client.get_channel(1049008278790746145)

    # Send a message to the channel every day at 11pm
    while True:
        # Get the current time
        now = datetime.now()

        # Check if the current time is 11pm
        if now.hour == 10 and now.minute == 26:
            # Send the message to the channel
            await channel.send("Hello, it's 11pm!")
            await asyncio.sleep(60)
        # Wait for one minute before checking the time again
        await asyncio.sleep(1)


# Run the bot using your bot's token
print("starting")
client.run("MTA0OTAwNzU2MTE4MzA4MDUzOQ.GnOtfF.6_DmtiWf3elalRzTukaAoiKoF11cSF3iC20T38")