import shutil
from config import WORK_DIR

def cleanup():
    shutil.rmtree(WORK_DIR, ignore_errors=True)
