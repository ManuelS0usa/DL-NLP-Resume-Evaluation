# https://www.superdatascience.com/blogs/opencv-face-detection
# https://www.stackovercloud.com/2019/03/28/how-to-detect-and-extract-faces-from-an-image-with-opencv-and-python/

import cv2
import sys
from default_settings import *


class Image():
            
    def __init__(self, imageName):
        self.imageName = imageName
    
    def detect(self):
        """
            Images saved:
            1_ : original imaged exported from pdf file
            2_ : detect face with rectangular green square on original image
            3_ : detected face cropped
        """
                         
        imagePath = "./" + DEFAULT_OPENCV_FOLDER + "/1_" + self.imageName
        # read image
        image = cv2.imread(imagePath)
        # convert rgb image to gray
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # apply face detector classifier
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
           gray,
           scaleFactor=1.3,
           minNeighbors=3,
           minSize=(30, 30)
        )
        
        for (x, y, w, h) in faces:
            # draw rectangles on face detected
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = image[y:y + h, x:x + w]
            # Cut image according to rectangle coordinates and save
            cv2.imwrite("./" + DEFAULT_OPENCV_FOLDER + "/3_" + self.imageName, roi_color)
            # Save image on results folder also
            cv2.imwrite("./" + DEFAULT_RESULTS + "/" + self.imageName[:-4] + "_image" + self.imageName[-4:] , roi_color)
        
        # save image with rectangle detection
        cv2.imwrite("./" + DEFAULT_OPENCV_FOLDER + "/2_" + self.imageName, image)  
           
        # Read image and show on window
#         self.show(2)
            
            
    def show(self, photoID):
        """ (integer) photoID: 1, 2 or 3 """        
        # The function cv2.imread() is used to read an image.
        img = cv2.imread("./" + DEFAULT_OPENCV_FOLDER + "/" + str(photoID) + "_" + self.imageName)            
        # display an image in a window.
        cv2.imshow("Face Detected", img)
        # waits for a key press to close the window and 0 specifies indefinite loop
        cv2.waitKey(0)
        # simply destroys all the windows we created.
        cv2.destroyAllWindows()
            