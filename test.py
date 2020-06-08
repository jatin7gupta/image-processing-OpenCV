import cv2


def read_image(path):
    img = cv2.imread(path, 0)
    return img


def display_image(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def top_left(r, c, img_h, img_w):
    if 0 <= r < img_h and 0 <= c < img_w:
        return r, c
    else:
        return top_left(r+1, c+1, img_h, img_w)


def top_right(r, c, img_h, img_w):
    if 0 <= r < img_h and 0 <= c < img_w:
        return r, c
    else:
        return top_right(r+1, c-1, img_h, img_w)


def bottom_left(r, c, img_h, img_w):
    if 0 <= r < img_h and 0<= c < img_w:
        return r, c
    else:
        return bottom_left(r-1, c+1, img_h, img_w)


def bottom_right(r, c, img_h, img_w):
    if 0 <= r < img_h and 0 <= c < img_w:
        return r, c
    else:
        return bottom_right(r-1, c-1, img_h, img_w)


# this function will return 4 coordinates row_from, row_to, col_from, col_to
def get_coordinates(r, c, img_h, img_w, N):
    row_from, col_from = top_left(r-N//2, c-N//2, img_h, img_w)

    row_to, col_to = bottom_right(r+N//2, c+N//2, img_h, img_w)
    return row_from, row_to, col_from, col_to


def slice_matrix(img_h, img_w):
    for r in range(img_h):
        for c in range(img_w):
            print(get_coordinates(r,c, img_h, img_w, 5))


def max_filtered_image(img):
    r, c = img.shape
    slice_matrix(r, c)


path = 'COMP9517_20T2_Assignment_Images/Particles.png'
image_a = read_image(path)
max_filtered_image(image_a)

display_image(image_a, 'image_a')