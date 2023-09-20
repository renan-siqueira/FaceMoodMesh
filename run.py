import os
from viewer.video_viewer import run_video_viewer
from utils.helpers import load_json
from config.settings import PATH_INPUT_DIR, VIDEO_NAME, PATH_MESSAGE_FILE, DISPLAY_WIDTH, DISPLAY_HEIGHT


if __name__ == '__main__':

    video_path = os.path.join(PATH_INPUT_DIR, VIDEO_NAME)
    messages = load_json(PATH_MESSAGE_FILE)

    run_video_viewer(
        video_path,
        messages,
        display_width=DISPLAY_WIDTH,
        display_height=DISPLAY_HEIGHT
    )
