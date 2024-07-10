# -*- coding: utf-8 -*-
import cv2

from common_image_tools import VideoSource, OpencvBackendMode


# To test this is useful to use the docker-compose in magic-stream.


def main():
    # raw_source = "rtsp://admin:admin@192.168.1.47:554/live/ch0"
    # raw_source = "videos/test1.mp4"
    raw_source = 0
    source = VideoSource(raw_source, target_frame_height=480, target_frame_width=640)

    print(source.parsed_source)

    cap = cv2.VideoCapture(source.parsed_source)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
