from tidalapi import Session

def main():
    session = Session()
    try:
        session.login_oauth_simple()
        if not session.check_login():
            print("Login failed")
            return
    except Exception as e:
        print(f"Error during login: {e}")
        return

    with open(".env", "w") as file:
        file.write(f"TIDAL_TOKEN_TYPE={session.token_type}\n")
        file.write(f"TIDAL_ACCESS_TOKEN={session.token_type}\n")
        file.write(f"TIDAL_REFRESH_TOKEN={session.refresh_token}\n")
        file.write(f"TIDAL_EXPIRY_TIME-{session.expiry_time}\n")
    
    print("Success in generating .env file!")

if __name__ == "__main__":
    main()