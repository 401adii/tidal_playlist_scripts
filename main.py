import sys
import argparse
from client import TidalClient
from algorithms import TidalAlgorithms

def main():
    parser = argparse.ArgumentParser(description="Generate Tidal Playlists automatically")

    subparsers = parser.add_subparsers(
        dest="algorithm",
        required=True,
        help="Which algorithm to run"
    )

    followed_parser = subparsers.add_parser(
        "followed",
        help="Generate playlist from followed artists"
    )

    followed_parser.add_argument(
        "--artists",
        type=int, 
        default=None,
        help="Number of followed artists (default: all)"
    )
    
    followed_parser.add_argument(
        "--tracks",
        type=int,
        default=5,
        help="Number of tracks per artist (default: 5)"
    )

    args = parser.parse_args()
    
    client = TidalClient()
    
    if not client.is_logged_in:
        print("Could not initialize Tidal session. Exiting")
        sys.exit(1)
    
        algorithms = TidalAlgorithms(client=client)


    if args.algorithm == "similar":
        print("WIP")
    elif args.algorithm == "followed":
        algorithms.followed_aritsts_mix()
        


if __name__ == "__main__":
    main()