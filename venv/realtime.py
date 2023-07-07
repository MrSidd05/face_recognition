# import cv2
# import numpy as np
# import face_recognition
# import os
# # from twilio.rest import Client


# # account_sid = 'ACa3cf920ad31e4fc16b69d1514f797d17'
# # auth_token = '3b667e5d7b6a1e1ba39284ecc3380bb8'
# # client = Client(account_sid, auth_token)
# # path=r'C:\Users\siddh\Desktop\major_project\ImagesAttendence'
# path='ImagesAttendence'
# images=[]
# classNames=[]
# mylist=os.listdir(path)
# print(mylist)

# for cl in mylist:
#     curImg=cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
# print(classNames)


# def findEncodings(images):
#     encodeList=[]
#     for img in images:
#         img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#         encode=face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList

# encodelistknown=findEncodings(images)
# cap=cv2.VideoCapture(0)

# while True:
#     success,img=cap.read()
#     imgS=cv2.resize(img,(0,0),None,0.25,0.25)
#     imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

#     facecurFrame=face_recognition.face_locations(imgS)
#     encodecurFrame=face_recognition.face_encodings(imgS)


#     for encodeFace,faceLoc in zip(encodecurFrame,facecurFrame):
#         matches=face_recognition.compare_faces(encodelistknown,encodeFace)
#         faceDis=face_recognition.face_distance(encodelistknown,encodeFace)
#         # print(faceDis)

#         matchIndex=np.argmin(faceDis)

#         if matches[matchIndex]:
#             name=classNames[matchIndex].upper()
#             print("Face Detetcted",name)

#         y1,x2,y2,x1=faceLoc
#         y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
#         cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
#         # cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#         cv2.putText(img,name,(x1+6,y2+6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


#     cv2.imshow('Webcam',img)
#     cv2.waitKey(1)
    

import cv2
import numpy as np
import face_recognition
import os
import datetime
import time

# path='ImagesAttendence'
path=r'C:\Users\siddh\Desktop\major_project\ImagesAttendence'
images=[]
classNames=[]
mylist=os.listdir(path)

for cl in mylist:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodelistknown=findEncodings(images)
cap=cv2.VideoCapture(0)

attendance = {}

while True:
    success,img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facecurFrame=face_recognition.face_locations(imgS)
    encodecurFrame=face_recognition.face_encodings(imgS)

    for encodeFace,faceLoc in zip(encodecurFrame,facecurFrame):
        matches=face_recognition.compare_faces(encodelistknown,encodeFace)
        faceDis=face_recognition.face_distance(encodelistknown,encodeFace)
        matchIndex=np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(img,name,(x1+6,y2+6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        else:
            name="unknown"
            # current_time=time.time()
            # print("New face detected: {name} at {current_time}")
            print("New face detected")
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(img,name,(x1+6,y2+6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


    cv2.imshow('Webcam',img)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
