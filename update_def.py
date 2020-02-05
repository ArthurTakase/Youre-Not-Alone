import discord #pip install discord.api

async def patch(message):
    patchnote = """**MAJ du 28/12/19**
> MAJ de la commande `!banuser` (ne prend en compte que les membres du serveur).
> Ajout de la commande `!guessconfig`.
> Ajout de la commande `!guesslaunch`.
Ce bot a été mis à jour pour la dernière fois le __28/12/19 à 00h00__."""

    await message.channel.send(patchnote)

async def help_def(message):
    commandes = """**Liste des commandes** (https://textup.fr/380108Xy)
> **Infos et Retours**
> `!help` `!patch` `!dev` `!devlist`
> **Guess Game**
> `!guess` `!guesslist` `!guessup` `!guessconfig` `!guesslaunch`
> **Random**
> `!duck` `!image` `!russian` `!coin` `!solve` `!patcho`
> **Anniversaire**
> `!birth` `!addbirth` `!allbirth` `!databirth` `!removebirth`
> **Weeb**
> `!randomanime` `!randommanga` `!goodanime` `!addanime` `!removeanime` `!allanime`
> **Administration**
> `!clear` `!banword` `!banlist` `!unbanword` `!banuser`
"""
    await message.channel.send(commandes)
