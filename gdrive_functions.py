from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = 'YOU_FOLDER_ID_HERE'

# assume you created the folder in your google drive 
# assume this is the link of your drive folder:  https://drive.google.com/drive/folders/15B2Z06-7os3CdfbnbUdq-cOaUjJRUNFl1t
# so the folder id is 15B2Z06-7os3CdfbnbUdq-cOaUjJRUNFl1t

def authenticate():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_file(file_path):
    file_name = os.path.basename(file_path)
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': file_name,
        'parents': [PARENT_FOLDER_ID]
    }
    file = service.files().create(
        body=file_metadata,
        media_body=file_path,
    ).execute()
    print('File ID: %s' % file.get('id'))
    print(f"File uploaded successfully: {file_path}")

def get_path(service, file_id, path=''):
    file = service.files().get(fileId=file_id, fields='id, name, parents').execute()
    path = f'/{file["name"]}' + path
    if 'parents' in file:
        path = get_path(service, file['parents'][0], path)
    return path

def list_files_in_folder(service, folder_id):
    print("please be patient, this may take a while...")
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, mimeType, parents)", q=f"'{folder_id}' in parents").execute()
    items = results.get('files', [])
    for item in items:
        item['path'] = get_path(service, item['id'])
        # if the item is a folder, recurse into it
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            list_files_in_folder(service, item['id'])
        print(item['path'])


def list_all_files():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    list_files_in_folder(service, PARENT_FOLDER_ID)