import cv2
import numpy as np
from logging import Logger

class BaseImage:
    '''We need base image to be able to work with high resolution images. 
    The first step of this class is to upsample the image.
    The second step is to blur the image to smooth the image and remove noise from it.
    We also need to adjust the sigma parameter to adjust the blurriness according the scale of an image
    '''
    def __init__(self, image, sigma, assumed_blur):
        self.image = image
        self.sigma = sigma
        self.assumed_blur = assumed_blur

    def CreateBaseImage(self):
        # upsample the image
        upsampled_image = cv2.resize(self.image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        #adjust the sigma parameter
        total_sigma = np.sqrt(max((self.sigma ** 2) - ((2 * self.assumed_blur) ** 2), 0.01))

        #Apply Gaussian Blur to upsampled image to adjust for the increased resolution
        blurred_image = cv2.GaussianBlur(upsampled_image, (0, 0), sigmaX=total_sigma, sigmaY=total_sigma)
        
        return blurred_image
    

if __name__ == "__main__":
    image = r"C:/Users/49179/Desktop/12.jpg"
    image = cv2.imread(image)
    baseimage = BaseImage(image, sigma = 1.6, assumed_blur=0.3)
    base = baseimage.CreateBaseImage()
    cv2.imshow("Base_Image",base)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
