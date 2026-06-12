import sys
import argparse
from client import TidalClient
from algorithms import similar_artists

def main():
    parser = argparse.ArgumentParser(description="Generate Tidal Playlists automatically")
    
    parser.add_argument(
        "algorithm",
        type=str,
        choices=["similar", "followed"],
        help="Which algorithm to run"
    )

    args = parser.parse_args()
    
    client = TidalClient()

    if not client.is_logged_in:
        print("Could not initialize Tidal session. Exiting")
        sys.exit(1)

    if args.algorithm == "similar":
        similar_artists.generate_playlist(client)
    elif args.algorithm == "followed":
        print("WIP")
        


if __name__ == "__main__":
    main()