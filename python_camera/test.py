import cv2

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

gFrame_width = 640
gFrame_height = 480
gFrame_scale = 0.5
gWin_x_shift = 70
gWin_width = int(gFrame_width * gFrame_scale)
gFace_shift = int(20 * gFrame_scale)
gFace_min = int(20 * gFrame_scale)

cap_list = [0, 2, 'http://richard:Aa123456@10.37.228.0:8081/video']
cap = []

user_exit = 0
for cap_list_item in cap_list:
	cap0 = cv2.VideoCapture(cap_list_item)
	cap0.set(cv2.CAP_PROP_FRAME_WIDTH, gFrame_width)
	cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, gFrame_height)

	cap.append( cap0 )

while(True):
	i = 0
	for cap_item in cap:
		i = i +1
		ret0, frame0 = cap_item.read()
		#ret1, frame1 = cap1.read()
		if ret0:
			small_frame0 = cv2.resize(frame0, (0, 0), fx=gFrame_scale, fy=gFrame_scale)
			gray0 = cv2.cvtColor(small_frame0, cv2.COLOR_BGR2GRAY)

			faces0 = faceCascade.detectMultiScale(
				gray0,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(gFace_min, gFace_min)
	    		)
			# Draw a rectangle around the faces
			for (x, y, w, h) in faces0:
				cv2.rectangle(small_frame0, (x -gFace_shift, y -gFace_shift), (x+w +gFace_shift, y+h +gFace_shift), (0, 255, 0), 2)
			dname = 'frame0' + str(i)
			cv2.imshow(dname, small_frame0)
			cv2.moveWindow(dname, (i-1) *gWin_width + gWin_x_shift,0)
			
			if cv2.waitKey(1) & 0xFF == ord('q'):
				user_exit = 1
				break
		if user_exit ==1 :
			break

for cap_item in cap:
	cap_item.release()
	
cv2.destroyAllWindows()


