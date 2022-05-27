#Import discord module
from discord.ext import commands

#Call command on discord using!
bot = commands.Bot(command_prefix='!')

#Add external server host
bot.lava_nodes = [
    {
        'host':'lava.link',
        'port':'80',
        'rest_uri':f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'singapore'
    }
]

#Create an instance of a bot that handles even and establishes connection
@bot.event
async def on_ready():
    print('Bot is ready to play music. ')
    bot.load_extension('dismusic')
    for guild in client.guilds: #Loop through the guild data that discord has sent bot func
        if guild.name == GUILD:
            break
#Print the following guild data
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

#Discord key for server
bot.run('Put discord key in here')
