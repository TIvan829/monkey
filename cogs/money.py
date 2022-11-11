import discord,json,os
from discord.ext import commands
from discord.commands import Option
from discord.commands import slash_command

with open("config.json","r",encoding="utf-8") as file:
    data=json.load(file)

class money(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @slash_command(description="查看背包",guild_ids=[985723834516791316])
    async def money(self,ctx,user:Option(discord.User,"要看的用戶",required=False)):
        pass #編寫中

def setup (bot):
    bot.add_cog(money(bot))
