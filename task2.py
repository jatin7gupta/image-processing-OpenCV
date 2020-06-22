import cv2
import sys
import numpy as np
from task1 import min_filtered_image, max_filtered_image, path, read_image


def max_min(I, N=3):
    A = max_filtered_image(I, N)
    B = min_filtered_image(A, N)
    O = np.zeros(I.shape).astype('uint8')
    O = I - B + 255
    return O, B


if __name__ == '__main__':
    I = read_image(path)
    if len(sys.argv) == 2:
        N = int(sys.argv[1])

        # check if N is odd
        if N % 2 == 1:
            O, background = max_min(I, N)
            cv2.imwrite(f'task2_O_N_{N}.png', O)
            print(f'task2_O_N_{N}.png saved in root.')

            # optional
            O_normalized = cv2.normalize(O, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            cv2.imwrite(f'task2_O_normalized_N_{N}.png', O_normalized)
            print(f'task2_O_normalized_N_{N}.png saved in root.')

            # background
            cv2.imwrite(f'task2_background_N_{N}.png', background)
            print(f'task2_background_N_{N}.png saved in root.')
        else:
            print('Use command line args. N as an odd integer N > 1')
    else:
        print('Use command line args. N as an odd integer')