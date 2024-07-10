# -*- coding: utf-8 -*-
import pytest

from common_image_tools import OpencvBackendMode, VideoSource


class TestVideoSource:
    @pytest.fixture
    def video_source(self):
        target_frame_width = 640
        target_frame_height = 360
        source = 0  # webcam source
        return VideoSource(source, target_frame_width, target_frame_height)

    def test_opencv_backend(self, video_source):
        # Test the default backend mode
        assert video_source.opencv_backend == OpencvBackendMode.OPENCV_DEFAULT

        # Test setting the backend mode
        video_source.opencv_backend = OpencvBackendMode.OPENCV_GSTREAMER_JETSON
        assert video_source.opencv_backend == OpencvBackendMode.OPENCV_GSTREAMER_JETSON

    def test_video_source_equality(self):
        target_frame_width = 640
        target_frame_height = 360
        source = 0  # webcam source

        video_source1 = VideoSource(source, target_frame_width, target_frame_height)
        video_source2 = VideoSource(source, target_frame_width, target_frame_height)

        # assert video_source1 is not video_source2
        # assert video_source1 != video_source2

        assert video_source1 == video_source2

    def test_video_source_equality_not_equal(self):
        target_frame_width = 640
        target_frame_height = 360
        source = 0  # webcam source

        video_source1 = VideoSource(source, target_frame_width, target_frame_height)
        video_source2 = VideoSource(source, target_frame_width, target_frame_height)

        # assert video_source1 is not video_source2
        # assert video_source1 != video_source2

        assert not (video_source1 != video_source2)

    def test_video_source_inequality_source(self):
        target_frame_width1 = 640
        target_frame_height1 = 360
        source1 = 0  # webcam source

        target_frame_width2 = 640
        target_frame_height2 = 360
        source2 = 1  # another webcam source

        video_source1 = VideoSource(source1, target_frame_width1, target_frame_height1)
        video_source2 = VideoSource(source2, target_frame_width2, target_frame_height2)

        assert video_source1 != video_source2

    def test_video_source_inequality_res(self):
        target_frame_width1 = 640
        target_frame_height1 = 360
        source1 = 0  # webcam source

        target_frame_width2 = 800
        target_frame_height2 = 600
        source2 = 0  # another webcam source

        video_source1 = VideoSource(source1, target_frame_width1, target_frame_height1)
        video_source2 = VideoSource(source2, target_frame_width2, target_frame_height2)

        assert video_source1 != video_source2

    def test_video_source_inequality_all(self):
        target_frame_width1 = 640
        target_frame_height1 = 360
        source1 = 0  # webcam source

        target_frame_width2 = 800
        target_frame_height2 = 600
        source2 = 1  # another webcam source

        video_source1 = VideoSource(source1, target_frame_width1, target_frame_height1)
        video_source2 = VideoSource(source2, target_frame_width2, target_frame_height2)

        assert video_source1 != video_source2
