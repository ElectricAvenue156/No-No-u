import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.invisible, activity=discord.Game(name="I have crippling depression"))

@client.event
async def on_message(message):
  await No_u(message)

async def No_u(message):
  if message.content == "No u" or message.content == "no u" or message.content == "nO u" or message.content == "no U" or message.content == "NO u" or message.content == "nO U" or message.content == "No U" or message.content == "NO U" or message.content == "nou" or message.content == "NOU":
    await message.delete()

client.run('NzkxMzUzMjg2OTI1MjIxOTEw.X-N7Lg.K-0Pxlp0j7AX2Bp_8d3KJHxxUQs')
