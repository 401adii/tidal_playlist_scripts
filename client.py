import os
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