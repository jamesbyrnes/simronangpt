import os
from dotenv import load_dotenv
import discord
from discord import app_commands

load_dotenv()
GUILD_ID = discord.Object(id=os.getenv('DISCORD_GUILD_ID'))

class DiscordClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=GUILD_ID)
        await self.tree.sync(guild=GUILD_ID)

intents = discord.Intents.default()
client = DiscordClient(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

def run():
    client.run(os.getenv('DISCORD_BOT_TOKEN'))
