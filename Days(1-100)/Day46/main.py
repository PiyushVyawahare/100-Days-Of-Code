import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Authentication
SPOTIFY_CLIENT_ID = "afab7caf99334ecbbee38b5efb98c1df"
SPOTIFY_CLIENT_SECRET = "77bae36ca80b487bae65d678d0b9ea12"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Scraping Billboard Hot 100
date = input("Enter your favorite date in the format YYYY-MM-DD : ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, "html.parser")
song_names = soup.find_all(
    name="span", class_="chart-element__information__song")
song_titles = [song.get_text() for song in song_names]

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    print(song ,year)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)
# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.user_playlist_add_tracks(
    user=user_id, playlist_id=playlist["id"], tracks=song_uris)
