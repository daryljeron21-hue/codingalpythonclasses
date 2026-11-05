import cv2

image = cv2.imread("Pixel_Art.jpg")
height, width, _ = image.shape

w_part = width // 3

part1_vert = image[:, :w_part]
part2_vert = image[:, w_part:w_part*2]
part3_vert = image[:, w_part*2:]

h_part = height // 3

part1_horiz = image[:h_part, :]
part2_horiz = image[h_part:h_part*2, :]
part3_horiz = image[h_part*2:, :]

cv2.imwrite("Pixel_Art.jpg", part1_vert)