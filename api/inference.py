from datetime import datetime

from numpy import ndarray


def classify_image(image: ndarray) -> int:
    now = datetime.now()
    return now.hour % 12