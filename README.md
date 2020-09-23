# timmy-bot
Discord bot for posting Tim Robinson GIFs

## Setup
1. Install the virtual environment
    > pipenv install
2. Get the discord token for the bot
    - See [these instructions for help](https://www.writebots.com/discord-bot-token/)
3. Setup a giphy account and get a giphy api token
    - Follow Giphy's [getting started](https://developers.giphy.com/) instructions to get a token
4. Update the .env file with the environment variables gathered:
    - `DISCORD_TOKEN`=MYDISCORDTOKEN
    - `DISCORD_GUILD`=NAME OF MY DISCORD GUILD
    - `GIPHY_TOKEN`=MYGIPHYTOKEN
    - `MAX_GIF_QUERY`=MAXIMUMGIFSTOQUERY  

## Running Timmy
To run the bot, simply run the bot after following the setup instructions.
> pipenv run python bot.py

## Calling Timmy
After setting up the bot, timmy can simply be called by using the catchphrase "timmy" in the discord guild
