from pathlib import Path
from config import DOWNLOAD_DIR, RENAMED_DIR, COURSE_NAME

VIDEO_EXT = {".mp4", ".mkv", ".avi", ".mov", ".webm"}
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}

def rename_all_files():
    Path(RENAMED_DIR).mkdir(parents=True, exist_ok=True)

    files = sorted(
        f for f in Path(DOWNLOAD_DIR).rglob("*")
        if f.suffix.lower() in VIDEO_EXT | IMAGE_EXT
    )

    v = i = 0

    for file in files:
        ext = file.suffix.lower()
        if ext in VIDEO_EXT:
            v += 1
            name = f"{COURSE_NAME}_VIDEO_{v:04d}{ext}"
        else:
            i += 1
            name = f"{COURSE_NAME}_IMAGE_{i:04d}{ext}"

        file.rename(Path(RENAMED_DIR) / name)

    print(f"Renamed {v} videos and {i} images")
    return v + i
