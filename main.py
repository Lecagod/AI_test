import cv2
import numpy as np
import os
import imutils
from imutils.video import FPS
from imutils.video import VideoStream
import face_recognition
import pickle
import threading

vs = VideoStream(src=0, framerate=30).start()

currentname = "unknown"
# Xác định các khuôn mặt từ file encodings.pickle được tạo từ chương trình TrainAI
encodingsP = "encodings.pickle"
cascade = "haarcascade_frontalface_default.xml"

# Đọc dữ liệu khuôn mặt đã được mã hóa và load file cascade
data = pickle.loads(open(encodingsP, "rb").read())
detector = cv2.CascadeClassifier(cascade)

fps = FPS().start()

while True:
    # Lấy Frame từ luồng video và thay đổi thành 500 pixel để xử lý nhanh hơn
    frame = vs.read()
    frame = imutils.resize(frame, width=500)

    # Chuyển đổi Frame từ BGR sang Gray để phát diện khuôn mặt
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Chuyển đổi Frame từ BGR sang RGB để nhận diện khuôn mặt
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Phát hiện khuôn mặt khi chuyển đổi Frame sang Gray
    rects = detector.detectMultiScale(gray, scaleFactor=1.3,
                                      minNeighbors=5, minSize=(30, 30),
                                      flags=cv2.CASCADE_SCALE_IMAGE)

    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    # So sánh khuôn mặt được đưa vào từ camera với dữ liệu khuôn mặt đã được train cho AI
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        name = "Unknown"

        # Kiểm tra xem nếu khuôn mặt được đưa vào từ camera với dữ liệu khuôn mặt trùng nhau
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            # Xác định tên sẽ được hiện
            name = max(counts, key=counts.get)

            if currentname != name:
                currentname = name
                print(currentname)

        names.append(name)

        for ((top, right, bottom, left), name) in zip(boxes, names):
            # Vẽ khung để hiển thị tên khuôn mặt
            cv2.rectangle(frame, (left, top), (right, bottom),
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
