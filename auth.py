import requests
from flask import Flask, redirect, request

app = Flask(__name__)

# Azure AD and Microsoft Graph API
client_id = "your_client_id"
client_secret = "your_client_secret"
tenant_id = "your_tenant_id"
username = "your_username"
password ="your_password"
scope = "offline_access Files.Read Files.Read.All Sites.Read.All"
redirect_uri = "http://localhost:5000/callback"



def get_access_token(code):
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope
    }
    token_response = requests.post(token_url, data=token_data)
    token_response.raise_for_status()
    return token_response.json()['access_token']


@app.route('/')
def home():
    authorization_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize"
    authorization_url += f"?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&response_mode=query&scope={scope}&state=12345"
    return redirect(authorization_url)


@app.route('/callback')
def callback():
    code = request.args.get('code')
    access_token = get_access_token(code)
    return "Authorization successful. You can close this window."


if __name__ == '__main__':
    app.run(port=5000)
