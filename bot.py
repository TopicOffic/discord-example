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
   await ctx.send(random.choice(["https://cdn77.scoreuniverse.com/modeldir/data/posting/60/958/posting_60958_x_xl.jpg",
               "https://cdn77.scoreuniverse.com/18eighteen/gallys/images_content/Adel_35036/13_tn.jpg",
               "https://cdn77.scoreuniverse.com/18eighteen/gallys/images_content/Adel_35036/15_tn.jpg"
               "http://cdn.hdpornpictures.com/2016-12-24/389207_14.jpg",
               "http://cdn.hdpornpictures.com/2019-02-01/588632_02.jpg",
               "http://cdn.hdpornpictures.com/2019-05-26/614361_13.jpg",
               "http://cdn.hdpornpictures.com/2019-04-28/609832_15.jpg",
               "http://cdn.hdpornpictures.com/2016-10-19/375505_09.jpg",
               "https://images.nubiles.net/galleries2/kelsey_kage/3_new-comer/tn/9.jpg",
               "https://images.nubiles.net/galleries2/kelsey_kage/3_new-comer/tn/16.jpg",
               "http://cdn.hdpornpictures.com/2018-11-10/562308_04.jpg",
               "http://cdn.hdpornpictures.com/2019-04-18/580378_02.jpg",
               "http://cdn.hdpornpictures.com/2018-12-19/563356_09.jpg",
               "http://cdn.hdpornpictures.com/2016-05-07/351751_06.jpg",
               "http://cdn.hdpornpictures.com/2018-09-17/560261_14.jpg",
               "http://cdn.hdpornpictures.com/2019-05-04/583615_12.jpg",
               "http://galleries.momsteachingteens.com/p/blakeallie/images/31.jpg",
               "http://galleries.momsteachingteens.com/p/blakeallie/images/35.jpg",
               "http://galleries.momsteachingteens.com/p/blakeallie/images/23.jpg",
               "http://galleries.sexymomma.com/042019/photo/audrey-aguilera-chasey-lain/images/11.jpg",
               "http://galleries.sexymomma.com/042019/photo/audrey-aguilera-chasey-lain/images/10.jpg",
               "http://galleries.sexymomma.com/042019/photo/audrey-aguilera-chasey-lain/images/14.jpg",
               "http://galleries.sexymomma.com/042019/photo/audrey-aguilera-chasey-lain/images/3.jpg",
               "http://galleries.sexymomma.com/042019/photo/audrey-aguilera-chasey-lain/images/5.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-sasha-heart/images/10.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-sasha-heart/images/12.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-sasha-heart/images/14.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-sasha-heart/images/9.jpg",
               "http://cdn.affiliates.mature.nl/4/free/6952/pictures/111176.jpg",
               "http://cdn.affiliates.mature.nl/4/free/6952/pictures/111174.jpg",
               "http://cdn.affiliates.mature.nl/4/free/6952/pictures/111179.jpg",
               "http://cdn.affiliates.mature.nl/4/free/6952/pictures/111180.jpg",
               "http://cdn.affiliates.mature.nl/4/free/6952/pictures/111182.jpg",
               "http://cdn.affiliates.mature.nl/4/free/6952/pictures/111185.jpg",
               "http://cdn.affiliates.mature.nl/4/free/6952/pictures/111184.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-mandy-more/images/13.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-mandy-more/images/12.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-mandy-more/images/14.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-mandy-more/images/4.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-mandy-more/images/8.jpg",
               "http://galleries.sexymomma.com/042019/photo/brenda-james-mandy-more/images/9.jpg",
               "http://cdn.hdpornpictures.com/2017-08-15/455205_01.jpg"]))

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


client.run('NTk4NTc2ODU3ODUxNDk0NDM5.XSYsLg.4QdnMTsIarZ7f1nyZgd4Fk-zee4')
