import cv2
import sys
import numpy as np
from task1 import read_image, max_filtered_image, min_filtered_image
from task2 import max_min


def min_max(I, N=3):
    B = min_filtered_image(I, N)
    A = max_filtered_image(B, N)
    O = np.zeros(I.shape).astype('uint8')
    O = I - A
    return O, A


def task3(I, M=0, N=3):
    if M == 0:
        return max_min(I, N)
    elif M == 1:
        return min_max(I, N)


if __name__ == '__main__':
    path = 'COMP9517_20T2_Assignment_Images/Cells.png'
    I = read_image(path)
    if len(sys.argv) == 3:
        N = int(sys.argv[1])
        M = int(sys.argv[2])
        I = read_image(path)

        # check for M and N
        if N % 2 == 1 and (M == 0 or M == 1):
            if M == 0:
                O, background = task3(I, M, N)

                cv2.imwrite(f'task3_N_{N}_M_{M}.png', O)
                print(f'task3_N_{N}_M_{M}.png saved in root.')

                cv2.imwrite(f'task3_N_{N}_M_{M}_background.png', background)
                print(f'task3_N_{N}_M_{M}_background.png saved in root.')
            else:
                O, background = task3(I, M, N)

                cv2.imwrite(f'task3_N_{N}_M_{M}.png', O)
                print(f'task3_N_{N}_M_{M}.png saved in root.')

                cv2.imwrite(f'task3_N_{N}_M_{M}_background.png', background)
                print(f'task3_N_{N}_M_{M}_background.png saved in root.')
        else:
            print('Use command line args. N: an odd integer N > 1 and M: either 0 or 1')
    else:
        print('Use command line args. N and M as integer')