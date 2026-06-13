from client import TidalClient
from random import shuffle, sample, choice

class TidalAlgorithms:
    def __init__(self, client: TidalClient):
        self._client = client


    def followed_artists_mix(self, artist_count: int = None, track_count: int = 5) -> None:
        #needs adjustments
        print("Running Followed Artist playlist generation")

        artists = self._client.fetch_favorite_artists()
        shuffle(artists)

        if artist_count is not None:
            count = min(artist_count, len(artists))   
            artists = sample(artists, count)
        
        if not artists:
            print("Artist list is empty. Aborting.")
            return
        
        final_tracks = []
        seen_track_ids = set()

        for artist in artists:
            albums = self._client.get_albums(artist)

            if not albums:
                print(f"No albums found for {albums.name}")
                continue

            artist_track_pool = []

            if track_count == 0:
                albums_to_fetch = albums
            else:
                albums_sample_size = min(track_count, len(albums))
                albums_to_fetch = sample(albums, albums_sample_size)

            for album in albums_to_fetch:
                artist_track_pool.extend(self._client.get_album_tracks(album))

            if track_count == 0:
                selected_tracks = artist_track_pool
            else:
                count = min(track_count, len(artist_track_pool))
                selected_tracks = sample(artist_track_pool, count)
            
            for track in selected_tracks:
                if track.id not in seen_track_ids:
                    seen_track_ids.add(track.id)
                    final_tracks.append(track)
                    print(f"+ Queued track {track.name}")
                else:
                    print(f"- Skipped duplicate: {track.name}")

        if final_tracks:
            shuffle(final_tracks)

            playlist_name = "Followed Daily Mix"
            playlist_desc = "Python script testing"
            self._client.create_playlist(
                playlist_name,
                playlist_desc,
                final_tracks
            ) 
        else:
            print("No valid tracks were found to add")


                

        




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