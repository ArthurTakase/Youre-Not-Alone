import discord #pip install discord.api
from random import randint
from random import choice
from datetime import datetime
import time

async def guess_def(message):
    msg = message.content.split(" ", 1)
    today = datetime.now()

    # [[id, 0/1],[id; 0/1]]
    f= open("files\\aventfind.txt", "r")
    fichier1 = f.read().split("\n")
    f.close()
    find = fichier1[0]
    answer_avent = fichier1[1].split("||")

    if len(msg) != 2 :
        await message.channel.send("""Tu penses avoir trouvé ce qui se cache derrière l'image ?
> **Utilisation :** !avent blabla
> **Exemple :** !avent Sanic""")

    elif find == "True" :
            #---- On a le bon nombre d'argument ----
            f = open("files\\aventuser.txt", "r")
            avent_list = f.read().split("\n")
            f.close()

            avent_id = []
            avent_all = []
            for i in range (len(avent_list)):
                avent_all.append(avent_list[i].split("|"))
                avent_id.append(avent_all[i][0])

            f = open("files\\avent.txt", "r")
            avent_list_answer = f.read().split("\n")
            f.close()

            is_in = False
            for i in range (len(avent_id)):
                if str(message.author.id) == avent_id[i] :
                    is_in = True
                    index = i

            if is_in == True : #Si on est dans la liste des utilisateurs de la commande
                role = str(message.author.roles)
                if avent_all[index][1] != str(today.day): #Si l'utilisateur n'a pas joué
                    if msg[1].lower() in answer_avent : #Si l'utilisateur a juste
                        if message.guild.id == 396081518222770176 :
                            await message.channel.send("<@!260090278541656064>, On a un vainqueur !\n Bravo {0.author.mention}, t'es vraiment très fort à ce jeu !")
                            f = open("files\\aventfind.txt", "w")
                            f.write("False")
                            f.close()
                        else :
                            role = message.guild.get_role(651154120128069656) #Snaky
                            await message.author.add_roles(role, reason="Winner of Avent Calendar", atomic=True)

                    else : #Si l'utilisateur a faux
                        if msg[1].lower() in  avent_list_answer: #Si la réponse a déjà été donnée
                            await message.channel.send("Cette réponse a déjà été donnée par un autre utilisateur.")
                        else : #Si la réponse n'a pas été donnée
                            await message.channel.send("Raté !")
                            # append la date à la liste des try
                            f = open("files\\avent.txt", "a")
                            f.write("\n" + str(msg[1]))
                            f.close()

                    avent_all[index][1] = today.day

                    #------------------------------------------------
                    #clean file
                    f1 = open("files\\aventuser.txt", "r+")
                    f1.seek(0)
                    f1.truncate()


                    for i in range (len(avent_all)) :
                        if i == 0 :
                            f1.write(str(avent_all[i][0]) + "|" + str(avent_all[i][1]))
                        else :
                            f1.write("\n" + str(avent_all[i][0]) + "|" + str(avent_all[i][1]))
                    f1.close()


                else : #Si l'utilisateur a déjà joué
                    await message.channel.send("Tu as déjà joué aujourd'hui !")
            else : #Si on est pas dans la liste
                await message.channel.send("Vous n'étiez pas dans la liste des participants au jeu :-( Mais je viens de t'ajouter !\nRefait la commande pour vérifier si tu as juste !")
                f = open("files\\aventuser.txt", "a")
                f.write("\n" + str(message.author.id) + "|0")
                f.close()
    else :
        await message.channel.send("L'image a déjà été trouvée !")

async def guesslist_def(message):
    f = open("files\\avent.txt", "r")
    avent_list = f.read().split("\n")
    f.close()

    avent_list_all = "Voici les réponses déjà données :\n"

    for i in range(len(avent_list)):
        avent_list_all += "> " + str(avent_list[i]) + "\n"

    await message.channel.send(avent_list_all)


async def guessup_def(message):
    msg = message.content.split(" ")
    today = datetime.now()

    f = open("files\\aventuser.txt", "r")
    avent_list = f.read().split("\n") #toutes les lignes ["65454654685465489|4"]
    f.close()

    avent_id = []
    avent_all = []
    for i in range (len(avent_list)):
        avent_all.append(avent_list[i].split("|")) #[[4894554468,4],[4894554468,4],[4894554468,4]]
        avent_id.append(avent_all[i][0]) #[4657487468, 48657897, 46789648996]


    for i in range (len(avent_id)):
        if str(message.author.id) == avent_id[i] :
            index = i

    if avent_all[index][1] == str(today.day) :
        answer = "Vous avez déjà joué aujourd'hui !\nProchain !avent à **minuit** !"
    else :
        answer = "Vous n'avez pas encore joué ! Alors, des idées ?"

    await message.channel.send(answer)

async def guesslaunch_def(message):
    f = open("files\\aventfind.txt", "r")
    fichier1 = f.read().split("\n")
    f.close()

    f = open("files\\aventfind.txt", "w")
    for i in range(len(fichier1)) :
        if i == 0 :
            f.write("True\n")
        else :
            f.write(fichier1[1])
    f.close()
    await message.channel.send("Guess Game en marche ! A vous de jouer !")

async def guessconfig_def(message):
    msg = message.content.split(" ", 1)

    if message.author.guild_permissions.administrator :
        if len(msg) != 2 :
            await message.channel.send("""Permet de configurer la solution du !guess ou de lancer la partie.
> **Utilisation (modifier la réponse)** : !guessconfig nom1\||nom2\||nom3\||etc...
> **Utilisation (lancer le jeu)** : !guessconfig start""")

        else :
                f = open("files\\aventfind.txt", "r+")
                read = f.read().split("\n")
                f.close()
                f = open("files\\aventfind.txt", "w")
                f.write(read[0] + "\n")
                f.write(msg[1])
                f.close()

                guess_avent = msg[1].split("||")
                message_rep = "Nouvelle(s) réponse(s) pour le jeu :"
                for i in range(len(guess_avent)) :
                    message_rep += "\n> " + guess_avent[i]

                await message.channel.send(message_rep)
