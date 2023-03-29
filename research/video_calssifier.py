import os
import sys

PATH_TO_NSWF_MODEL = "/content/nsfw_model"
if PATH_TO_NSWF_MODEL not in sys.path:
    sys.path.append(PATH_TO_NSWF_MODEL)

import numpy as np
import cv2
from PIL import Image
from IPython.display import display
from nsfw_detector import predict
from scenedetect import detect, ContentDetector, AdaptiveDetector
from pprint import pprint


def central_crop(image):
    center = image.shape
    w = h = min(image.shape[:2])
    x = center[1]/2 - w/2
    y = center[0]/2 - h/2

    crop_img = image[int(y):int(y+h), int(x):int(x+w)]
    return crop_img


class IntimateVideoClassifier:
    """NSWF classifier class.

    Attributes:
    * model_path - path to the model weights
    * input_dim - dimension of input for model.
    * batch_size - is a batch size of frames to the model, classify 
    frames when they will gather in batch.
    * threshold - is model threshold (prob_of_iclass > threshold => iclass).

    Methods:
    * predict - returns probs of frames.
    * classify_scenes - return timecode and frames of scenes to censor
    """

    def __init__(self, model_path, input_dim, batch_size, threshold=.8):
        """Note. input_dim = according to the weights of the model 224x224 or 299x299."""
        self.batch_size = batch_size
        self.input_dim = input_dim
        self.threshold = threshold
        self.model = predict.load_model(model_path)
        self.central_crop = True

    def predict(self, video_path, start_frame=0, end_frame=None, classify_every_n_frames=1):
        """Return probs of frames nswf classes starting from 
        `start_frame`(inclusive) to `end_frame`(exclusive) 
        with step `classify_every_n_frames`.

        Example: {'number_of_frame':{'class':probability, ...}, ...}
        """
        frame_count = start_frame

        batch = []
        frames_idx = []
        output = {}

        cap = cv2.VideoCapture(video_path)
        # end frame or video length
        end_frame = end_frame or int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # set start frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        while cap.isOpened() and (frame_count < end_frame):
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = self._preprocess(frame)
                # collect frames to batch with indexes
                frames_idx.append(frame_count)
                batch.append(frame)
                # process batch
                if len(batch) >= self.batch_size:
                    minibatch = np.concatenate(batch, axis=0)
                    probs = predict.classify_nd(self.model, minibatch)
                    output.update(dict(zip(frames_idx, probs)))
                    # clear frames and indexes collections
                    batch.clear()
                    frames_idx.clear()

                frame_count += classify_every_n_frames
                # move forward for `classify_every_n_frames` frames
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
            else:
                cap.release()
                break

        if len(batch) > 0:
            minibatch = np.concatenate(batch, axis=0)
            probs = predict.classify_nd(self.model, minibatch)
            output.update(dict(zip(frames_idx, probs)))

        return output

    def classify_scenes(self, video_path, scenes=None, scene_threshold=.1, classify_every_n_frames=1):
        """Return List of tuples (start of the scene: FrameTimecode, end of the scene: FrameTimecode)
        
        Args:
        * scenes - List of tuples of FrameTimecode to be classified. 
        If None than create with alghorithm. default None.
        * scene_threshold - if number of scenes with nswf class > scene_threshold than add it to return.

        FrameTimecode. https://scenedetect.com/projects/Manual/en/latest/api/frame_timecode.html#scenedetect-frame-timecode
        """
        scenes = scenes or detect(video_path, ContentDetector())
        nswf_scenes = []
        # TODO We create stream for every scene
        for scene_start, scene_end in scenes:
            scene_start_frame = scene_start.get_frames()
            scene_end_frame = scene_end.get_frames()
            scene_length = (scene_end_frame - scene_start_frame) / classify_every_n_frames

            # TODO Highlight slow movments and blurry frames
            probs = self.predict(video_path, 
                         start_frame=scene_start_frame, 
                         end_frame=scene_end_frame,
                         classify_every_n_frames=classify_every_n_frames
                         )
            nswf_scenes_count = sum([
                prob["porn"] > self.threshold 
                or prob["hentai"] > self.threshold 
                or prob["sexy"] > self.threshold 
                for prob in probs.values()
            ])
            # print(scene_start_frame, scene_end_frame, ":", (nswf_scenes_count / scene_length))
            if (nswf_scenes_count / scene_length) > scene_threshold:
                nswf_scenes.append((scene_start, scene_end))
        return self.gluing(nswf_scenes)

    @classmethod
    def gluing(cls, raw_nswf_scenes):
        """Glue close frames."""
        nswf_scenes = []
        for idx in range(len(raw_nswf_scenes)):
            if len(nswf_scenes) > 0:
                pred_end = nswf_scenes[-1][1].get_frames()
                cur_start = raw_nswf_scenes[idx][0].get_frames()
                if (cur_start - pred_end) < 20:
                    nswf_scenes[-1] = (nswf_scenes[-1][0], raw_nswf_scenes[idx][1])
                else:
                    nswf_scenes.append(raw_nswf_scenes[idx])
            else:    
                nswf_scenes.append(raw_nswf_scenes[idx])
        return nswf_scenes

    def _preprocess(self, frame):
        frame = central_crop(frame) if self.central_crop else frame
        resized_frame = cv2.resize(frame, (self.input_dim, self.input_dim))
        resized_frame = resized_frame / 255
        return resized_frame[np.newaxis, ...]