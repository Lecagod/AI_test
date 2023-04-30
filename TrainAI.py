import cv2
import numpy as np
from PIL import Image
import os
import access_database as db

def TRAIN_DATA():
    #connect
    cnx = db.connect_to_db('127.0.0.1','root','vlo136fv',1306,'face_data')
    cursor = cnx.cursor()
    # Path for face image database

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #get list data not train
    def get_list_train():
        train_list = db.get_list_to_train(cursor)
        return train_list
    
    #update state in DB
    def update_state(data):
        db.update_state(cnx,data[0],data[1])
    
    #get image path
    def getImagePath(name):
        return os.getcwd()+f"\\dataset\\{name}\\"
        
        
    # function to get the images and label data
    def getImagesAndLabels(path):

        # imagePaths = [os.path.join(path,f) for f in os.listdir(path)] # chỉnh sửa đường dẫn
        imageNames =os.listdir(path)
        print(imageNames)
        faceSamples=[]
        ids = []

        for imageName in imageNames:
            imagePath = path+imageName
            print(imagePath)
            PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids

    print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    
    #list name to train
    list_name = get_list_train()
    print(list_name)
    for name in list_name:
        print(name)
        path = getImagePath(name[0])
        print(path)
        faces,ids = getImagesAndLabels(path) #faces = name/
        recognizer.train(faces, np.array(ids)) # train ??

        # Save the model into trainer/trainer.yml
        if not os.path.exists("trainer"):
            os.makedirs("trainer")
        recognizer.write('trainer/trainer.yml')
        
        update_state(name)

    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    db.close_cnc(cnx)