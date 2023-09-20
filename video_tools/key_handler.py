import cv2


def handle_key_press(key, pause, show_keypoints, show_emotions, show_help):
    """
    Handles the key pressed by the user to set actions in the video viewer.

    Parameters:
    - key (int): The ASCII code of the pressed key.
    - pause (bool): Indicates if the video is paused.
    - show_keypoints (bool): Indicates if facial points are being displayed.
    - show_emotions (bool): Indicates if emotions are being displayed.
    - show_help (bool): Indicates if the help menu is being displayed.

    Returns:
    - tuple: A tuple containing the action to be taken and updated states for pause, show_keypoints, show_emotions, and show_help.
    """
    
    actions = {
        ord('q'): ('break', pause, show_keypoints, show_emotions, show_help),
        ord('p'): (None, not pause, show_keypoints, show_emotions, show_help),
        ord('k'): (None, pause, not show_keypoints, show_emotions, show_help),
        ord('e'): (None, pause, show_keypoints, not show_emotions, show_help),
        ord('h'): (None, pause, show_keypoints, show_emotions, not show_help),
    }

    return actions.get(key, (None, pause, show_keypoints, show_emotions, show_help))


def add_messages_to_frame(frame, messages, display_width, show_help=True):
    """
    Adds messages (or a help menu) to a video frame.

    Parameters:
    - frame (ndarray): The current video frame.
    - messages (dict): A dictionary with messages to be displayed.
    - display_width (int): The width of the viewing display.
    - show_help (bool, optional): If True, displays the help menu. Otherwise, shows the message to press [H]. Default is True.

    Returns:
    - ndarray: The frame with the messages added.
    """
    
    frame_copy = frame.copy()

    if show_help:
        cv2.rectangle(frame_copy, (display_width - 270, 0), (display_width - 0, 30 + 30 * len(messages)), (0, 0, 0), -1)

        alpha = 0.5
        cv2.addWeighted(frame_copy, alpha, frame, 1 - alpha, 0, frame)

        for idx, (key, message) in enumerate(messages.items()):
            cv2.putText(frame, message, (display_width - 250, 30 + 30 * idx), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    else:
        cv2.rectangle(frame_copy, (5, -10), (300, 25), (0, 0, 0), -1)

        alpha = 0.5
        cv2.addWeighted(frame_copy, alpha, frame, 1 - alpha, 0, frame)
        cv2.putText(frame, "Press [H] to display the menu", (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    return frame
