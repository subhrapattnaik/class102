import cv2
import dropbox
import time
import random


#print(time.time())
#print(random.randint(0,9))

start_time=time.time()

def take_snapshot():
 number=random.randint(0,100)
 #initializing cv2
 videoCaptureObject =cv2.VideoCapture(0)
 result = True
 while(result):
   #read the frames while the camera is on
   ret,frame = videoCaptureObject.read()
   img_name="img"+str(number)+".png"
   #cv2.imwrite() method is used to save an image to any storage device
   cv2.imwrite(img_name,frame)
   start_time=time.time
   result = False

 return img_name
 print("snapshot taken")
 # releases the camera
 videoCaptureObject.release()
 #closes all the window that might be opened while this process
 cv2.destroyAllWindows()


def upload_file(img_name):
    #access_token="sl.Aw8e5HJaWTB-0cyf4xCQfFfAhfbGgaboUkJokVvid3XO9pzCGzWE0nxZK8AVVSaobG0C-7bSETPa6t0at-DfwfHIV7pEOK5pJDR2Z0kSXh0ECXnLRKtfxo9Lxs4wzNrO9B0gvk0"
    access_token="JQYxA-3ju2YAAAAAAAAAAQ4jdMxFoHX_L9IV44ZV9c3qiAns_FmhQ_TW1ffc3kIO"
    #access_token ='sl.Aw7ghgTCHfA6-oXflve7Cwmw9sabD9ve6vOGz0LGm2F8Jp_VbjPAHYyiQjG4vF6dYAoBNF0tdoIYGznzxlF57MAAEmG2pwH56WFwaqho1X5q11nRc2zyf3xS9AoFCf-Zo6UJenXmYdZC'
  
    file=img_name
    file_from=file
    file_to="/CaptureAndUploadImg/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()
