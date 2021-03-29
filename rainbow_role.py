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
from asyncio import sleep
import random

serverid = 793839120643522600
rainbowrolename = "Special"
delay = 0.5
colours = {
    "red": 0xf16f6,
    "blue": 0x676f1,
    "yellow": 0xf1e86f,
    "purple": 0x9f6ff1,
    "green": 0x6ff17e,
    "cyan": 0x6feff1
}


class Rainbow(commands.Cog):
    members = []
    counter = 0

    def __init__(self, bot):
        self.client = bot
        self.delay = delay

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.loop.create_task(self.change_role())

    @commands.command(aliases=["rainbow", "rb"])
    @commands.is_owner()
    async def rainbowrole(self, ctx, member: discord.Member):
        await self.client.wait_until_ready()

        guild = ctx.guild
        special_role = discord.utils.get(guild.roles, name=rainbowrolename)

        if not special_role:
            special_role = await guild.create_role(name=rainbowrolename)

        self.members.append(member)
        await member.add_roles(special_role, reason="You got my favorite role")
        await ctx.send(f"Lucky, {member.mention} you got a special role")
        await member.send(f"You got a special role x)")

    @commands.is_owner()
    @commands.command()
    async def rbt(self, ctx, time: int):
        self.delay = int(time)

    async def change_role(self):
        await self.client.wait_until_ready()
        server = self.client.get_guild(serverid)

        while not self.client.is_closed():
            for role in server.roles:
                if role.name == rainbowrolename and self.members:
                    # What you want to do.
                    await role.edit(
                        colour=discord.Colour(list(colours.values())[self.counter]))
                    if self.counter == 4:
                        self.counter = 0
                    else:
                        self.counter += 1
                    break

            await sleep(self.delay)


def setup(client):
    client.add_cog(Rainbow(client))
