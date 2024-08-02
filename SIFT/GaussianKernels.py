import cv2
import numpy as np

class GaussianKernels:
    def __init__(self, s, sigma):
        self.s = s
        self.sigma = sigma
    
    def CreateGaussianKernels(self):
        num_images_per_octave  =  self.s + 3
        k = 2 **(1.0/ self.s)
        gaussian_kernel = np.zeros(num_images_per_octave)
        gaussian_kernel = [self.sigma]

        for i in range(1, num_images_per_octave):
            sigma_prev = self.sigma * (k**(i -1))
            sigma_total = k*sigma_prev
            gaussian_kernel.append(np.sqrt(sigma_total**2-sigma_prev**2))
        return gaussian_kernel
        

if __name__ == '__main__':  
    kernels = GaussianKernels(s=3, sigma=np.sqrt(2)).CreateGaussianKernels()
    print(kernels)

