import os
import sys
from random import choice, sample, shuffle
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


def main() -> None:
    session = Session()
    if not login(session):
        print("Could not initialize Tidal session. Exiting.")
        sys.exit(1)
    
    artists = fetch_artists(session)
    if not artists:
        print("Could not fetch any artists. Exiting")
        sys.exit(1)
    
    shuffle(artists)

    TARGET_ARTIST_COUNT = 10
    SIMILAR_COUNT_PER_ARTIST = 5

    selected_data = {}
    for artist in artists:
        if len(selected_data) >= TARGET_ARTIST_COUNT:
            break
        
        similar_list = get_similar_artists(artist)
        if len(similar_list) >= SIMILAR_COUNT_PER_ARTIST:
            chosen_similar = sample(similar_list, SIMILAR_COUNT_PER_ARTIST)
            selected_data[artist] = chosen_similar
        else:
            continue
    
    if len(selected_data) < TARGET_ARTIST_COUNT:
        print(f"Warning: Could only find {len(selected_data)} artists with enough similar artists")
    
    track_ids_to_add = []

    for similar_artists_list in selected_data.values():
        for artist in similar_artists_list:
            albums = get_albums(artist)

            if not albums:
                continue

            random_album = choice(albums)
            tracks = get_album_tracks(random_album)

            if not tracks:
                continue
            
            random_track = choice(tracks)

            track_ids_to_add.append(random_track.id)
            print(f"Queued for playlist: {random_track.name} by {artist.name}")
        
    if not track_ids_to_add:
        print("\nNo tracks were found. Exiting")
        sys.exit(1)
    
    try:
        playlist_name = "discover mix"
        playlist_desc = "python auto discovery script testing"

        print(f"\nCreating playlist: '{playlist_name}")

        new_playlist = session.user.create_playlist(playlist_name, playlist_desc)
        new_playlist.add(track_ids_to_add)
        
        print(f"Success! Added {len(track_ids_to_add)} tracks to the playlist")
    except Exception as e:
        print(f"\nError while creating playlist: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
