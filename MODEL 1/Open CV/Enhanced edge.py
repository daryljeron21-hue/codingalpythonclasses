import cv2
import numpy as np
import matplotlib.pyplot as plt

image = input("Enter the path to the image: ")
def display_image(title, image):
    """"Utility function to display an image."""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    plt.title(title)
    plt.axis('off')
    plt.show()
laplacian_image=input("Enter 'yes' for Laplacian edge detection: ")
if laplacian_image == "yes":
    def laplacian_edge_detection(image_path):
            """Function to perform Laplacian edge detection"""
            image = cv2.imread(image_path)
            if image is None:
                print("Error: Image not found!")
            return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)

    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
    display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))
else:
    print("Laplacian edge detection skipped.")
    print("Thanks for using the program!")