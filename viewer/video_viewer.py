# video_viewer.py
import cv2
from core import video_processing


def run_video_viewer(video_path, messages, display_width, display_height):
    """
    Runs the video viewer, processing and displaying the video frame by frame.

    Parameters:
    - video_path (str): Path of the video file to be processed.
    - messages (dict): Dictionary containing messages for display on the interface.
    - display_width (int): Width of the video display window.
    - display_height (int): Height of the video display window.

    During execution, the video is processed frame by frame to detect faces, facial points, and emotions. 
    The user can pause, play, and change settings in real-time using keyboard shortcuts.
    """
    
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print('fps:', fps)

    pause = False
    show_keypoints = False
    show_emotions = False
    show_help = False

    while cap.isOpened():
        if not pause:
            ret, frame = cap.read()

            if not ret:
                break

            face_data_list, display_frame = video_processing.process_frame(frame, display_width, display_height, show_keypoints, show_emotions)
            video_processing.update_display(display_frame, messages, display_width, show_help)

        action, pause, show_keypoints, show_emotions, show_help = video_processing.handle_user_input(pause, show_keypoints, show_emotions, show_help)

        if action == 'break':
            break

    cap.release()
    cv2.destroyAllWindows()
