import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Crear el objeto que maneja la cámara
# el 0 representa el dispositivo a usar
cap = cv2.VideoCapture(0)

with mp_pose.Pose(
    static_image_mode=False) as pose:

    while True:
        # Leer el dispositivo
        ret, frame = cap.read()
        # Si ret es False, quiere decir que no se
        # obtuvo información alguna
        if ret == False:
            break   # Entonces, se rompe
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        if results.pose_landmarks is not None:
            print(results.pose_landmarks)
            #for landmark_id, landmark in enumerate(results.pose_landmarks):
            #    print(f"{landmark_id} en {landmark} es {type(results.pose_landmarks)}")
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(128, 0, 250), thickness=2, circle_radius=3),
                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))

        cv2.imshow("Video Kerr", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
