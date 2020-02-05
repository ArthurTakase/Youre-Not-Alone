TOKEN = #Votre Token ici

import discord #pip install discord.api
from random import randint
from random import choice
from imgurpython import ImgurClient #pip install imgurpython
import imgurpython
from datetime import datetime
import time
from mal import Anime #import Anime #pip install mal-api
from mal import Manga
from math import sqrt
from imgur_def import *
from update_def import *
from birth_def import *
from misc_def import *
from anime_def import *
from author_def import *
from modo_def import *
from guess_def import *
from patcho_raph_def import *


birthday = []
f = open("files\\birthday.txt", "r+")
birthday1 = f.read().split(";\n")

for i in range(len(birthday1) - 1):
    birthday.append(birthday1[i].split(" ", 2))

f = open("files\\ban.txt", "r", encoding="utf-8")
banned_msgs = f.read().split("\n")
f.close()

#-------------------------------------------------------------------------------

again = True

class MyClient(discord.Client):

    global birthday, banned_msgs

    # Fonction qui permet de voir si le bot est lancé. S'execute au démarrage
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name) #print son nom "You're (not) a Bot"
        print(self.user.id) #print son id "638122881376583692"
        print('------')

        await client_discord.change_presence(status=discord.Status.idle, activity=discord.Game("type !help"))

    async def on_member_join(self, member):
        if member.guild.id == 396081518222770176 :
            role = member.guild.get_role(423454978930245632) #LeBar
            await member.add_roles(role, reason=None, atomic=True)
            await member.send("""Bonsoir ! Bienvenue sur Le Bar !
N'oublis pas d'aller lire les règles dans #⚠-regles-et-news-⚠ et de te présenter dans #presentation pour avoir accès à tout le serveur !
Si tu as des demandes particulières, tu peux faire appel à un modérateur.""".format(member.mention))


    async def on_message(self, message):
        try :
            # we do not want the bot to reply to itself
            if message.author.id == self.user.id: # Si c'est le bot qui aprle juste avant ça fait rien
                return
            else :
                command_id = message.content.split(" ", 1)

            if command_id[0] =='!duck':
                await duck(message)

            if command_id[0] == '!image':
                await image(message)

            if command_id[0] == '!patch' :
                await patch(message)

            if command_id[0] == "!help" :
                await help_def(message)

            if command_id[0] == '!birth':
                await birth(message, 0, again)
            else :
                await birth(message, 1, again)

            if command_id[0] == '!addbirth':
                await add_birth(message)

            if command_id[0] == '!allbirth':
                await all_birth(message)

            if command_id[0] == '!databirth':
                await data_birth(message)

            if command_id[0] == '!removebirth':
                await remove_birth(message)

            if command_id[0] == '!russian':
                await russian_def(message)

            if command_id[0] == "!coin" :
                await coin_def(message)

            if command_id[0] == '!randomanime':
                await randon_anime_def(message)

            if command_id[0] == '!randommanga':
                await random_manga_def(message)

            if command_id[0] == "!goodanime" :
                await good_anime_def(message)

            if command_id[0] == '!addanime':
                await add_anime_def(message)

            if command_id[0] == '!removeanime':
                await remove_anime_def(message)

            if command_id[0] == '!allanime' :
                await all_anime_def(message)

            if command_id[0] == '!dev':
                await dev_def(message)

            if command_id[0] == '!devlist' :
                await devlist_def(message)

            if command_id[0] == '!clear':
                await clear_def(message)

            if command_id[0] == "!guess" :
                await guess_def(message)

            if command_id[0] == '!guesslist' :
                await guesslist_def(message)

            if command_id[0] == "!guessup" :
                await guessup_def(message)

            if command_id[0] == "!guesslaunch" :
                await guesslaunch_def(mesage)

            if command_id[0] == "!guessconfig" :
                await guessconfig_def(message)

            if command_id[0] == "!solve" :
                await solve_def(message)

            if command_id[0] == "!patcho" :
                await patcho_def(message)

            if command_id[0] == "!banword" :
                await banword_def(message)

            if any(msg in message.content.lower() for msg in banned_msgs):

                f = open("files\\banuser.txt", "r", encoding="utf-8")
                banned_user_str = f.read().split("\n")
                f.close()

                banned_user = []
                for i in range (len(banned_user_str)):
                    banned_user.append(int(banned_user_str[i]))

                if message.author.id in banned_user and not message.content.startswith("!banword") and not message.content.startswith("!unbanword"):
                    await message.delete()
                    loli_msg = await message.channel.send("Vous avez utilisé un mot interdit, petit coquin !")
                    await loli_msg.delete(delay = 4)

            if command_id[0] == "!banuser" :
                await banuser_def(message)

            if command_id[0] == "!banlist" :
                await banlist_def(message)

            if command_id[0] == "!unbanword" :
                await unbanword_def(message)

        except Exception as e :
            await message.channel.send(e)

client_discord = MyClient()
client_discord.run(TOKEN)
