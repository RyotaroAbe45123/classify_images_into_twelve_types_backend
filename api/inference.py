from time import sleep

import numpy as np
from numpy import ndarray


def classify_image(image: ndarray) -> int:
    # 判定ロジックをここに書く
    # 画像の画素値を使って判定する
    sleep(2)
    # RGBの平均値
    img_avg = np.mean(image, axis=2)
    # 画素値の平均値
    img_sum = np.int64(np.mean(img_avg))
    # 12で割った余り
    image_type= img_sum % 12
    return int(image_type)