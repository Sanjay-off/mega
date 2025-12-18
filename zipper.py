import subprocess
from pathlib import Path
from config import (
    DOWNLOAD_DIR,
    ZIP_DIR,
    ZIP_PASSWORD,
    ZIP_PART_SIZE_MB,
    COURSE_NAME
)

def create_zip_parts():
    Path(ZIP_DIR).mkdir(parents=True, exist_ok=True)

    # Zip base path
    zip_base = Path(ZIP_DIR) / COURSE_NAME

    # 7-Zip command preserving folder structure
    subprocess.run(
        [
            "7z", "a",
            f"{zip_base}.zip",
            f"{DOWNLOAD_DIR}/*",   # IMPORTANT: zip original structure
            f"-p{ZIP_PASSWORD}",
            "-mhe=on",             # encrypt filenames + structure
            "-mem=AES256",
            f"-v{ZIP_PART_SIZE_MB}m"
        ],
        check=True
    )

    return sorted(Path(ZIP_DIR).glob("*.zip*"))
