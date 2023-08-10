#
# import json
#
# with open("token.txt", encoding="utf8") as file:
#     content = json.load(file)
#     # content = file.read()
#     access_token = content["access_token"]
#     print(access_token)

import spotipy

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify()
artist = sp.artist(urn)
print(artist)
