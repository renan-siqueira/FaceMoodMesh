import cv2
import mediapipe as mp
from deepface import DeepFace
from utils.helpers import load_json
from config.settings import PATH_EMOTION_TRANSLATION_FILE


def detect_faces(image):
    """
    Detects faces in an image.

    Parameters:
    - image (ndarray): The image on which face detection will be performed.

    Returns:
    - list: A list containing landmarks of the detected face, if any.
    """

    mp_face_mesh = mp.solutions.face_mesh

    with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=100, min_detection_confidence=0.2) as face_mesh:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

    return results.multi_face_landmarks if results.multi_face_landmarks else []


def get_face_bounding_box(face_landmarks, image_width, image_height):
    """
    Gets the bounding box around a face based on its landmarks.

    Parameters:
    - face_landmarks (list): List of face landmarks.
    - image_width (int): Image width.
    - image_height (int): Image height.

    Returns:
    - tuple: Coordinates (x_min, y_min, x_max, y_max) of the bounding box.
    """

    x_min, y_min = image_width, image_height
    x_max, y_max = 0, 0

    for landmark in face_landmarks.landmark:
        x, y = int(landmark.x * image_width), int(landmark.y * image_height)
        x_min, y_min = min(x, x_min), min(y, y_min)
        x_max, y_max = max(x, x_max), max(y, y_max)

    return x_min, y_min, x_max, y_max


def analyze_emotions(face_crop_no_points):
    """
    Analyzes the emotions of a face.

    Parameters:
    - face_crop_no_points (ndarray): Face image without the landmarks.

    Returns:
    - str: The dominant detected emotion, if any.
    """

    try:
        emotion_analysis = DeepFace.analyze(face_crop_no_points, actions=['emotion'], enforce_detection=False)
        if isinstance(emotion_analysis, list):
            emotion_analysis = emotion_analysis[0]

        emotion_translation = load_json(PATH_EMOTION_TRANSLATION_FILE)

        dominant_emotion = emotion_analysis['dominant_emotion']
        dominant_emotion_pt = emotion_translation.get(dominant_emotion, 'None')

        return dominant_emotion_pt.capitalize()
    except:
        return 'None'
    

def is_human_face(image, draw_keypoints=True, detect_emotions=True):
    """
    Checks for human faces in the image and, if found, processes and extracts information.

    Parameters:
    - image (ndarray): The image to be processed.
    - draw_keypoints (bool, optional): If True, draws landmarks on the face. Default is True.
    - detect_emotions (bool, optional): If True, detects emotions on the face. Default is True.

    Returns:
    - list: A list containing information of each detected face, such as dominant emotion and cropped images.
    """
    
    mp_drawing = mp.solutions.drawing_utils

    face_data = []
    face_landmarks_list = detect_faces(image)
    height, width, _ = image.shape

    for face_landmarks in face_landmarks_list:
        image_copy = image.copy()

        if draw_keypoints:
            landmark_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
            connection_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
            
            mp_drawing.draw_landmarks(image, face_landmarks, mp.solutions.face_mesh.FACEMESH_TESSELATION,
                                      landmark_drawing_spec=landmark_drawing_spec,
                                      connection_drawing_spec=connection_drawing_spec)

        x_min, y_min, x_max, y_max = get_face_bounding_box(face_landmarks, width, height)

        face_crop_no_points = image_copy[y_min:y_max, x_min:x_max]
        face_crop_with_points = image[y_min:y_max, x_min:x_max]

        if detect_emotions:
            dominant_emotion = analyze_emotions(face_crop_no_points)
        else:
            dominant_emotion = None

        face_data.append({
            "annotated_image": image,
            "face_crop_no_points": face_crop_no_points,
            "face_crop_with_points": face_crop_with_points,
            "dominant_emotion": dominant_emotion,
            "bounding_box": (x_min, y_min, x_max, y_max)
        })

    return face_data
