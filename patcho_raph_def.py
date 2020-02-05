import discord #pip install discord.api
from random import randint
from random import choice
from datetime import datetime
import time

async def patcho_def(message):
    msg = message.content.split(" ", 1)

    if len(msg) != 2 : #Pas assez d'arguments
        await message.channel.send("""Compteurs pour les problèmes de Patcho.
> **!patcho raph** -> ajoute 1 au compteur `séparation des deux amoureux`.
> **!patcho cul** -> ajoute 1 au compteur `viens benji on parle de cul`.
> **!patcho pecho** -> ajoute 1 au compteur `bisous bisous raph`.
> **!patcho all** -> permet de voir la perversion de Benji.""")
    else :
        f = open("files\\patcho.txt", "r", encoding="utf-8")
        patcho_line = f.read().split("\n")
        f.close()

        patcho_raph = patcho_line[0].split("|")
        patcho_cul = patcho_line[1].split("|")
        patcho_couple = patcho_line[2].split("|")

        if msg[1] == "pecho": #ajoute un au compteur mise en couple
            patcho_couple[1] = str(int(patcho_couple[1]) + 1)

            f1 = open("files\\patcho.txt", "r+", encoding="utf-8")
            f1.seek(0)
            f1.truncate()

            f1.write(patcho_raph[0] + "|" + patcho_raph[1] + "\n")
            f1.write(patcho_cul[0] + "|" + patcho_cul[1] + "\n")
            f1.write(patcho_couple[0] + "|" + patcho_couple[1])

            await message.channel.send("""Ca fait déjà **{nbr} fois** que <@!282942845361324032> pécho Raph.
Il faudrait faire une fanfic...""".format(message, nbr = patcho_couple[1]))

        elif msg[1] == "raph" : #ajouter 1 au compteur séparation
            patcho_raph[1] = str(int(patcho_raph[1]) + 1)

            f1 = open("files\\patcho.txt", "r+", encoding="utf-8")
            f1.seek(0)
            f1.truncate()

            f1.write(patcho_raph[0] + "|" + patcho_raph[1] + "\n")
            f1.write(patcho_cul[0] + "|" + patcho_cul[1] + "\n")
            f1.write(patcho_couple[0] + "|" + patcho_couple[1])

            await message.channel.send("""Ca fait déjà **{nbr} fois** que <@!282942845361324032> est mentionné pour **une rupture avec Raph**.
Il serait temps de savoir bordel !""".format(message, nbr = patcho_raph[1]))


        elif msg[1] == "cul" : #ajouter 1 à la liste cul
            patcho_cul[1] = str(int(patcho_cul[1]) + 1)

            f1 = open("files\\patcho.txt", "r+", encoding="utf-8")
            f1.seek(0)
            f1.truncate()

            f1.write(patcho_raph[0] + "|" + patcho_raph[1] + "\n")
            f1.write(patcho_cul[0] + "|" + patcho_cul[1] + "\n")
            f1.write(patcho_couple[0] + "|" + patcho_couple[1])

            await message.channel.send("""Ca fait déjà **{nbr} fois** que <@!282942845361324032> est mentionné pour **du cul**.
Ce petit perver !""".format(message, nbr = patcho_cul[1]))

        elif msg[1] == "all" :
            await message.channel.send("""Voici les stats de Benji, ce petit coquin :
> **Sexe** : {sexe}
> **Rupture** : {raph}
> **Couple** : {couple}""".format(message, sexe = patcho_cul[1], raph = patcho_raph[1], couple = patcho_couple[1]))

        else :
            await message.channel.send("""Compteurs pour les problèmes de Patcho.
> **!patcho raph** -> ajoute 1 au compteur 'séparation' des deux amoureux.
> **!patcho cul** -> ajoute 1 au compyeur 'Vins benji on parle de cul'.""")
