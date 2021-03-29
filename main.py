################################################################################
# Copyright (c) 2021 JagTheFriend
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

import discord
from discord.ext import commands


client = commands.Bot(command_prefix="%")  # can be changed 

# to see whether the bot is running or not
@client.event
async def on_ready():
    '''shows that the bot is working'''
    print("\n\nIts working !!\n\n")

@client.event
async def on_message(message):
    '''prints out what was typed'''
    print("Someone sent a message")
    await client.process_commands(message)

if __name__ == '__main__':
    client.load_extension("")    
    # loading the tokens
    TOKEN = os.environ.get("TOKEN")
    client.run(TOKEN)
