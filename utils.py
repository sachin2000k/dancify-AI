import mediapipe as mp
import cv2
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
def get_keypoints(frame):
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, enable_segmentation=True) as pose:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         image.flags.writable = False
        results = pose.process(image)
        try:
            points = results.pose_landmarks.landmark
            landmarks = np.zeros(shape=(32,2))
            for i, point in enumerate(points):
                landmarks[i]=[point.x, point.y]
            return landmarks.reshape(2*33,)
        except Exception as ex:
            print("Exception :",ex)
            return None

def get_distance(points1, points2):
    distance = np.linalg.norm(points1-points2)
    return distance
    
    # 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
