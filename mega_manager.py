import subprocess
import time
from pathlib import Path
from config import DOWNLOAD_DIR, MEGA_LINK, QUOTA_SLEEP_SECONDS

def download_with_quota_handling():
    Path(DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)

    while True:
        print("Starting / resuming MEGA download...")

        proc = subprocess.run(
            ["mega-get", MEGA_LINK, DOWNLOAD_DIR],
            capture_output=True,
            text=True
        )

        output = (proc.stdout + proc.stderr).lower()

        if "quota" in output or "exceeded" in output:
            print("MEGA quota reached. Waiting...")
            time.sleep(QUOTA_SLEEP_SECONDS)
            continue

        if proc.returncode == 0:
            print("MEGA download completed.")
            break

        print("Temporary MEGA error. Retrying in 10 minutes...")
        time.sleep(600)
