import os
from typing import List
from tidalapi import Artist, Album, Track
from tidalapi import Session

class TidalClient:
    def __init__(self):
        self.session = Session()
        self.is_logged_in = self._login()

    def _login(self) -> bool:
        token_type = os.getenv("TIDAL_TOKEN_TYPE")
        access_token = os.getenv("TIDAL_ACCESS_TOKEN")
        refresh_token = os.getenv("TIDAL_REFRESH_TOKEN")

        if not all([token_type, access_token, refresh_token]):
            print("Error: Missing environmental variables")
            return False
        
        try:
            self.session.load_oauth_session(
                token_type=token_type,
                access_token=access_token,
                refresh_token=refresh_token,
            )
            if not self.session.check_login():
                print("Login failed: Session invalid")
                return False

            print(f"Logged in successfully as {self.session.user.username}")
            return True
        except Exception as e:
            print(f"Error while logging in: {e}")
            return False
    
    def fetch_favorite_artists(self) -> List[Artist]:
        try:
            return self.session.user.favorites.artists()
        except Exception as e:
            print(f"Error while fetching artists: {e}")
            return []

    def get_similar_artists(self, artist: Artist) -> List[Artist]:
        try:
            similar = artist.get_similar()
            if similar:
                return similar
            return []
        except Exception as e:
            print(f"Error while fetching similar artists for {artist.name}: {e}")
            return []


    def fetch_artists(self) -> List[Artist]:
        try:
            return self.session.user.favorites.artists()
        except Exception as e:
            print(f"Error while fetching artits: {e}")
            return []


    def get_similar_artists(self, artist: Artist) -> List[Artist]:
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