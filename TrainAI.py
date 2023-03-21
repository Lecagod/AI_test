from imutils import paths
import face_recognition
import pickle
import cv2
import os

# Noi AI lay du lieu khuon mat de train
print("[INFO] start processing faces...")
imagePaths = list(paths.list_images("Faces"))

# Tạo ra danh sách khuôn mặt đã được mã hóa và tên
knownEncodings = []
knownNames = []

# Vòng giúp lấy tất cả các ảnh khuôn mặt được lưu trữ
for (i, imagePath) in enumerate(imagePaths):
	#Lây tên người từ nơi chứa dữ liệu khuôn mặt
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]

	# Chuyển định dạng ảnh từ BGR sang RGB
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# Xác định tọa độ x,y của các khung tương ứng với từng ảnh dữ liệu
	boxes = face_recognition.face_locations(rgb)

	# Trích xuất đặc trưng khuôn mặt
	encodings = face_recognition.face_encodings(rgb, boxes)

	# Tương tự với tất cả những dữ liệu khác
	for encoding in encodings:
		knownEncodings.append(encoding)
		knownNames.append(name)

# Cho hết toàn bộ dữ liệu vào file encodings.pickle
print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open("encodings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()
