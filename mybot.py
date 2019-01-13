import discord

from discord import Game

badWords = ["owo", "uwu", "arf", "woof", "purr", "meow", "howl", "awoo", "aroo", "fursuit", "murrsuit", "bad dragon", "good boy", "good boye", "dawg", "merp", "sergal", "after dark", "knot", "lewd", "yiff", "canine", "equine", "femboi fox", "femboy fox", "chee", "paws", "maws", "belly", "belly rub", "arcanine", "FA", "furaffinity", "e621", "collar", "leash", "whine", "rp", "roleplay", "role play", "cub", "pups", "cubs", "roo", "waff", "scalie", "scalies", "folf", "werewolf", "housepets!", "housepets", "dobe", "daddy", "bulge", "anthrocon", "mff", "flop"]
\\         ["1  ", "1  ", "1  ", "2   ", "3   ", "2   ", "3   ", "4   ", "4   ", "3      ", "4       ", "4         ", "3       ", "4        ", "2   ", "3   ", "3     ", "3         ", "4   ", "4   ", "4   ", "2     ", "2     ", "4         ", "4         ", "3   ", "3   ", "4   ", "3    ", "4        ", "3       ", "4 ", "4          ", "4   ", "2     ", "3    ", "3    ", "4 ", "4       ", "4        ", "2  ", "2   ", "2   ", "3  ", "2   ", "3     ", "4      ", "3   ", "2       ", "3         ", "3        ", "3   ", "3    ", "4    ", "4        ", "4  ", "3   "]

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    server = message.server
    author = message.author


    
    if 'owo' in message.content.lower() or 'uwu' in message.content.lower() or 'arf' in message.content.lower() or ':owo:' in message.content.lower():
        msg = ':red_circle::red_circle:  STOP YOU DEGENERATE :red_circle::red_circle:  {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="lvl1 furry")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="lvl1 furry")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "You are a :fox: {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to add roles.")


    if 'Yiff' in message.content.lower() or 'Paw' in message.content.lower() or 'aroo' in message.content.lower() or 'sergal' in message.content.lower():
        msg = ':red_circle::red_circle: NO THATS BAD FOR YOUR HEALTH :red_circle::red_circle: {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="lvl2 furry")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="lvl2 furry")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "You are a :fox: {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to add roles.")


    if ('fursuit') in message.content.lower():
        msg = ':red_circle::red_circle: Fur=Bad :red_circle::red_circle: {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="lvl3 furry")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="lvl3 furry")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "You are a :fox: {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to add roles.")

    if ('murrsuit') in message.content.lower():
        msg = ':red_circle::red_circle: GET THE HEAVY ARTILARY WE HAVE A MEGA FURRY :red_circle::red_circle: {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="lvl4 furry")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="lvl4 furry")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "You are a :fox: {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to add roles.")

    if (';-;') in message.content.lower():
        msg = 'NO JUST STOP YOU FURRY {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="FURRY")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="FURRY")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to add roles.")

    if ('!remove1') in message.content.lower():
        msg = 'Fine But no more goddam OWOing {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="lvl1 furry")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="lvl1 furry")
            await client.remove_roles(message.author, role)
            await client.send_message(message.channel, "Successfully removed {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to remove roles.")

    if ('!remove2') in message.content.lower():
        msg = 'Fine But no more goddam OWOing {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="lvl2 furry")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="lvl2 furry")
            await client.remove_roles(message.author, role)
            await client.send_message(message.channel, "Successfully removed {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to remove roles.")

    if ('!remove3') in message.content.lower():
        msg = 'Fine But no more goddam OWOing {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="lvl3 furry")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="lvl3 furry")
            await client.remove_roles(message.author, role)
            await client.send_message(message.channel, "Successfully removed {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to remove roles.")

    if ('!remove4') in message.content.lower():
        msg = 'Fine But no more goddam OWOing {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="lvl4 furry")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="lvl4 furry")
            await client.remove_roles(message.author, role)
            await client.send_message(message.channel, "Successfully removed {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to remove roles.")
@client.event
async def on_ready():
    await client.change_presence(game=Game (name="furry hunting simulator 2018"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTI5MTIyNjgzNTUyNzkyNTc5.DxwraQ.89ugi59GdLQYV0RxymcV-g5KCdY')