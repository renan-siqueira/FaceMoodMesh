import cv2


def resize_frame(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Resizes an image to the specified dimensions, maintaining its aspect ratio.

    Parameters:
    - image (ndarray): The image to be resized.
    - width (int, optional): The desired width of the resized image. If None, will be calculated based on provided height.
    - height (int, optional): The desired height of the resized image. If None, will be calculated based on provided width.
    - inter (int, optional): Interpolation method to be used. Default is cv2.INTER_AREA.

    Returns:
    - ndarray: Resized image.
    """
    
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


def draw_rectangle(frame, text, position, margin=5):
    """
    Draws a rectangle with text inside on a given image.

    Parameters:
    - frame (ndarray): The image where the rectangle with text will be drawn.
    - text (str): The text to be drawn inside the rectangle.
    - position (tuple): The position (x, y) where the bottom-left corner of the text will be placed.
    - margin (int, optional): The margin around the text inside the rectangle. Default is 5.

    Returns:
    - ndarray: Image with the rectangle and text drawn.
    """
    
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    text_width = text_size[0] + 2 * margin
    text_height = text_size[1] + 2 * margin

    text_x, text_y = position
    bg_rect = (text_x, text_y - text_height, text_width, text_height)
    cv2.rectangle(frame, bg_rect, (0, 0, 0), -1)
    cv2.putText(frame, text, (text_x + margin, text_y - margin), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return frame
