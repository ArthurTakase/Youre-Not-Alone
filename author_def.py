import discord #pip install discord.api
from random import randint
from random import choice
from datetime import datetime
import time

async def dev_def(message) :
    msg = message.content.split(" ", 1)

    if len(msg) != 2 :
        await message.channel.send("""Pour faire passer des infos au dev (idées de commandes, rapport de bug, etc...).
> **Utilisation :** !dev blabla
> **Exemple :** !dev commande pour une image de chat""")

    else :
        author = str(message.author)
        if "|" in author :
            await message.channel.send("Pour utiliser cette commande, veuillez changer de pseudo Discord.")
        else :
            author_msg = author.split("#")

        # append la date à la liste des anniversaires
        f = open("files\\idea.txt", "a")
        f.write("\n" + author_msg[0] + "|" + str(msg[1]))
        await message.channel.send("Rapport envoyé avec succès !".format(message))

async def devlist_def(message):
    f = open("files\\idea.txt", "r")
    dev_list = f.read().split("\n")
    f.close()
    dev_list.remove(dev_list[0])

    dev_idea = "Voici les retours des utilisateurs :\n"

    if len(dev_list) == 0 :
        await message.channel.send("Ce serveur n'a fait aucun retour.")
    else :
        dev_last = []
        for i in range(len(dev_list)):
            dev_all = dev_list[i].split("|", 1)
            dev_last.append(dev_all)

            dev_idea += "> " + str(dev_last[i][1]) + " - **" + str(dev_last[i][0]) + "**\n"

        await message.channel.send(dev_idea)
