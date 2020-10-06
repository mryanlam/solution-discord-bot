import discord

client = discord.Client()

guest_role_id = 762854964166787093

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    # Assigns role on join
    guest_role = member.guild.get_role(guest_role_id)
    await member.add_roles(guest_role_id, reason="Guest User")

def get_credentials():
    with open("config.txt") as f:
        return f.readline()

client.run(get_credentials())