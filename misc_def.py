import discord #pip install discord.api
from random import randint
from random import choice
from datetime import datetime
import time

russian = ["Fire !", "Pouf", "Pouf", "Pouf", "Pouf", "Pouf"]

async def russian_def(message):
    global russian
    gun = choice(russian)

    if gun == "Fire !" :
        await message.channel.send("{x} 🔫 On se revoit en enfer {0.author.mention}.".format(message, x = gun))

        russian = ["Fire !", "Pouf", "Pouf", "Pouf", "Pouf", "Pouf"]

        await message.channel.send("Aux suivants...".format(message))

    else :
        russian.remove(gun)
        if len(russian) == 5 :
            await message.channel.send("{x} 🤠 Vous avez la vie sauve {0.author.mention} (cela fait {mun} tir à blancs).".format(message, x = gun, mun = 6 + (0 - len(russian))))
        else :
            await message.channel.send("{x} 🤠 Vous avez la vie sauve {0.author.mention} (cela fait {mun} tirs à blancs).".format(message, x = gun, mun = 6 + (0 - len(russian))))

async def coin_def(message):
    coin = ["PILE", "FACE"]

    await message.channel.send("Attention, je lance une pièce.")
    time.sleep(2)
    await message.channel.send("Roulement de tambour...")
    time.sleep(2)
    await message.channel.send("ET C'EST {x} ! {0.author.mention}".format(message, x = choice(coin)))

async def solve_def(message):
    msg = message.content.split(" ")
    #msg[0] = !solve // msg[1] = a (ax²) // msg[2] = b (bx) // msg[3] = class

    if len(msg) != 4 :
        await message.channel.send("""Résout une équation du second degrés.
> **Utilisation :** !solve a b c
> **Exemple :** !solve 12 -3 4 -> 12x² - 3x + 4""")
    else :
        a = float(msg[1])
        b = float(msg[2])
        c = float(msg[3])

        delta = b*b - (4 * a * c)

        if delta == 0 :
            x = -b / 2*a

            answer = "Pour la fonction **" + str(a) + "x² + " + str(b) + "x + " + str(c) + "**:\n> delta = " + str(delta) + "\n> x = " + str(round(x, 2))
        elif delta < 0 :
            answer = "Pour la fonction **" + str(a) + "x² + " + str(b) + "x + " + str(c) + "**\n> Delta est inférieur à 0.\n> Il n'y a pas de racines."
        else :
            x1 = (-b+sqrt(delta))/2*a
            x2 = (-b-sqrt(delta))/2*a

            answer = "Pour la fonction **" + str(a) + "x² + " + str(b) + "x + " + str(c) + "** :\n> delta = **" + str(delta) + "**\n> x1 = **" + str(round(x1, 2)) + "**\n> x2 = **" + str(round(x2, 2)) + "**"

        await message.channel.send(answer)
