from gdrive_functions import upload_file, list_all_files

if __name__ == '__main__':
    while True:
        print("""
            1. List all files
            2. Upload a file
            type 'exit' to exit
        """)
        choice = input ("-> ")
        if choice == '1':
            list_all_files()
        elif choice == '2':
            to_upload = r''+input('Enter the fullpath to upload: ')
            upload_file(to_upload)
        elif choice == 'exit':
            break
