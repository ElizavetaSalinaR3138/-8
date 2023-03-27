import cv2

cap = cv2.VideoCapture("sample.mp4");

img = cv2.imread('fly64.png')

img_height, img_width, _ = img.shape

cap.set(3,1280)
cap.set(4,700)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
  diff = cv2.absdiff(frame1, frame2)
  gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (5, 5), 0)
  _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
  dilated = cv2.dilate(thresh, None, iterations = 3)
  сontours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


  for contour in сontours:
    (x, y, w, h) = cv2.boundingRect(contour)
    frame1[ y:y+img_height , x:x+img_width ] = img
    stroka = str(x) + ', ' + str(y)
    cv2.putText(frame1, stroka, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)

    if cv2.contourArea(contour) < 700:
      continue
    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

  cv2.imshow("frame1", frame1)
  frame1 = frame2
  ret, frame2 = cap.read()

  if cv2.waitKey(100) == 27:
    break




cap.release()
cv2.destroyAllWindows()
