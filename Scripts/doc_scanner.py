import cv2
import numpy as np
from .utils import resize_image

def order_points(pts):
    """
    Orders coordinates: top-left, top-right, bottom-right, bottom-left.
    """
    rect = np.zeros((4, 2), dtype="float32")
    
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    
    return rect

def four_point_transform(image, pts):
    """
    Applies perspective transform to obtain a top-down view of the document.
    """
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    
    # Compute width of new image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    
    # Compute height of new image
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
        
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    return warped

def scan_document(image):
    """
    Detects document edges and applies perspective transform.
    Returns:
        - warped: The scanned document image
        - original_with_contours: The original image with detected contours drawn
    """
    # Resize for faster processing, keep ratio
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image_resized = resize_image(image, height=500)
    
    # Grayscale, Blur, Canny
    gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)
    
    # Find Contours
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    
    screenCnt = None
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        
        if len(approx) == 4:
            screenCnt = approx
            break
            
    if screenCnt is None:
        # Fallback: just return original if no 4-point contour found
        return image, image
        
    # Draw contours on resized image for visualization
    debug_img = image_resized.copy()
    cv2.drawContours(debug_img, [screenCnt], -1, (0, 255, 0), 2)
    
    # Apply transform
    warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
    
    # Convert to grayscale and threshold to give it a "scanned" look
    warped_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    # Simple adaptive threshold
    T = cv2.adaptiveThreshold(warped_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                              cv2.THRESH_BINARY, 11, 2)
                              
    # Convert back to BGR so it displays correctly in Streamlit
    scanned_result = cv2.cvtColor(T, cv2.COLOR_GRAY2BGR)
    
    return scanned_result, debug_img
