from dataclasses import dataclass, field
from typing import Tuple, List

import cv2 as cv
from savia.core.library import get_intensity


@dataclass
class StreamProcessor:
    """StreamProcessor"""

    frame_store: list = field(default_factory=list)
    frame_gray_store: list = field(default_factory=list)
    frame_hist_store: list = field(default_factory=list)
    frame_intensity_store: list = field(default_factory=list)

    frame_count: int = None

    events: list = field(default_factory=list)
    uri: str = None
    fps: int = 24

    # def instantiate(self, url=None):
    #     """instantiate"""
    #     # TODO: Confirm that this is either an image or a video
    #     if not type(url) == str:
    #         raise "url must be of type str"

    #     cap = cv.VideoCapture(url)

    #     self.uri = url
    #     self.fps = cap.get(CAP_PROP_FPS)

    #     while cap.isOpened():
    #         ret, frame = cap.read()
    #         if not ret:
    #             break

    #         self.frame_store.append(frame)

    #         f_gray, f_hist, t128p = get_intensity(frame)
    #         self.frame_gray_store.append(f_gray)
    #         self.frame_hist_store.append(np.array(f_hist).ravel())
    #         self.frame_intensity_store.append(t128p)

    #     self.frame_count = len(self.frame_store)

    # def get_frames(self) -> Tuple[int, int, int]:
    #     """get_frames"""
    #     return get_frames(self.frame_intensity_store)

    # def get_events(self) -> List:
    #     """get_evetns"""
    #     self.events = get_events(self.frame_intensity_store, fps=self.fps)
    #     return self.events
