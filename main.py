import cv2

image = cv2.imread("Baiden.jpg")


casc = cv2.CascadeClassifier("haarcascade_eye.xml")
eyes = casc.detectMultiScale(image)

print(eyes)

for (x,y,w,h) in eyes:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 3)



cv2.imshow("Baiden", image)
cv2.waitKey()

