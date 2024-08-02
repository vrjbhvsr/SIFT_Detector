import cv2
import numpy as np
from BaseImage import BaseImage
from NumberOfOctaves import NumberOfOctaves
from GaussianKernels import GaussianKernels
from GassianImagesPyramid import GaussianImages

class Difference_of_Gaussian:
    def __init__(self, num_octaves, Gaussian_pyramid):
        self.num_octaves = num_octaves
        self.gaussian_pyramid = Gaussian_pyramid
    
    def DoG(self):
        DoG_pyramid = []
        for octave, images in enumerate(self.gaussian_pyramid):
            DoG_octave = []
            for scale in range(1,len(images)):
                difference = images[scale] - images[scale-1]
                DoG_octave.append(difference)
            print(octave, len(DoG_octave))
            DoG_pyramid.append(DoG_octave)
        return DoG_pyramid
    

if __name__ == "__main__":
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
        
        # Compute DoG images
    DoG_pyramid = Difference_of_Gaussian(num_octaves=num_octaves, Gaussian_pyramid=gaussian_images ).DoG()
        
        # Optionally display the DoG images
    for octave_index, DoG_images in enumerate(DoG_pyramid):
            for scale_index, DoG_image in enumerate(DoG_images):
                cv2.imshow(f'Octave {octave_index + 1}, DoG {scale_index + 1}', DoG_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
