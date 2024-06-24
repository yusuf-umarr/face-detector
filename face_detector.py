import cv2
from random import randrange

#load some pre-trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose an image to detect faces in
img = cv2.imread('RDJ.jpeg')

#capture the video
webcam = cv2.VideoCapture(0) #0 mean the default camera

#Iterate forever over frames
while True:
    successful_frame_read, frame = webcam.read()

#convert img to greyscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


#detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# draw a rectangle 
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)


    cv2.imshow('Yusuf Face Detector', frame)
    key= cv2.waitKey(1) #wait 1 milisceond then go to the next iteration

    #Stop if Q key is pressed
    if key==81 or key== 113:
        break

    #Release the video capture object
webcam.release()



#detect faces
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# print(face_coordinates)

#draw a rectangles around the image

# cv2.rectangle(img, (100, 85), (100 + 181, 85 + 181), (0, 255, 0), 2)

# for (x, y, w, h) in face_coordinates:
    # cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(128,256), randrange(256), randrange(256)), 2)

#display image


# (x, y, w, h) = face_coordinates [0]







# cv2.imshow('Yusuf Face Detector', grayscaled_img)
# cv2.imshow('Yusuf Face Detector', img)
# cv2.waitKey()
 
print("code completed!!!")