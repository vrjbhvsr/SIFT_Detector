import numpy as np
import cv2
from BaseImage import BaseImage

class NumberOfOctaves:
    def __init__(self, base_image, minIMageSize = 16):
        self.base_image = base_image
        self.minImageSize = minIMageSize
        self.octaves = []

    def ComputeOctaves(self):
        # Defining image size
        image_shape = self.base_image.shape[:2]

        #Determine the smaller Dimension
        min_dim = min(image_shape)

        # Compute the Number of octaves
        num_octaves = int(np.log2(min_dim/self.minImageSize))+ 1

        return num_octaves


if __name__ == "__main__":
    image = r"C:/Users/49179/Desktop/12.jpg"
    image = cv2.imread(image)
    baseimage = BaseImage(image, sigma = 1.6, assumed_blur=0.3)
    base = baseimage.CreateBaseImage()
    octaves = NumberOfOctaves(base).ComputeOctaves()