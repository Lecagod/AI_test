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
        train_list = db.get_list(cursor)
        return train_list
    
    #update state in DB
    def update_state(data):
        db.update_state(cnx,data[0],data[1])
    
    #get image path
    def getImagePath(name):
        return os.getcwd()+f"\\dataset\\{name}\\"
        
        
    # function to get the images and label data
    def getImagesAndLabels(listname):
        imageNames =[]
        listID =[]
        for id,name,msv in listname:
            path = getImagePath(name)
            listImages= os.listdir(path)
            for i in range(len(listImages)):
                listImages[i]= path+listImages[i]
                listID.append(id)
            imageNames.extend(listImages)
       
        # print(imageNames)
        faceSamples=[]
        ids = []
        print(listID)
        for id in range(len(imageNames)):
            
            # print(imageNames[i])
            PIL_img = Image.open(imageNames[id]).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')

            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(listID[id])

        return faceSamples,ids

    print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    
    #list name to train
    list_name = get_list_train()
      
    faces,ids = getImagesAndLabels(list_name)
    
    recognizer.train(faces, np.array(ids))
   
    # Save the model into trainer/trainer.yml
    if not os.path.exists("trainer"):
        os.makedirs("trainer")
    recognizer.write('trainer/trainer.yml')       
        
    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    db.close_cnc(cnx)