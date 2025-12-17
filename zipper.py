import os
import pyminizip
from pathlib import Path
from config import (
    RENAMED_DIR, ZIP_DIR,
    ZIP_PASSWORD,
    ZIP_PART_SIZE_MB,
    ZIP_COMPRESSION_LEVEL,
    COURSE_NAME
)

def create_zip_parts():
    Path(ZIP_DIR).mkdir(parents=True, exist_ok=True)

    files = [str(Path(RENAMED_DIR) / f) for f in os.listdir(RENAMED_DIR)]

    pyminizip.compress_multiple(
        files=files,
        output_path=ZIP_DIR,
        password=ZIP_PASSWORD,
        compression_level=ZIP_COMPRESSION_LEVEL,
        volume_size=ZIP_PART_SIZE_MB * 1024 * 1024
    )

    zip_files = sorted(Path(ZIP_DIR).iterdir())
    final = []

    for i, z in enumerate(zip_files, 1):
        new = z.with_name(f"{COURSE_NAME}_PART_{i:02d}.zip")
        z.rename(new)
        final.append(new)

    return final
