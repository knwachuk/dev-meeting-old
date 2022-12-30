import cv2 as cv
from typing import Tuple

def get_intensity(frame) -> Tuple:
    """Converts the frame to gray, computes the frame histogram, and the global (tonal 128 plus) intensity of a frame."""
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_hist = cv.calcHist([frame_gray], [0], None, [256], [0, 256])

    # Get half sum from frame histogram (discard low tonal range)
    tonal_128_plus = np.sum(frame_hist[len(frame) // 2 :])

    return frame_gray, frame_hist, tonal_128_plus
