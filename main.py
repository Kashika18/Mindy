import discord
import os
import requests
import json
import random
import sad_words
import encouragement
import tip
from keep_alive import keep_alive

client = discord.Client()


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author==client.user:
		return

	msg = message.content

	if msg.startswith('*help'):
		async def embed(message):
			embed=discord.Embed(title="Helplines", url="https://www.vandrevalafoundation.com/", color=0xFF5733)
			await message.send(embed=embed)

	if msg.startswith('*hello'):
		await message.channel.send('Hello!'+message.author.mention)
		await message.channel.send(file=discord.File('joey.jpg'))

	if msg.startswith('*inspire'):
		quote = get_quote()
		await message.channel.send(quote)

	if any(word in msg for word in sad_words.words):
		await message.channel.send(random.choice(encouragement.encouragements))

	if msg.startswith('*tips'):
		await message.channel.send(random.choice(tip.tips))

	

	

keep_alive()
client.run(os.environ['token'])