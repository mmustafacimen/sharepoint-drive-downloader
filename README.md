# sharepoint-drive-downloader

This project allows downloading all files and folders from a SharePoint or OneDrive drive using the Microsoft Graph API.

## Project Structure

* **auth.py** → Handles Microsoft OAuth authorization using Flask
* **downloader.py** → Recursively downloads files and folders from the user's drive

## Features

* Microsoft Graph API integration
* Automatic access token generation
* Recursive folder download
* Supports downloading files from nested folders

## Requirements

* Python 3.8+
* Flask
* requests

Install dependencies:

```
pip install flask requests
```

## Configuration

Before running the scripts, you must configure your Azure AD credentials.

Required values:

* CLIENT_ID – Azure application client ID
* CLIENT_SECRET – Azure application client secret
* TENANT_ID – Azure tenant ID
* USERNAME – Microsoft account username
* PASSWORD – Microsoft account password

Replace these values inside the scripts.

Example:

```
client_id = "your_client_id"
client_secret = "your_client_secret"
tenant_id = "your_tenant_id"
username = "your_username"
password = "your_password"
```

## Usage

### 1. Authorization (Optional)

Run the OAuth authorization server:

```
python auth.py
```

Steps:

1. Starts a local Flask server
2. Redirects the user to the Microsoft login page
3. Receives the authorization code
4. Exchanges the code for an access token

### 2. Download Files

Run the downloader script:

```
python downloader.py
```

The script will:

* Authenticate with Microsoft Graph API
* List files and folders in the user's drive
* Download all files recursively

Downloaded files will be saved in the current directory.

## Notes

* This project uses the Microsoft Graph API.
* Proper Azure AD permissions are required.
* The application must have permissions such as:

  * `Files.Read`
  * `Files.Read.All`
  * `Sites.Read.All`

## Security Warning

Never publish real credentials in a public repository.

Always remove or replace sensitive information before uploading to GitHub.
