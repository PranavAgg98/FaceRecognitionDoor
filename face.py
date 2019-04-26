import face_recognition
import cv2
import serial
import time
import threading

arduino = serial.Serial('COM3', 9600)

video_capture = cv2.VideoCapture(0)


pranav_image = face_recognition.load_image_file("pranav1.png")
pranav_face_encoding = face_recognition.face_encodings(pranav_image)[0]


amit_image = face_recognition.load_image_file("amit.jpeg")
amit_face_encoding = face_recognition.face_encodings(amit_image)[0]


known_face_encodings = [
    pranav_face_encoding,
    amit_face_encoding
]
known_face_names = [
    "Pranav",
    "Amit Suman"
]

def detected():

    arduino.write('1'.encode())
    time.sleep(5)
    
def not_detected():
    arduino.write('0'.encode()) 

while True:
   
    ret, frame = video_capture.read()

    
    rgb_frame = frame[:, :, ::-1]
    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

   
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        if True in matches:
            fd = 1
        else:
            fd = 0   
       
        name = "Unknown"

        
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        if fd==1:
           detected()
        else:
            not_detected()        
   
    cv2.imshow('Video', frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()


