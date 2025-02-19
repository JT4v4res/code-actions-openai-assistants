from openai import OpenAI
import requests
import os
import json
from datetime import datetime


def upload_json_to_drive(access_token: str, json_data: json, file_name: str, parent_folder_id: str = None) -> str | None:
    """
    Uploads JSON data to Google Drive without saving it locally.

    :param access_token: OAuth 2.0 access token.
    :param json_data: Dictionary containing JSON data to upload.
    :param file_name: Name of the file to create on Google Drive.
    :param parent_folder_id: (Optional) ID of the parent folder on Google Drive.
    :return: ID of the uploaded file if successful, None otherwise.
    """
    upload_url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'
    headers = {'Authorization': f'Bearer {access_token}'}

    # File metadata
    metadata = {
        'name': file_name,
        'mimeType': 'application/json'
    }
    if parent_folder_id:
        metadata['parents'] = [parent_folder_id]

    # Convert JSON data to a byte stream
    json_bytes = json.dumps(json_data).encode('utf-8')

    # Multipart request body
    files = {
        'metadata': ('metadata', json.dumps(metadata), 'application/json; charset=UTF-8'),
        'file': (file_name, json_bytes, 'application/json')
    }

    response = requests.post(upload_url, headers=headers, files=files)
    if response.status_code == 200:
        file_id = response.json().get('id')
        print(f'File uploaded successfully. File ID: {file_id}')
        return file_id
    else:
        print('Error uploading file:', response.text)
        return None


def get_google_auth(client_secret: str, ref_token: str, client_id: str) -> str:
    """
    Get Google OAuth 2.0 access token using the refresh token.
    :param client_secret:
    :param ref_token:
    :param client_id:
    :return access_token:
    """
    auth_url = 'https://oauth2.googleapis.com/token'

    auth_params = {
        "client_secret": client_secret,
        "grant_type": "refresh_token",
        "refresh_token": ref_token,
        "client_id": client_id,
    }

    auth_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    auth_response = requests.post(auth_url, params=auth_params, headers=auth_headers)

    return auth_response.json().get('access_token')


def get_thread_messages(client: OpenAI, thread_id: str) -> str:
    """
    Get all the messages from a thread.

    :param client:
    :param thread_id:
    :return:
    """
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    return json.dumps([message.to_dict() for message in messages.data], indent=4)

def create_thread(client: OpenAI) -> str:
    thread = client.beta.threads.create()

    return thread.id


def main() -> None:
    os.environ['OPENAI_API_KEY'] = "<YOUR_OPENAI_API_KEY>"

    client = OpenAI()

    thread_id = "<YOUR_THREAD_ID>"

    drive_api_client_secret = "<YOUR_CLIENT_SECRET>"

    drive_api_refresh_token = "<YOUR_REFRESH_TOKEN>"

    drive_api_client_id = "<YOUR_API_ID>"

    thread_json = get_thread_messages(client, thread_id=thread_id)

    access_token = get_google_auth(client_secret=drive_api_client_secret, ref_token=drive_api_refresh_token, client_id=drive_api_client_id)

    file_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_{thread_id}.json'

    upload_json_to_drive(access_token, json_data=thread_json, file_name=file_name, parent_folder_id="<YOUR_PARENT_FOLDER_ID>")


if __name__ == '__main__':
    main()