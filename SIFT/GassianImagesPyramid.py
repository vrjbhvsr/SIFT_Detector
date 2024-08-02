import numpy as np
import cv2
from GaussianKernels import GaussianKernels
from BaseImage import BaseImage
from NumberOfOctaves import NumberOfOctaves


class GaussianImages:
    def __init__(self, image, num_octaves, kernels):
        self.image = image
        self.num_octaves = num_octaves
        self.kernels = kernels

    def ComputeGaussianImages(self):
        Gaussian_image_pyramid = []
        current_image = self.image
        for octave in range(self.num_octaves):
            Gaussian_images_in_octave = [current_image]
            for kernel in self.kernels[1:]:
                blurred_image = cv2.GaussianBlur(Gaussian_images_in_octave[-1], (0, 0), sigmaX=kernel, sigmaY=kernel)
                Gaussian_images_in_octave.append(blurred_image)
            Gaussian_image_pyramid.append(Gaussian_images_in_octave)
            new_octave_base_image = Gaussian_images_in_octave[2]
            current_image = cv2.resize(new_octave_base_image, (int(new_octave_base_image.shape[1] / 2), int(new_octave_base_image.shape[0] / 2)))
        return Gaussian_image_pyramid
    
if __name__ == '__main__':
    image = r"C:/Users/49179/Desktop/jam-2932909_640.jpg"
    image = cv2.imread(image)
    if image is None:
        print("Error: Image not found!")
    else:
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY).astype(np.float32)
        gray_image = gray_image/255.
    
    
    
    baseimage = BaseImage(gray_image, sigma = 1.6, assumed_blur=0.3)
    base = baseimage.CreateBaseImage()
    
    # Define the number of octaves and the Gaussian kernels
    num_octaves = NumberOfOctaves(base).ComputeOctaves()
    kernels = GaussianKernels(s=2, sigma=1.6).CreateGaussianKernels()
    print(kernels)
    
    # Create a GaussianImages object
    gaussian_images = GaussianImages(base, num_octaves, kernels).ComputeGaussianImages()
    # Display the Gaussian pyramid
    for octave, images in enumerate(gaussian_images):
        for i, image in enumerate(images):
            cv2.imshow(f'Octave {octave+1}, Gaussian Kernel {i+1}', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
            
