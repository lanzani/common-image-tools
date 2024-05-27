import cv2

from common_image_tools.tool import movement_detection


def main():
    cap = cv2.VideoCapture(0)
    previous_frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if previous_frame is not None:
            movement = movement_detection(previous_frame, frame, blur_size=5, threshold_sensitivity=25)

        cv2.imshow('frame', frame)

        if cv2.waitKey(3) & 0xFF == ord('q'):
            break

        previous_frame = frame.copy()


if __name__ == "__main__":
    main()
