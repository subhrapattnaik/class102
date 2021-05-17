import cv2
import dropbox
def take_snapshot():
 #initializing cv2
 videoCaptureObject =cv2.VideoCapture(0)
 result = True
 while(result):
 #read the frames while the camera is on
   ret,frame = videoCaptureObject.read()
   print(ret)
   #cv2.imwrite() method is used to save an image to any storage device
   cv2.imwrite("./102/picture.jpg",frame)
   result = False
 # releases the camera
 videoCaptureObject.release()
 #closes all the window that might be opened while this process
 cv2.destroyAllWindows()

take_snapshot()
