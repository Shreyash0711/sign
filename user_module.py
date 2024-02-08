import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import tensorflow

class HandGestureClassifier:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = HandDetector(maxHands=2)
        self.classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
        self.offset = 20
        self.imgSize = 300
        self.labels = ["Hello","I love you","No","Okay","Please","Thank you","Yes"]

    def process_frame(self):
        imgOutput= 0
        flag=1
        while (flag==1):
            cv2.imshow('Image', imgOutput)
            key = cv2.waitKey(1)
            if key == ord('b'):
                break

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    gesture_classifier = HandGestureClassifier()
    gesture_classifier.process_frame()
    gesture_classifier.release()
