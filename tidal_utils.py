from typing import List
from tidalapi import Artist, Album, Track
from client import TidalClient

def fetch_favorite_artists(client: TidalClient) -> List[Artist]:
    try:
        return client.session.user.favorites.artists()
    except Exception as e:
        print(f"Error while fetching artists: {e}")
        return []


def get_similar_artists(artist: Artist) -> List[Artist]:
    try:
        similar = artist.get_similar()
        if similar:
            return similar
        return []
    except Exception as e:
        print(f"Error while fetching similar artists for {artist.name}: {e}")
        return []


def fetch_artists(client : TidalClient) -> List[Artist]:
    try:
        return client.session.user.favorites.artists()
    except Exception as e:
        print(f"Error while fetching artits: {e}")
        return []


def get_similar_artists(artist: Artist) -> List[Artist]:
    try:
        similar = artist.get_similar()
        if similar:
            return similar
        return []
    except Exception as e:
        print(f"Error while getting similar artist for {artist.name}: {e}")
        return []
    

def get_albums(artist: Artist) -> List[Album]:
    if not artist:
        return []
    
    try:
        albums = artist.get_albums()
    
        if not albums:
            print(f"No albums have been found for {artist.name}")
            return []
    
        return albums
    except Exception as e:
        print(f"Error while getting albums: {e}")
        return []
    

def get_album_tracks(album: Album) -> List[Track]:
    try:
        tracks = album.tracks()

        if not tracks:
            print(f"Could not get any tracks from album {album.name}")
            return []

        return tracks
    except Exception as e:
        print(f"Error while getting tracks from album {album.name}: {e}")
        return []