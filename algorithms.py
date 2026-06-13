from client import TidalClient
from random import shuffle, sample, choice

TARGET_ARTIST_COUNT = 10
SIMILAR_COUNT_PER_ARTIST = 5

class TidalAlgorithms:
    def __init__(self, client: TidalClient):
        self._client = client


    def followed_aritsts_mix(self, artist_count: int = None, track_count: int = 5) -> None:
        print("Running Followed Artist playlist generation")




# def generate_similar_artist(self) -> None:
#     print("Running playlist generation based off similar artists from favorite artists")

#     artists = _client.fetch_favorite_artists()
#     if not artists:
#         print("Could not fetch any artists. Exiting")
#         return
    
#     shuffle(artists)

#     selected_data = {}
#     for artist in artists:
#         if len(selected_data) >= TARGET_ARTIST_COUNT:
#             break
        
#         similar_list = _client.get_similar_artists(artist)
#         if len(similar_list) >= SIMILAR_COUNT_PER_ARTIST:
#             chosen_similar = sample(similar_list, SIMILAR_COUNT_PER_ARTIST)
#             selected_data[artist] = chosen_similar
#         else:
#             continue
    
#     if len(selected_data) < TARGET_ARTIST_COUNT:
#         print(f"Warning: Could only find {len(selected_data)} artists with enough similar artists")
    
#     track_ids_to_add = []

#     for similar_artists_list in selected_data.values():
#         for artist in similar_artists_list:
#             albums = _client.get_albums(artist)

#             if not albums:
#                 continue

#             random_album = choice(albums)
#             tracks = client.get_album_tracks(random_album)

#             if not tracks:
#                 continue
            
#             random_track = choice(tracks)

#             track_ids_to_add.append(random_track.id)
#             print(f"Queued for playlist: {random_track.name} by {artist.name}")
        
#     if not track_ids_to_add:
#         print("\nNo tracks were found. Exiting")
#         return
    
#     try:
#         playlist_name = "discover mix"
#         playlist_desc = "python auto discovery script testing"

#         print(f"\nCreating playlist: '{playlist_name}")

#         new_playlist = _client.session.user.create_playlist(playlist_name, playlist_desc)
#         new_playlist.add(track_ids_to_add)
        
#         print(f"Success! Added {len(track_ids_to_add)} tracks to the playlist")
#     except Exception as e:
#         print(f"\nError while creating playlist: {e}")