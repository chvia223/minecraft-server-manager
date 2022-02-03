import discord
import time
import requests

client = discord.Client()

def start():
    # Insert VM start endpoint
    url = ""

    res = requests.get(url)

    return res.status_code

def stop():
    # Insert VM stop endpoint
    url = ""

    res = requests.get(url)

    return res.status_code

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$serverbot'):
        if message.content.startswith('$serverbot -list'):
            await message.channel.send('Here is a list of servers we have available:\n\n'
                                       '   -Minecraft Paper 1.16.6 @ "$paper"')
        elif message.content.startswith('$serverbot -help'):
            await message.channel.send('Here are the general serverbot commands:\n\n'
                                       '   "$serverbot -list" --- Lists available servers to choose from\n'
                                       '   "$serverbot -help" --- Lists available general serverbot commands\n\n'
                                       'To interact with a server use the "$" with its given name. You can see the name in the list command.\n'
                                       'For example:\n\n'
                                       '   "$paper" --- will list available commands for the spigot server')
        else:
            await message.channel.send("Hi! I'm ServerAssitantBot. I'm here to help you interact with and play on the dedicated game servers that we host.\n\n"
                                       'For a list of my available commands type "$serverbot -help"')


    if message.content.startswith('$paper'):
        if message.content.startswith('$paper -start'):
            await message.channel.send('The server is starting. I will be unavailable to take commands for the next 30 seconds while I help start the spigot server. ' 
                                       'I apologize for the inconvenience.')
            status_code_enter = start()
            if status_code_enter == 200:
                time.sleep(30)
                await message.channel.send('\nThe server has been initialized successfully.\n\n'
                                           'The ip address is: cvm-boyz.ddns.net\n\n'
                                           'This server also has a Dynmap that can be accessed in your browser @ cvm-boyz.ddns.net:8123\n\n'
                                           'Enjoy!')
            else:
                await message.channel.send('There was a problem starting the server. You should contact Christian and let him know so he can fix the issue.')
        elif message.content.startswith('$paper -stop'):
            status_code_exit = stop()
            if status_code_exit == 200:
                await message.channel.send('The server is stopping. I hope you had a fun time playing!')
            else:
                await message.channel.send('There was a problem shutting the server down. You should contact Christian and let him know so he can fix the issue.')
        else:
            await message.channel.send('That is not a valid spigot command. Below is a list of valid commands:\n\n'
                                       '   "$paper -start" --- Will start the Minecraft Spigot server\n'
                                       '   "$paper -stop" --- Will stop the Minecraft Spigot server\n')

# Insert Client Token
client.run('')