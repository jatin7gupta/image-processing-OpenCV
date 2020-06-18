import cv2
import numpy as np
import sys


def read_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return img


def display_image(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def max_filtered_image(img, N):
    img_row, img_col = img.shape
    N_row, N_col = N, N

    A = np.zeros(img.shape)

    pad_height = N_row // 2
    pad_width = N_col // 2

    # zero image ie zero 2d array
    padded_image = np.zeros((img_row + (2 * pad_height), img_col + (2 * pad_width)))

    # embedding input image in padded image
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = img

    for row in range(img_row):
        for col in range(img_col):
            A[row, col] = np.amax(padded_image[row:row + N_row, col:col + N_col])

    return A.astype('uint8')


def min_filtered_image(img, N=3):
    img_row, img_col = img.shape
    N_row, N_col = N, N

    A = np.zeros(img.shape)

    pad_height = N_row // 2
    pad_width = N_col // 2

    # zero image ie zero 2d array
    padded_image = np.zeros((img_row + (2 * pad_height), img_col + (2 * pad_width)))
    padded_image = padded_image + 255

    # embedding input image in padded image
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = img

    for row in range(img_row):
        for col in range(img_col):
            A[row, col] = np.amin(padded_image[row:row + N_row, col:col + N_col])

    return A.astype('uint8')


path = 'COMP9517_20T2_Assignment_Images/Particles.png'

if __name__ == '__main__':
    I = read_image(path)
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
        if N % 2 == 1:
            A = max_filtered_image(I, N)
            B = min_filtered_image(A, N)
            cv2.imwrite(f'task1_A_N_{N}.jpg', A)
            print(f'task1_A_N_{N}.jpg saved in root.')
            cv2.imwrite(f'task1_B_N_{N}.jpg', B)
            print(f'task1_B_N_{N}.jpg saved in root.')
        else:
            print('Use command line args. N as an odd integer N > 1')
    else:
        print('Use command line args. N as an odd integer')


