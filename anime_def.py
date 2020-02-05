import discord #pip install discord.api
from random import randint
from random import choice
from mal import Anime #import Anime #pip install mal-api
from mal import Manga
from math import sqrt

async def random_anime_def(message):
    while 1 :
        try :
            number_anime = randint(0, 25000)
            anime = Anime(number_anime)
            await message.channel.send("Si tu sais pas quoi faire, tu peux regarder :\nhttps://myanimelist.net/anime/" + str(number_anime))
            break
        except :
            print(number_anime, "error anime")
            continue

async def random_manga_def(message):
    while 1 :
        try :
            number_manga = randint(0, 25000)
            manga = Manga(number_manga)
            await message.channel.send("Si tu sais pas quoi faire, tu peux lire :\nhttps://myanimelist.net/manga/" + str(number_manga))
            break
        except :
            print(number_manga, "error manga")
            continue

async def good_anime_def(message):
    #----------------------------------
    f = open("files\\anime.txt", "r")
    good_anime = f.read().split("\n")

    f.close()
    #----------------------------------
    anime = choice(good_anime)

    good_anime_user = anime.split("|", 1)
    answer = "**" + str(good_anime_user[0]) + "** te recommande de regarder : \n> " + str(good_anime_user[1])

    #author = str(message.author)
    #author_msg = author.split("#")

    #answer = "**" + str(author_msg[0]) + "** te recommande de regarder **" + str(good_anime_user[1]) + "**"
    await message.channel.send(answer)

async def add_anime_def(message):
    msg = message.content.split(" ", 1)

    if len(msg) != 2 :
        await message.channel.send("""Ajoute un anime à la base de donnée de !goodanime.
> **Utilisation :** !addanime nom
> **Exemple :** !addanime Evangelion""")

    else :
        author = str(message.author)
        if "|" in author :
            await message.channel.send("Pour utiliser cette commande, veuillez changer de pseudo Discord.")
        else :
            author_msg = author.split("#")

            # append la date à la liste des anniversaires
            f = open("files\\anime.txt", "a")
            f.write("\n" + author_msg[0] + "|" + str(msg[1]))
            await message.channel.send("Anime enregistré au nom de {author} !".format(message, author = author_msg[0]))


async def remove_anime_def(message):
    msg = message.content.split(" ", 1)
    if len(msg) != 2 :
        await message.channel.send("""Enlève un anime de la base de donnée de !goodanime
> **Utilisation :** !removeanime nom
> **Exemple :** !removeanime Evangelion""")

    else :
        #--------------- lecture fichier ----------------

        f = open("files\\anime.txt", "r")
        good_anime = f.read().split("\n")
        f.close()
        #good_anime.remove(good_anime[-1])

        #------------------------------------------------
        msg = message.content.split(" ", 1)
        good_anime_all = []
        anime_list = []

        for i in range(len(good_anime)):
            animeI = good_anime[i].split("|", 1)
            good_anime_all.append(animeI)
            anime_list.append(good_anime_all[i][1])

        if msg[1] in anime_list :
            for i in range(len(good_anime_all)):
                if good_anime_all[i][1] == msg[1]:
                    good_anime_all.remove(good_anime_all[i])
                    break

            #------------------------------------------------
            #clean file
            f1 = open("files\\anime.txt", "r+")
            f1.seek(0)
            f1.truncate()


            for j in range (len(good_anime_all)) :
                #f.write("\n" + author_msg[0] + "|" + str(msg[1]))
                if j == 0 :
                    f1.write(str(good_anime_all[j][0]) + "|" + str(good_anime_all[j][1]))
                else :
                    f1.write("\n" + str(good_anime_all[j][0]) + "|" + str(good_anime_all[j][1]))
            f1.close()

            await message.channel.send("Anime supprimé !".format(message))
            #------------------------------------------------
        else :
            await message.channel.send("Aucun anime trouvé pour ce nom".format(message))

async def all_anime_def(message):
    #--------------- lecture fichier ----------------

    f = open("files\\anime.txt", "r")
    good_anime = f.read().split("\n")
    f.close()

    msg = message.content.split(" ", 1)
    good_anime_all = []
    anime_list = "Voici les animes conseilés par les utilisateurs :\n"

    for i in range(len(good_anime)):
        animeI = good_anime[i].split("|", 1)
        good_anime_all.append(animeI)
        anime_list += "> **" + str(good_anime_all[i][1]) + "** - " + str(good_anime_all[i][0]) + "\n"

    await message.channel.send(anime_list)
