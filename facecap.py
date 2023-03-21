import cv2

name = 'TranVanPhuc' #Thaybangtennguoimuonluudulieu

cam = cv2.VideoCapture(0)

cv2.namedWindow("Nhan s de luu anh", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Nhan s de luu anh", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Nhan s de luu anh", frame)

    k = cv2.waitKey(1)
    if k == ord("q"):
        # Nhan nut q
        print("Dang dong chuong trinh")
        break
    elif k == ord("s"):
        # nhan nut s
        img_name = "Faces/"+ name +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
