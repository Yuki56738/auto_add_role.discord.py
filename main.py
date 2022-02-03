from dotenv import load_dotenv
import os
import discord
print("Script started.")

load_dotenv()

# print(os.environ.get("DISCORD_TOKEN"))

TOKEN = os.environ.get("DISCORD_TOKEN")
ROLE = int(os.environ.get("DISCORD_VOL_ROLE"))

intents = discord.Intents.all()
intents.typing = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
@client.event
# async def on_member_join(member):
async def on_message(message):
        if str(message.channel.name) == "自己紹介記入":
            member = message.author
            print(member.name)
            role = member.guild.get_role(ROLE)
            roles_now = member.roles
            flag = 0
            for x in roles_now:
                if str(x) == "メンバー" or str(x) == "管理者":
                    print("He already has member role.")
                    flag += 1
            if flag == 0:
                    print("Adding role member...")
                    await member.add_roles(role)
                    print("Added role.")

client.run(TOKEN)

