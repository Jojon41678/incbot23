import discord




client = discord.Client()



@client.event

async def on_message(message):

    # we do not want the bot to reply to itself

    if message.author == client.user:

        return



    if message.content.startswith('!clanbewerbung'):

        msg = 'Sende deine Stats per Link von Tracker Network in #trackerlink oder sende coole clips von dir in #clips {0.author.mention}'.format(message)

        await client.send_message(message.channel, msg)
    elif message.content.startswith('!modbewerbung'):

        msg = 'Sende eine vollständige Bewerbung in #modbewerbung; Inhalt könnt ihr  in #modbewerbungen finden! {0.author.mention}' .format(message)

        await client.send_message(message.channel, msg)

    elif message.content.startswith('!befehle'):

        msg = '!clanbewerbung , !modbewerbung {0.author.mention}'.format(message)

        await client.send_message(message.channel, msg)     

     



@client.event

async def on_ready():

    print('Logged in as')

    print(client.user.name)

    print(client.user.id)

    print('------')



client.run('NTUxNzE4MTE2NTA2MjA2MjIx.D17f9w.D-u0U_rV5tKl6GWtpbuFCjkYvoE')
