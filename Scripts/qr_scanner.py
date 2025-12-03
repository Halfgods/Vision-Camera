import cv2
import numpy as np

def decode_qr(image):
    """
    Detects and decodes a QR code from an image.
    Returns:
        - decoded_text: The string data from the QR (or None if not found)
        - result_image: The image with the QR code bounding box drawn (or original if not found)
    """
    # Initialize QRCode detector
    detector = cv2.QRCodeDetector()
    
    # Detect and decode
    data, bbox, straight_qrcode = detector.detectAndDecode(image)
    
    result_image = image.copy()
    
    if bbox is not None and data:
        # Draw bounding box
        n = len(bbox)
        for i in range(n):
            # bbox is a list of arrays of points, we need to iterate through it
            # OpenCV 4.x returns bbox as shape (1, 4, 2)
            points = bbox[i].astype(int)
            for j in range(len(points)):
                pt1 = tuple(points[j])
                pt2 = tuple(points[(j+1) % len(points)])
                cv2.line(result_image, pt1, pt2, (0, 255, 0), 3) # Green box
        
        # Put text
        cv2.putText(result_image, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    
        return data, result_image
    
    return None, image
