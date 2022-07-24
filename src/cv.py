import cv2
import sys


class Image():
            
    def __init__(self, imageName):
        self.imageName = imageName
    
    def detect(self):
         # Face detect and save            
            imagePath = "./opencv_images/1_" + self.imageName
            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(30, 30)
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_color = image[y:y + h, x:x + w]
                cv2.imwrite("./opencv_images/3_" + self.imageName, roi_color)
    
            cv2.imwrite("./opencv_images/2_" + self.imageName, image)
                           
            # The function cv2.imread() is used to read an image.
            img = cv2.imread("./opencv_images/2_" + self.imageName)
            # The function cv2.imshow() is used to display an image in a window.
#             cv2.imshow("Image", img)
            
    
#             image2 = mpimg.imread("oioi.png")
#             print(image2)
#             plt.imshow(image2)
#             plt.show()
            

#             image = mpimg.imread("opencv_images/3_" + res['filename'].replace(".pdf", "") + ".jpg")
#             plt.imshow(image)
#             plt.show()

#             waitKey() waits for a key press to close the window and 0 specifies indefinite loop
#             cv2.waitKey(0)
#             cv2.destroyAllWindows() simply destroys all the windows we created.
#             cv2.destroyAllWindows()