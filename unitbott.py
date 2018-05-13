import discord, random, dandd
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client() # initialise Client 
client = commands.Bot(command_prefix = "//") #initialise client bot

@client.event
async def on_ready():
    print("unibott running.") #confirms if the bot is running
    
@client.event
async def on_message(message):
     charMessage = message.content;
     msgChannel = message.channel
     msgAuthor = message.author.id
     # will check for specified word and call out author if detected.
     if 'badword' in charMessage:
         await client.send_message(msgChannel, '<@%s> Watch your profanity!' % (msgAuthor))
     # '//' is unibott's command prefix,
     # this if statement checks if '//' is present the begining of a msg.
     # if '//' is present and a specified command isnt present then an error msg will let the user know.
     if charMessage[0] == '/' and charMessage[1] == '/':
          commandArray = charMessage.replace('/', '').split();
     # best practice for a command that takes args,
     # in this case the command '//roll' also needs the max roll value. 
          if commandArray[0] == 'roll':
                # roll a dice, min val 1, max specified by user.
                rollArray = dandd.roll(commandArray)
                print (rollArray)
                rollCount = len(rollArray)
                index = 0
                while rollCount != 0:
                    await client.send_message(msgChannel, rollArray[index])
                    index = index + 1;
                    rollCount = rollCount - 1;
     # another example of a command with args, this one has a max input.
          elif commandArray[0] == 'countdown':
               count = int(commandArray[1])
               try:
                    if count > 20:
                        await client.send_message(msgChannel, 'TOO BIG!')
                    else:
                        while count >= 0:
                            await client.send_message(msgChannel, count)
                            count = count - 1
               except:
                                     await client.send_message(msgChannel, "the command " + str(commandArray) + " is missing arguments!")
     # voting
          elif commandArray[0] == 'vote':
              try:
                   await client.send_message(msgChannel,  '**NEW VOTE** @everyone\n' + ':a:' + commandArray[1] + '\n:b:' + commandArray[2])
              except:
                   await client.send_message(msgChannel, "the command " + str(commandArray) + " is missing arguments!")       
     # basic if this is said then print this command
          elif commandArray[0] == 'ping':
               # prints 'pong!'.
                await client.send_message(msgChannel, 'pong!')
          elif commandArray[0] == 'pong':
               # prints 'ping!'.
               await client.send_message(msgChannel, 'ping!')
     # let the user know that the command prefix was present but no command was found.
          else:
              await client.send_message(msgChannel, 'COMMAND NOT FOUND, CHECK SPELLING!')
     # current method for adding reactions to messages
     if '**NEW VOTE**' in charMessage:
         await client.add_reaction(message, '\U0001f170')
         await client.add_reaction(message, '\U0001f171')
# this is your unique client token! DO NOT SHARE!!!!!!!!
client.run("NDM5NTY5NzYyMDYyOTU4NjEy.DdewUA.pNIiB2XKywnZnOzx0_hN4EfBT2E")
