import cv2
import numpy as np
from task1 import read_image, display_image, max_filtered_image, min_filtered_image, N
from task2 import max_min


def min_max(I, N=3):
    B = min_filtered_image(I, N)
    A = max_filtered_image(B, N)
    O = cv2.subtract(I, A)
    return O


def task3(I, M=0, N=3):
    if M == 0:
        return max_min(I, N)
    elif M == 1:
        return min_max(I, N)


if __name__ == '__main__':
    path = 'COMP9517_20T2_Assignment_Images/Cells.png'
    I = read_image(path)
    O = task3(I, 0, N)
    display_image(O, 'm=0')

    O = task3(I, 1, N)
    display_image(O, 'm=1')
