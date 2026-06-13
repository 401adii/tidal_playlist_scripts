import sys
import argparse
from client import TidalClient
from algorithms import TidalAlgorithms

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
    algorithms = TidalAlgorithms(client=client)

    if not client.is_logged_in:
        print("Could not initialize Tidal session. Exiting")
        sys.exit(1)

    if args.algorithm == "similar":
        print("WIP")
    elif args.algorithm == "followed":
        algorithms.followed_aritsts_mix()
        


if __name__ == "__main__":
    main()