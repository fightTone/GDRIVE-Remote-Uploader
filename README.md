# GDRIVE-Remote-Uploader

Alternative. this will help you transfer files to your gdrive when u cant use scp ftp etc. are not available.

**Steps:**

* *Google Cloud Setup*

1. go to console.cloud.google.com and create a project
2. go to Library and add Google Drive
3. go to credential and manage service accounts
4. create aservice account and copy the email created
5. click the Actions and choose "Manage Keys"
6. "ADD KEY" then create new key and choose "json" as keytype
7. download it and place it on the repository or somewhere u can keep it safe

* *G-Drive Setup*

1. create a Folder in your gdrive
2. share the folder to the email you recently copied from (Google Cloud Setup) number 4

* *Run the app.py*

1. in app.py, replace the value in SERVICE_ACCOUNT_FILE = to the path where the the json file is located (*Google Cloud Setup* number 7)
2. in app.py, replace the value of the PARENT_FOLDER_ID with your own folder id.

   ```
   # assume you created the folder in your google drive 
   # assume this is the link of your drive folder:  https://drive.google.com/drive/folders/15B2Z06-7os3CdfbnbUdq-cOaUjJRUNFl1t
   # so the folder id is 15B2Z06-7os3CdfbnbUdq-cOaUjJRUNFl1t
   ```
3. run the app .py and enjoy

   ```
   python app.py
   ```
   Note you can add config.json or any configs for it.
