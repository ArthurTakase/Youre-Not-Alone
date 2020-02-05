import discord #pip install discord.api
from random import randint
from random import choice
from datetime import datetime
import time

async def birth(message, type, again):
    today = datetime.now()
    #------------------------------------------------
    birthday = []

    f = open("files\\birthday.txt", "r")
    birthday1 = f.read().split(";\n")

    for i in range(len(birthday1) - 1):
        birthday.append(birthday1[i].split(" ", 2))
    #------------------------------------------------

    x = True
    if type == 0 :
        for i in range (len(birthday)) :
            if int(birthday[i][0]) == today.day and int(birthday[i][1]) == today.month :
                x = False
                await message.channel.send("C'est l'anniversaire de **{user}** aujourd'hui !\nhttps://media.giphy.com/media/3oEhn78T277GKAq6Gc/giphy.gif".format(message, user = birthday[i][2]))

        if x == True :
            await message.channel.send("Il n'y a pas d'anniversaire aujourd'hui !".format(message))
    elif type == 1 :
        if today.hour == 0 and today.minute == 0 :
            again = True

        if again == True :
            for i in range (len(birthday)) :
                if int(birthday[i][0]) == today.day and int(birthday[i][1]) == today.month :
                    x = False
                    await message.channel.send("C'est l'anniversaire de **{user}** aujourd'hui !\nhttps://media.giphy.com/media/3oEhn78T277GKAq6Gc/giphy.gif".format(message, user = birthday[i][2]))
                    again = False

async def add_birth(message):
    msg = message.content.split(" ", 3)

    # regarde si le message fait la bonne longueur et help l'utilisateur
    if len(msg) == 1 or len(msg) == 2 or len(msg) == 3:
        await message.channel.send("""Pour ajouter une date d'anniversaire, faites la commande de cette manière :
> **Utilisation :** !addbirth jour mois nom
> **Exemple :** !addbirth 10 4 Arthur -> Arthur a son anniversaire le 10 avril.""")

    elif msg[1].startswith("0") or msg[2].startswith("0"):
        await message.channel.send("Merci de ne pas mettre de 0 devant un numéro")

    # append la date à la liste des anniversaires
    else :
        f = open("files\\birthday.txt", "a")
        #birthday.append([int(msg[1]), int(msg[2]), msg[3]])
        f.write(str(msg[1]) + " " + str(msg[2]) + " " + str(msg[3]) + ";\n")
        await message.channel.send("Date enregistrée !".format(message))

async def all_birth(message):
    #------------------------------------------------
    birthday = []

    f = open("files\\birthday.txt", "r")
    birthday1 = f.read().split(";\n")

    for i in range(len(birthday1) - 1):
        birthday.append(birthday1[i].split(" ", 2))
    #------------------------------------------------

    birth = "Je connais les anniversaires de plein de monde !\n"
    if len(birthday) == 0:
         await message.channel.send("Je ne connais pas encore de dates. Vous pouvez en ajouter avec la commande !addbirth".format(message))
    else :
        for i in range (len(birthday)):
            birth += "> **{u}** - {d}/{m}\n".format(message, d = birthday[i][0], m = birthday[i][1], u = birthday[i][2])
        await message.channel.send(birth)

async def data_birth(message):
    #------------------------------------------------
    birthday = []

    f = open("files\\birthday.txt", "r")
    birthday1 = f.read().split(";\n")

    for i in range(len(birthday1) - 1):
        birthday.append(birthday1[i].split(" ", 2))
    #------------------------------------------------

    await message.channel.send("{d}".format(message, d = birthday))

async def remove_birth(message):
    #--------------- lecture fichier ----------------
    birthday = []

    f = open("files\\birthday.txt", "r")
    birthday1 = f.read().split(";\n")

    for i in range(len(birthday1) - 1):
        birthday.append(birthday1[i].split(" ", 2))
    f.close()
    #------------------------------------------------

    msg = message.content.split(" ", 1)

    if len(msg) == 1 :
        await message.channel.send("Pour supprimer une date d'anniversaire, faites la commande de cette manière :\n> !removebirth nom".format(message))

    name = []
    for i in range(len(birthday)):
        name.append(birthday[i][2])

    if msg[1] in name :
        for i in range(len(birthday)):
            if birthday[i][2] == msg[1]:
                birthday.remove([birthday[i][0], birthday[i][1], birthday[i][2]])
                break

        #------------------------------------------------
        #clean file
        f1 = open("files\\birthday.txt", "r+")
        f1.seek(0)
        f1.truncate()

        for j in range (len(birthday)) :
            f1.write(str(birthday[j][0]) + " " + str(birthday[j][1]) + " " + str(birthday[j][2]) + ";\n")
        f1.close()

        await message.channel.send("Anniversaire supprimé !".format(message))
        #------------------------------------------------
    else :
        await message.channel.send("Aucun anniversaire trouvé pour ce nom".format(message))
