import openai
import os
import json
import discord
from discord.ext import commands

with open('config.json') as config_file:
    config = json.load(config_file)

bot_token = config['bot_token']
openai.api_key = config['openai_api_key']

os.system("cls" if os.name == "nt" else "clear")

intents = discord.Intents.default()
intents.message_content = True  

client = commands.Bot(command_prefix='.', help_command=None, intents=intents)

class Chat:
    def __init__(self):
        self.model_id = "gpt-3.5-turbo"

    def get_response(self, message):
        response = openai.ChatCompletion.create(
            model=self.model_id,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content

@client.event
async def on_ready():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Connected as {client.user}")
    game = discord.Game("@akxd")
    await client.change_presence(activity=game, status=discord.Status.dnd)

@client.slash_command(name="ask", description="Get an answer to a question.")
async def ask(ctx: discord.ApplicationContext, question: str):
    await ctx.respond("Request Sent!", ephemeral=True)
    chat = Chat()
    try:
        response = chat.get_response(message=question)
    except Exception as e:
        response = f"Failed to get response.\n\nDebug info: ```{e}```"
    em = discord.Embed(description=f"> {question}\n\n```{response}```", color=0x000000)
    em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
    await ctx.send(embed=em)

@client.command()
async def ask(ctx, *, question: str):
    chat = Chat()
    try:
        response = chat.get_response(message=question)
    except Exception as e:
        response = f"Failed to get response.\n\nDebug info: ```{e}```"
    em = discord.Embed(description=f"> {question}\n\n```{response}```", color=0x000000)
    em.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
    await ctx.send(embed=em)

client.run(bot_token, reconnect=True)
