import cv2
import numpy as np
from task1 import min_filtered_image, max_filtered_image, path, read_image, display_image, N


def max_min(I, N=3):
    A = max_filtered_image(I, N)
    B = min_filtered_image(A, N)
    O = np.zeros(I.shape).astype('uint8')
    # cv2.subtract(I, B, dst=O)
    O = I - B + 255
    return O#.astype('uint8')


if __name__ == '__main__':
    I = read_image(path)
    O = max_min(I, N)
    display_image(O, 'O')