import os
import sys
from random import choice
from typing import List, Optional
from tidalapi import Session, Artist, Album, Track


ARTIST_COUNT = 5

def login(session : Session) -> bool:
    token_type = os.getenv("TIDAL_TOKEN_TYPE")
    access_token = os.getenv("TIDAL_ACCESS_TOKEN")
    refresh_token = os.getenv("TIDAL_REFRESH_TOKEN")
    
    if not all([token_type, access_token, refresh_token]):
        print("Error: Missing environment variables")
        return False

    try:
        session.load_oauth_session(
            token_type = token_type,
            access_token = access_token,
            refresh_token=refresh_token
        )
        if not session.check_login():
            print(f"Login failed: Session invalid")    
            return False
        print(f"Logged in successfully as {session.user.username}")
        return True
    except Exception as e:
        print(f"Error while logging in: {e}")
        return False
    

def fetch_artists(session : Session) -> List[Artist]:
    try:
        return session.user.favorites.artists()
    except Exception as e:
        print(f"Error while fetching artits: {e}")
        return []


def get_random_artist(artists : List[Artist]) -> Optional[Artist]:
    if not artists:
        return None
    return choice(artists)


def get_random_similar_artist(artist: Artist) -> Optional[Artist]:
    try:
        similar = artist.get_similar()
        if similar:
            return choice(similar)
        return None
    except Exception as e:
        print(f"Error while getting similar artist: {e}")
        return None
    

def get_albums(artist: Artist) -> List[Album]:
    if not artist:
        return None
    
    try:
        albums = artist.get_albums()
    
        if not albums:
            print(f"No albums have been found")
            return None
    
        return albums
    except Exception as e:
        print(f"Error while getting albums: {e}")
        return []


def get_random_album(albums: List[Album]) -> Optional[Album]:
    if not albums:
        return None
   
    return choice(albums)
    

def get_album_tracks(album: Album) -> List[Track]:
    try:
        tracks = album.tracks()

        if not tracks:
            print(f"Could not get any tracks from album {album.name}")
            return []

        print("Getting tracks successful")
        return tracks
    except Exception as e:
        print(f"Error while getting tracks from album {album.name}: {e}")
        return []

def main() -> None:
    session = Session()
    if not login(session):
        print("Could not initialize Tidal session. Exiting.")
        sys.exit(1)
    
    artists = fetch_artists(session)
    if not artists:
        print("Could not fetch any artists. Exiting")
        sys.exit(1)
    
    random_artists = []

    for _ in range(ARTIST_COUNT):        
        artist = get_random_artist(artists)
        random_artists.append(artist)

    for artist in random_artists:
        print(f"{artist.name}")


if __name__ == "__main__":
    main()
