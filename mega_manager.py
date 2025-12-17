import subprocess
import time
from pathlib import Path
from config import DOWNLOAD_DIR, MEGA_LINK, QUOTA_SLEEP_SECONDS

def download_with_quota_handling():
    Path(DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)

    while True:
        print("Starting / resuming MEGA download...")

        process = subprocess.run(
            [
                "megatools", "dl",
                "--recursive",
                "--resume",
                "--path", DOWNLOAD_DIR,
                MEGA_LINK
            ],
            capture_output=True,
            text=True
        )

        output = (process.stdout + process.stderr).lower()

        if "quota" in output or "transfer" in output:
            print("MEGA quota reached. Waiting for reset...")
            time.sleep(QUOTA_SLEEP_SECONDS)
            continue

        if process.returncode == 0:
            print("MEGA download completed.")
            break

        print("Temporary MEGA error. Retrying in 10 minutes...")
        time.sleep(600)
