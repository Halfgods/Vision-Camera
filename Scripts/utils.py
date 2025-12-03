import cv2
import numpy as np
from PIL import Image

def load_image(image_file):
    """
    Converts a Streamlit file upload or camera input (PIL/Bytes) to an OpenCV image (numpy array).
    """
    if image_file is None:
        return None
    
    # Convert to PIL Image
    img = Image.open(image_file)
    
    # Convert to numpy array
    img_array = np.array(img)
    
    # Convert RGB to BGR (OpenCV standard)
    # Check if image has alpha channel
    if img_array.shape[-1] == 4:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2BGR)
    else:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
    return img_array

def to_streamlit_image(cv2_img):
    """
    Converts an OpenCV image (BGR) back to RGB for Streamlit display.
    """
    return cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

def resize_image(image, width=None, height=None):
    """
    Resizes an image while maintaining aspect ratio.
    """
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized
