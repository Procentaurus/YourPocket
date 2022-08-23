from pathlib import Path
import os

def deleteFile(path):
    if path != '/images/model.png':
        BASE_DIR = Path(__file__).resolve().parent.parent
        final_path = str(BASE_DIR) +'/static/images/user_images/' + str(path)
        if os.path.exists(final_path):
            os.remove(final_path)
        return True
    else:
        return False