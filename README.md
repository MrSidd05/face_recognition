Face Recognition Project
The provided code demonstrates the process of face recognition using the OpenCV and face_recognition libraries in Python. It loads two images: a reference face image and a test face image. 

First, the code detects the face in the reference image using the face_recognition library's `face_locations` function and calculates the face encoding using the `face_encodings` function. Then, a rectangle is drawn around the detected face in the reference image.

Next, the code performs the same steps for the test image, detecting the face location and encoding it. A rectangle is also drawn around the face in the test image.

The code then uses the `compare_faces` function to compare the face encodings of the reference image and the test image. It returns a list of boolean values indicating whether the faces match or not. Additionally, the `face_distance` function calculates the distance between the face encodings, where a lower distance suggests a better match.

The results and face distance are printed to the console. The test image is annotated with the results and face distance, which are displayed on the image using OpenCV's `putText` function. Both the reference image and the annotated test image are shown using the `imshow` function.

Finally, the program waits for a key press before closing the windows.

In summary, this code provides a basic implementation of face recognition by comparing the face encodings of a reference image and a test image. It showcases the essential steps involved in face recognition, including face detection, face encoding, face comparison, and result visualization.
