import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    
    return img_name
    print("Snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BHCZMHyrl2yW6Ode0Ol4Zxhl7ZKEomjW3OmU7Gz8351qEVysf5Yhe2CgpmfEnclbsL9KM2D8Up2EH3y9YsdH15xOZJhL7S7dCoKsDoNphxqq2KhL4iLKLvv5axjbdEhpKh1H2xqMucvP"
    file = img_name
    file_from = file
    file_to = "/testfolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to,mode = dropbox.files.WriteMode.overwrite)
        print("Files uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)

main()

