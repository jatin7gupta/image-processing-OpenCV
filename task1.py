import cv2
import numpy as np


def read_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return img


def display_image(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def max_filtered_image(img, M):
    img_row, img_col = img.shape
    M_row, M_col = M, M

    A = np.zeros(img.shape)

    pad_height = M_row // 2
    pad_width = M_col // 2

    # zero image ie zero 2d array
    padded_image = np.zeros((img_row + (2 * pad_height), img_col + (2 * pad_width)))

    # embedding input image in padded image
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = img

    for row in range(img_row):
        for col in range(img_col):
            A[row, col] = np.max(padded_image[row:row + M_row, col:col + M_col])

    return A.astype('uint8')


if __name__ == '__main__':
    path = 'COMP9517_20T2_Assignment_Images/Particles.png'
    I = read_image(path)
    display_image(I, 'I')
    display_image(max_filtered_image(I, 15), 'max filtered image')