# video_processing.py
import cv2
from video_tools import is_human_face, draw_rectangle, resize_frame, add_messages_to_frame, handle_key_press


def process_face_data(frame, show_keypoints, show_emotions):
    """
    Processes face data to identify keypoints and emotions.
    
    Args:
    - frame: The frame to be processed.
    - show_keypoints: If true, displays keypoints on the frame.
    - show_emotions: If true, displays emotions on the frame.

    Returns:
    - List of face data and annotated frame.
    """

    face_data_list = is_human_face(frame, show_keypoints, show_emotions)
    annotated_frame = frame

    for face_data in face_data_list:
        x_min, y_min, x_max, y_max = face_data["bounding_box"]
        dominant_emotion = face_data["dominant_emotion"]

        if show_emotions and dominant_emotion:
            emotion_position = (x_min, y_min - 10)
            annotated_frame = draw_rectangle(annotated_frame, dominant_emotion, emotion_position)

    return face_data_list, annotated_frame

def process_frame(frame, display_width, display_height, show_keypoints, show_emotions):
    """
    Processes the full frame, resizing and processing facial data.
    
    Args:
    - frame: The frame to be processed.
    - display_width: Desired width for display.
    - display_height: Desired height for display.
    - show_keypoints: If true, displays keypoints on the frame.
    - show_emotions: If true, displays emotions on the frame.

    Returns:
    - List of face data and display frame.
    """
    
    resized_frame = resize_frame(frame, width=display_width, height=display_height)
    face_data_list, display_frame = process_face_data(resized_frame, show_keypoints, show_emotions)
    return face_data_list, display_frame

def update_display(frame, messages, display_width, show_help):
    """
    Updates the window display with the processed frame and messages.
    
    Args:
    - frame: The frame to be displayed.
    - messages: Messages to be added to the frame.
    - display_width: Desired width for display.
    - show_help: If true, displays help messages.

    Returns:
    - None
    """
    
    frame_with_messages = add_messages_to_frame(frame, messages, display_width, show_help)
    cv2.imshow('Player', frame_with_messages)

def handle_user_input(pause, show_keypoints, show_emotions, show_help):
    """
    Handles user input via pressed keys.
    
    Args:
    - pause: Whether the video is paused or not.
    - show_keypoints: If true, displays keypoints on the frame.
    - show_emotions: If true, displays emotions on the frame.
    - show_help: If true, displays help messages.

    Returns:
    - Action to be taken based on pressed key and display states.
    """
    
    key = cv2.waitKey(1) & 0xFF
    return handle_key_press(key, pause, show_keypoints, show_emotions, show_help)
