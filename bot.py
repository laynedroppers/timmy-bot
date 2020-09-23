import os
import sys
import logging
import random
import discord
from dotenv import load_dotenv

import giphy_client
from giphy_client.rest import ApiException

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GIPHY_TOKEN = os.getenv("GIPHY_TOKEN")
MAX_GIF_QUERY = int(os.getenv("MAX_GIF_QUERY"))

client = discord.Client()
giphy_api = giphy_client.DefaultApi()
logger = logging.getLogger(__name__)


@client.event
async def on_ready():
    try:
        guild = discord.utils.get(client.guilds, name=GUILD)
        logger.info(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        members =[member.name for member in guild.members]
        logger.info(f"{len(members)} members found on the server. Fuck {random.choices(members)}")
    except Exception as e:
        logger.error(f"Could not connect to discord. {e}")
        sys.exit(1)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "timmy" in message.content:
        try:
            queries = ["I think you should leave", "tim robinson"]
            response = giphy_api.gifs_search_get(GIPHY_TOKEN, limit=MAX_GIF_QUERY, q=random.choices(queries))
            lst = list(response.data)
            gif = random.choices(lst)
            await message.channel.send(gif[0].url)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

client.run(DISCORD_TOKEN)
