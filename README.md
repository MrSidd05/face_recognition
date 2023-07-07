#Basic.ipynb😎



Face Recognition Project
The provided code demonstrates the process of face recognition using the OpenCV and face_recognition libraries in Python. It loads two images: a reference face image and a test face image. 

First, the code detects the face in the reference image using the face_recognition library's `face_locations` function and calculates the face encoding using the `face_encodings` function. Then, a rectangle is drawn around the detected face in the reference image.

Next, the code performs the same steps for the test image, detecting the face location and encoding it. A rectangle is also drawn around the face in the test image.

The code then uses the `compare_faces` function to compare the face encodings of the reference image and the test image. It returns a list of boolean values indicating whether the faces match or not. Additionally, the `face_distance` function calculates the distance between the face encodings, where a lower distance suggests a better match.

The results and face distance are printed to the console. The test image is annotated with the results and face distance, which are displayed on the image using OpenCV's `putText` function. Both the reference image and the annotated test image are shown using the `imshow` function.

Finally, the program waits for a key press before closing the windows.

In summary, this code provides a basic implementation of face recognition by comparing the face encodings of a reference image and a test image. It showcases the essential steps involved in face recognition, including face detection, face encoding, face comparison, and result visualization.

#Realtime.ipynb😁



The provided code implements a real-time face recognition system using OpenCV, face_recognition, and the Telegram bot API. It begins by importing the necessary libraries and setting up the Telegram bot. The system then loads a set of known face images and their corresponding class names. These images are used to create face encodings for comparison.

The code continuously captures frames from the webcam and processes them. Each frame is resized and converted to RGB format, and face locations and encodings are detected using face_recognition. The face encodings of the captured faces are compared with the known encodings, and if a match is found, the corresponding class name is retrieved and displayed on the frame.

If a new face is detected (no match found), the system sets a flag indicating a new face has been detected. It saves the image of the new face and sends a notification with the image using the Telegram bot.

The annotated frame with recognized faces or "unknown" labels is displayed in real-time. The program continues this process until the 'q' key is pressed, at which point it releases the webcam capture and closes the windows.

Overall, this project showcases a real-time face recognition system that can identify known faces, label them accordingly, and notify the user when a new face is detected.
