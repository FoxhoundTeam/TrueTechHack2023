import numpy as np
import cv2
from tqdm import tqdm
from pytube import YouTube


def download_video_from_youtube(urls, dir, file_extension="mp4", resolution="360p"):
    if isinstance(urls, str):
        urls = [urls]
    for url in tqdm(urls):
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension=file_extension)
        stream.get_by_resolution(resolution).download(dir)


def cut_video_fragment(video_path, fragment_path, start_frame=0, end_frame=None):
    """Save fragment of the video in mp4 starting from `start_frame` and end with `end_frame`."""
    frame_count = start_frame
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(fragment_path, fourcc, 20.0, (width,  height))
    # end frame or video length
    end_frame = end_frame or int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # set start frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    while cap.isOpened() and (frame_count < end_frame):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            frame_count += 1
        else:
            cap.release()
            out.release()
            break