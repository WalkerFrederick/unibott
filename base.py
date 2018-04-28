import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot

@client.event
async def on_ready():
    print("unibott running.") #confirms if the bot is running
    
@client.event
async def on_message(message):
     charMessage = message.content;
     msgChannel = message.channel
     msgAuthor = message.author.id
     if 'strahd' in charMessage:
         await client.send_message(msgChannel, '<@%s> Watch your profanity!' % (msgAuthor))
     if charMessage[0] == '/' and charMessage[1] == '/':
          commandArray = charMessage.replace('/', '').split();
          if commandArray[0] == 'roll':
              try:
                  #roll a dice, min val 1, max specified in command.
                  await client.send_message(msgChannel, random.randint(1,int(commandArray[1])))
              except:
                  await client.send_message(msgChannel, "the command " + str(commandArray) + " is missing arguments!")
          elif commandArray[0] == 'ping':
               #prints pong.
                await client.send_message(msgChannel, 'pong!')
          elif commandArray[0] == 'pong':
               #prints ping.
               await client.send_message(msgChannel, 'ping!')
          elif commandArray[0] == 'countdown':
               count = int(commandArray[1])
               if count > 20:
                   await client.send_message(msgChannel, 'TOO BIG!')
               else:
                   while count >= 0:
                       await client.send_message(msgChannel, count)
                       count = count - 1
          else:
              await client.send_message(msgChannel, 'COMMAND IS INVALID, CHECK SPELLING!')
     else:
          print("")

client.run("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
