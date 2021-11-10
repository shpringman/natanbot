import discord
import os
import asyncio

from keep_alive import keep_alive
import search_lulu
import twitter_funny
client = discord.Client()

banger_generator = twitter_funny.Banger()
lulu_web = search_lulu.Lululemon()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
  client.loop.create_task(my_background_task()) # best to put it in here

async def my_background_task():
    await client.wait_until_ready() # ensures cache is loaded
    #counter = 0
    channel = client.get_channel(id=906237140424339476) # replace with target channel id
    while not client.is_closed():
        #counter += 1
        scubastock = lulu_web.scuba(2)
        if '0' not in scubastock:
          await channel.send('<@198320888943214593>! <@!270440912327409675>!\n' + scubastock + ' are in stock in size XS/S!\nhttps://shop.lululemon.com/p/womens-outerwear/Scuba-Oversized-12-Zip-Hoodie/_/prod9960807')
        #await channel.send(counter)
        await asyncio.sleep(10)


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('hello <:nyanpfp:600130086259392512>')
  if message.content.startswith('$pingtest'):
    await message.channel.send('<@198320888943214593> <@!270440912327409675>')
  if message.content.startswith('so true'):
    await message.channel.send('<:sotrue:806533606766805072>')
  if f'$scuba' in message.content:
    scubastock = lulu_web.scuba(1)
    await message.channel.send('here is the current state of scuba oversized 1/2 zips:\n'+ str(scubastock))
  if f'$banger' in message.content:
    bangertweet = banger_generator.sendTweet()
    await message.channel.send(bangertweet)
  if message.content.startswith('$affirmation'):
    await message.channel.send('your lululemon method does work!!!!!!')
  if message.content.startswith('thank you natanbot'):
    await message.channel.send('<:nyanpfp:600130086259392512>')
  if message.content.startswith('$elie'):
    await message.channel.send('i am not elie')
  if message.content.startswith('natanbot'):
    await message.channel.send('yes?')
  if message.content.startswith('$hank'):
    await message.channel.send('https://cdn.discordapp.com/attachments/838822596295262248/906372973999566848/nnp06etsjdv61.png')
    


keep_alive()
client.run(os.getenv('TOKEN'))