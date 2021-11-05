import discord

client = discord.Client()

@client.event
async def on_ready():
    # De bot kan op veel verschillende servers draaien. Met deze regel code pak je de eerste server die deze bot heeft. Als jouw bot maar 1 server heeft is het makkelijk.
    guild = client.guilds[0]
    # De naam van de server printen we gelijk uit.
    print(guild.name, "is de naam van de server!")

    # We printen de naam van de bot user uit.
    print(client.user, "is verbonden met de client")

    channel = guild.text_channels[0]
    print(channel.name, "is de naam van het kanaal!")
    await channel.send("Ik ben aanwezig!")

@client.event
async def on_message(message):
    print(message.channel.name, "Het bericht is geplaats vanaf dit kanaal.")
    print(message.content)
    print(message.author,"is de persoon die het bericht schreef.")
    print(message.created_at,"is het moment dat het bericht geplaatst is.")
    print(message.channel,"is het kanaal waar het bericht geplaatst is.")

    await message.channel.send("Hallo " + message.author)
    if message.author.bot == False:
        message.channel.send





client.run("")