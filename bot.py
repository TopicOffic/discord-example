import discord
import asyncio
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "#")

#@client.command
#async def canale_principale(ctx):
 #  ctx.send("Setta il canale principale del BOT")
 #  @client.event
 #  async def on_message()



@client.event
async def on_ready():
   message = 'This motherfucker is ready'
   await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=message, url="https://www.twitch.tv/topicoffic"))
   print("Discord " + discord.__version__)
   print("--------------------------------------")
   print("Logged in as " + client.user.name)
   print("--------------------------------------")
   print("Client ID "+ str(client.user.id))
   print("--------------------------------------")

#   for channel in client.get_all_channels:
 #     print(channel)

      #if channel == 'generale':
      #  channel.send('This motherfucker is ready')

#class MyClient(discord.Client):
#    async def on_ready(self):
#        print('Logged on as {0}!'.format(self.user))


@client.command()
async def clear(ctx, amount=2):
   await ctx.channel.purge(limit=amount)


@client.command()
async def popo(ctx):
   await ctx.send(random.choice(["1,1"]))

   print("Qualcuno ha fatto il furbetto!!")

@client.command()
async def ciao(ctx):
   await ctx.send("Ciao anche a te!")
   print(client)

@client.event
async def on_member_join(member):
   print(f'Hello {member}')

@client.event
async def on_member_remove(member):
   print(f'Goodbye {member}')


client.run('kAHFn8AUP7ddY1JhSK9vEmDBPnkZ5SJw')
