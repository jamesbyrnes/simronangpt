import discord
from discord import app_commands

# TODO: REPLACE WITH REAL GUILD# OR ENV
GUILD_NUM = discord.Object(id=0)

class DiscordClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=GUILD_NUM)
        await self.tree.sync(guild=GUILD_NUM)

intents = discord.Intents.default()
client = DiscordClient(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

def run():
    print('hi, starting up')

    # TODO: REPLACE WITH REAL TOKEN OR ENV
    client('token')
