from pathlib import Path
from config import DOWNLOAD_DIR, RENAMED_DIR, COURSE_NAME

VIDEO_EXT = {".mp4", ".mkv", ".avi", ".mov", ".webm"}
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}

def rename_all_files():
    Path(RENAMED_DIR).mkdir(parents=True, exist_ok=True)

    all_files = sorted(
        f for f in Path(DOWNLOAD_DIR).rglob("*")
        if f.suffix.lower() in VIDEO_EXT | IMAGE_EXT
    )

    video_count = 0
    image_count = 0

    for file in all_files:
        suffix = file.suffix.lower()

        if suffix in VIDEO_EXT:
            video_count += 1
            new_name = f"{COURSE_NAME}_VIDEO_{video_count:04d}{suffix}"

        elif suffix in IMAGE_EXT:
            image_count += 1
            new_name = f"{COURSE_NAME}_IMAGE_{image_count:04d}{suffix}"

        target = Path(RENAMED_DIR) / new_name
        file.rename(target)

    print(f"Renamed {video_count} videos and {image_count} images")

    return video_count + image_count
