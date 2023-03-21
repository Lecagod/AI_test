import cv2
import numpy as np
import os
import imutils
from imutils.video import FPS
from imutils.video import VideoStream
import face_recognition
import pickle
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection

vs = VideoStream(src=0, framerate=30).start()

currentname = "unknown"
#Xác định các khuôn mặt từ file encodings.pickle được tạo từ chương trình TrainAI

encodingsP = "encodings.pickle"

#Đọc dữ liệu khuôn mặt đã được mã hóa và load file cascade
data = pickle.loads(open(encodingsP, "rb").read())

fps = FPS().start()

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:

    while True:
        #Lấy Frame từ luồng video và thay đổi thành 500 pixel để xử lý nhanh hơn
        frame = vs.read()
        frame = imutils.resize(frame, width=500)

        #Chuyển đổi Frame từ BGR sang RGB để nhận diện khuôn mặt
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #Phát hiện khuôn mặt sử dụng MediaPipe
        results = face_detection.process(rgb)

        boxes = []
        encodings = []
        names = []

        #So sánh khuôn mặt được đưa vào từ camera với dữ liệu khuôn mặt đã được train cho AI
        if results.detections:
            for detection in results.detections:
                box = detection.location_data.relative_bounding_box
                h, w, c = frame.shape
                bounding_box = int(box.xmin*w), int(box.ymin*h), \
                               int(box.width*w), int(box.height*h)

                boxes.append(bounding_box)

                # Chiết xuất Feature của khuôn mặt sử dụng Face Recognition
                face = frame[bounding_box[1]:bounding_box[1]+bounding_box[3],
                             bounding_box[0]:bounding_box[0]+bounding_box[2]]
                rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                encoding = face_recognition.face_encodings(rgb_face)
                if encoding:
                    encodings.append(encoding)

            # So sánh các Feature
            for encoding in encodings:
                matches = face_recognition.compare_faces(
                    data["encodings"], encoding[0])
                name = "Unknown"

                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    #Xác định tên sẽ được hiện
                    name = max(counts, key=counts.get)

                    if currentname != name:
                        currentname = name
                        print(currentname)

                names.append(name)

            for ((left, top, width, height), name) in zip(boxes, names):
                # Vẽ khung để hiển thị tên khuôn mặt
                cv2.rectangle(frame, (left, top), (left+width, top+height),
                              (0, 255, 225), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                            .8, (0, 255, 255), 2)

        cv2.imshow("Nhan dien khuon mat dang duoc chay", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()