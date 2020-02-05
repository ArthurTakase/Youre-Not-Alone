import discord #pip install discord.api
from imgurpython import ImgurClient #pip install imgurpython
import imgurpython
from random import choice

client_id = '964662976ac554f'
client_secret = 'b05f5fd17e5f5e9758cc69a1f891c106dab0ad26'
client_imgur = ImgurClient(client_id, client_secret)

async def gallery_search(self, q, advanced=None, sort='time', window='all', page=0):
    if advanced:
        data = {field: advanced[field]
                for field in set(self.allowed_advanced_search_fields).intersection(advanced.keys())}
    else:
        data = {'q': q}

    response = self.make_request('GET', 'gallery/search/%s/%s/%s' % (sort, window, page), data)
    return build_gallery_images_and_albums(response)

async def duck(message):
    tag_gallery = client_imgur.gallery_search("duck animal cute")
    image = choice(tag_gallery).link
    await message.channel.send(image)

async def image(message):
    msg = message.content.split(" ", 1)

    if len(msg) == 1:
        await message.channel.send("""Affiche une image en fonction des tags donnés
> **Exemple :** !image cat cute kitten""")

    else :
        tag_gallery = client_imgur.gallery_search(msg[1])
        image = choice(tag_gallery).link
        await message.channel.send(image)
