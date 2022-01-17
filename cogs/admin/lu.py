import discord
from discord.ext import commands
from discord.ui import Button, View





#pip install git+https://github.com/Rapptz/discord.py


class LU(commands.Cog):
    '''Help command'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        await ctx.send('Succesfully been enabled!')
        self.bot.load_extension(f'cogs.{extension}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        await ctx.send('Succesfully been disabled!')
        self.bot.unload_extension(f'cogs.{extension}')

        


def setup(bot):
    bot.add_cog(LU(bot))
    print("Admin | load / unload is enabled!")