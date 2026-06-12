import sys
from client import TidalClient
from random import choice, sample, shuffle
from tidal_utils import fetch_favorite_artists, get_similar_artists, get_album_tracks, get_albums

#probably will be moved as arguments 
TARGET_ARTIST_COUNT = 10
SIMILAR_COUNT_PER_ARTIST = 5

def generate_playlist(client : TidalClient) -> None:
    #this algorithm needs adjustments/different approach
    #tidalapi seems to have outdated data for certain aritsts :((
    print("Running playlist generation based off similar artists from favorite artists")

    artists = fetch_favorite_artists(client)
    if not artists:
        print("Could not fetch any artists. Exiting")
        return
    
    shuffle(artists)

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

        new_playlist = client.session.user.create_playlist(playlist_name, playlist_desc)
        new_playlist.add(track_ids_to_add)
        
        print(f"Success! Added {len(track_ids_to_add)} tracks to the playlist")
    except Exception as e:
        print(f"\nError while creating playlist: {e}")
        
