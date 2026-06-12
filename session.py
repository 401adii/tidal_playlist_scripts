import os
from tidalapi import Session

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

if __name__ == "__main__":
    pass