import spotipy
import requests
import json
import datetime
import os
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET = os.environ.get("SECRET")
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
CACHE_PATH = "token.txt"

URL = "https://www.billboard.com/charts/hot-100"

SPOTIFY_ENDPOINT = "https://api.spotify.com/v1"

add_playlist = "yes"
while add_playlist.lower() == "yes":
    date = ""
    date_format = "%Y-%m-%d"

    while True:
        try:
            date = input("what year you would like to travel to? YYYY-MM-DD\t")
            dateObject = datetime.datetime.strptime(date, date_format)
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
        else:
            break

    response = requests.get(f"{URL}/{date}")
    response.raise_for_status()
    spotify_website = response.text

    soup = BeautifulSoup(spotify_website, "html.parser")
    titles = [title.getText().strip("\n\t") for title in soup.select(selector="li ul li h3", class_="c-title")]
    artists = [artist.getText().strip("\n\t") for artist in soup.select(selector="li ul li span", class_="c-label") if
               not artist.getText().strip("\n\t").isdigit() and artist.getText().strip("\n\t") != "-"]
    title_artist_list = dict(zip(titles, artists))
    year = date.split("-")[0]

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE,
            cache_path=CACHE_PATH,
            show_dialog=True,
        )
    )

    user_id = sp.current_user()["id"]

    with open("token.txt", encoding="utf8") as file:
        content = json.load(file)
        access_token = content["access_token"]

    headers = {
        "Authorization": "Bearer {token}".format(token=access_token)
    }

    tracks_uris = []
    for title in titles:
        params = {
            "q": f"track:{title} artist:{title_artist_list[title]} year:{year}",
            "type": "track",
        }
        try:
            track_info = requests.get(
                'https://api.spotify.com/v1/search',
                headers=headers,
                params=params,
            ).json()
            track_uri = track_info["tracks"]["items"][0]["uri"]
        except IndexError or KeyError:
            params = {
                "q": f"track:{title} artist:{title_artist_list[title].split(' ')[0]} year:{year}",
                "type": "track",
            }
            try:
                track_info = requests.get(
                    'https://api.spotify.com/v1/search',
                    headers=headers,
                    params=params,
                ).json()
                track_uri = track_info["tracks"]["items"][0]["uri"]
            except IndexError or KeyError:
                continue
            else:
                tracks_uris.append(track_uri)
        else:
            tracks_uris.append(track_uri)

    try:
        params = {
            "q": f"{date} Billboard 100",
            "type": "playlist",
        }
        playlist_search = requests.get(
            'https://api.spotify.com/v1/search',
            headers=headers,
            params=params,
        ).json()
        playlist_uri = playlist_search["playlists"]["items"][0]["uri"]
    except IndexError or KeyError:
        playlist = sp.user_playlist_create(
            user=user_id,
            name=f"{date} Billboard 100",
            public=False,
            collaborative=False,
            description="NONE",
        )
        playlist_id = playlist["id"]

        sp.playlist_add_items(
            playlist_id=playlist_id,
            items=tracks_uris,
            position=None,
        )
        print("playlist has been created")
    else:
        sp.playlist_replace_items(playlist_id=playlist_uri, items=tracks_uris)
        print("playlist has been updated!")

    while True:
        add_playlist = input("Do you want to add another playlist? yes/no\t")
        if add_playlist.lower() == "yes" or add_playlist.lower() == "no":
            break
        else:
            print("Invalid response, should be 'yes' or 'no'")
