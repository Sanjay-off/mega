from mega_manager import download_with_quota_handling
# from renamer import rename_all_files
from zipper import create_zip_parts
from uploader import upload_to_telegram
from cleanup import cleanup

def main():
    download_with_quota_handling()

    # count = rename_all_files()
    # if count == 0:
    #     print("No files found. Exiting.")
    #     return

    zip_files = create_zip_parts()
    upload_to_telegram(zip_files)

    cleanup()
    print("All files uploaded successfully.")

if __name__ == "__main__":
    main()
