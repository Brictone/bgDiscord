#! /usr/bin/python3.7

# discord bot to do things that otherwise would require a human.
# some ideas would be to create a badge system
#    Interactive Jukebox
#    in Game discord interaction
#    Connect Jira or other to discord for task tracking and collaboration
#    many other things fun things.

# initially I just labeled this as bgDiscord out of a lack of a better name.
# Ultimately I'm not really sure what I want to do with this yet.
# Also Classes infuriate me. >:|

# requirements
# python3 -m pip install -U discord.py
# or python3 -m pip install -U discord.py[voice]
#    apt install libffi-dev libnacl-dev python3-dev

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('my token goes here')
