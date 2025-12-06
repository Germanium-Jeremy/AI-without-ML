import cv2

cam = cv2.VideoCapture(1)
if not cam.isOpened():
     print("Camera 1 not working, trying next...")
     cam = cv2.VideoCapture(2)

if not cam.isOpened():
     print("Camera 2 also not working!")
else:
     print("Camera opened successfully")
     while True:
          ok, frame = cam.read()
          if not ok:
               print("Failed to capture frame")
               break
          cv2.imshow("Test", frame)
          if cv2.waitKey(1) == ord('q'):
               break

cam.release()
cv2.destroyAllWindows()
