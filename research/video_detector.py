import os
import sys
import numpy as np
import cv2
from PIL import Image
from IPython.display import display
from pprint import pprint
from ultralytics import YOLO


class SmokersVideoDetector:
    """Smokers detector class.

    Attributes:
    * model_path - path to the model weights
    * threshold - is model threshold (prob_of_ibbox > threshold => ibbox).

    Methods:
    * predict - returns probs of frames.
    * detect - returns bboxes with corisponding classes to every frame in video.
    """
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.include_classes = ["cigarette"]

    def predict(self, video_path):
        """Return generator to predict on frame per iteration as same as YOLO."""
        results = self.model(video_path, stream=True)
        return results

    def detect(self, video_path, threshold=0):
        """Detect cigarettes.
        
        Args:
        * video_path: path or url
        * threshold: threshold for confidence of the model

        Return 
        1. dict of frames and their bboxes with class and confidence
        2. dict of class index and label name
        """
        results = self.predict(video_path)
        out = {}
        for idx, frame in enumerate(results):
            frame = frame.cpu().numpy()
            label_names = frame.names
            boxes = frame.boxes
            # Note. If need change xyxy to more convient out (check YOLO predict docs). 
            predicted_boxes = [
                (bbox, cls, conf) for bbox, conf, cls in zip(boxes.xyxy, boxes.conf, boxes.cls) 
                if (conf > threshold) and label_names[cls] in self.include_classes
            ]
            out[idx] = predicted_boxes
        return out, label_names