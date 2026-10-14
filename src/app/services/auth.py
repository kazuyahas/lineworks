import os, time, jwt, asyncio, requests

def generate_jwt():
    now = int(time.time())
    payload = {
        "iss": os.environ["LINEWORKS_CLIENT_ID"],
        "sub": os.environ["LINEWORKS_SERVICE_ACCOUNT_EMAIL"],
        "iat": now,
        "exp": now + 1800
    }
    with open("/etc/secrets/private_20261014164535.key", "r") as f:
        private_key = f.read()
    return jwt.encode(payload, private_key, algorithm="RS256")

def get_access_token():
    assertion = generate_jwt()
    url = "https://auth.worksmobile.com/oauth2/v2.0/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "client_id": os.environ["LINEWORKS_CLIENT_ID"],
        "client_secret": os.environ["LINEWORKS_CLIENT_SECRET"],
        "assertion": assertion,
        "scope": "bot"
    }
    r = requests.post(url, headers=headers, data=data)
    return r.json()["access_token"]

async def start_token_refresh(app):
    async def refresh():
        while True:
            app.state.access_token = get_access_token()
            await asyncio.sleep(60 * 25)
    asyncio.create_task(refresh())