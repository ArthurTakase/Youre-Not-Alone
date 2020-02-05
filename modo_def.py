import discord #pip install discord.api
from random import randint
from random import choice
from datetime import datetime
import time

async def clear_def(message):
    if message.author.guild_permissions.administrator: #@&396396443000373248
        msg = message.content.split(" ")

        if len(msg) == 2:
            try :
                limit_clear = int(msg[1]) + 1
                await message.channel.purge(limit=limit_clear)
                #await message.channel.send("Les messages ont été effacés !")
                bot_msg = await message.channel.send("Les messages ont été effacés !")
                await bot_msg.delete(delay = 4)
            except :
                await message.channel.send("Alors, heuu, comment tu veux que je supprime {msg} messages ?".format(message, msg = msg[1]))
        else :
            await message.channel.send("Veuillez mettre un chiffre après le !clear")

    else :
        await message.channel.send("T'as pas le droit nananère !")

async def banword_def(message):
    global banned_msgs
    if message.author.guild_permissions.administrator :

        f = open("files\\ban.txt", "r", encoding="utf-8")
        banned_msgs = f.read().split("\n")
        f.close()

        msg = message.content.split()

        if len(msg) != 2 :
            await message.channel.send("""Ajouter un mot à bannir.
> **Utilisation :** !banword msg""")
        else :
            f = open("files\\ban.txt", "a", encoding="utf-8")
            f.write("\n" + str(msg[1]))
            f.close()

            banned_msgs.append(msg[1])

            await message.channel.send("Mot enregistré !")
    else :
        await message.channel.send("Tu n'as pas les droits !")

async def banuser_def(message):
    msg = message.content.split()

    if len(msg) == 2 and msg[1] == "all" :
        f = open("files\\banuser.txt", "r", encoding="utf-8")
        banned_user = f.read().split("\n")
        f.close()

        answer = "Les utilisateurs bannis sont :"
        for i in range (len(banned_user)) :
            if i != 0 :
                answer += "\n> <@" + banned_user[i] +">"

        await message.channel.send(answer)

    elif message.author.guild_permissions.administrator:

        f = open("files\\banuser.txt", "r", encoding="utf-8")
        banned_user = f.read().split("\n")
        f.close()

        if len(msg) != 2 :
            await message.channel.send("""Ajouter un utilisateur à bannir.
    > **Utilisation :** !banuser user_id""")

        else :
            try :
                member = message.guild.get_member(int(msg[1]))
                if member != None and msg[1] != "260090278541656064":
                    f = open("Bar_files\\banuser.txt", "a", encoding="utf-8")
                    f.write("\n" + msg[1])
                    f.close()
                    await message.channel.send("Utilisateur enregistré !")
                else :
                    await message.channel.send("Veuillez entrer l'ID d'un membre du serveur.")
            except :
                await message.channel.send("Veuillez entrer un ID.")
            #else :
                #await message.channel.send("Veuillez entrer un ID.")
    else :
        await message.channel.send("Tu n'as pas les droits ! Par contre tu peux voir la liste des utilisateurs bannis avec la commande !banuser all.")

async def banlist_def(message):
    f = open("files\\ban.txt", "r", encoding="utf-8")
    banned_msgs = f.read().split("\n")
    f.close()

    retour = "Les mots bannis sont :"

    for i in range(len(banned_msgs)) :
        retour += "\n> **" + str(banned_msgs[i]) + "**"

    await message.channel.send(retour)

async def unbanword_def(message):
    #global banned_msgs
    msg = message.content.split()
    if message.author.guild_permissions.administrator :
        if len(msg) != 2 :
            await message.channel.send("""Permet de supprimer un mot de la liste des mots bannis.
> **Utilisation :** !unbanword blabla""")
        else :
            if msg[1] in banned_msgs :
                f1 = open("files\\ban.txt", "r+", encoding="utf-8")
                all_banned_msgs = f1.read().split("\n")
                f1.close()
                all_banned_msgs.remove(msg[1])

                #------------------------------------------------
                f1 = open("files\\ban.txt", "r+", encoding="utf-8")
                f1.seek(0)
                f1.truncate()


                for j in range (len(all_banned_msgs)) :
                    #f.write("\n" + author_msg[0] + "|" + str(msg[1]))
                    if j == 0 :
                        f1.write(all_banned_msgs[j])
                    else :
                        f1.write("\n" + all_banned_msgs[j])
                f1.close()

                await message.channel.send("Mot supprimé !".format(message))
    else :
        await message.channel.send("Tu n'as pas les droits !")
