import cv2

from common_image_tools.tool import movement_detection_bbox


def main():
    cap = cv2.VideoCapture(0)
    previous_frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if previous_frame is not None:
            movement_bbox = movement_detection_bbox(previous_frame, frame)
        else:
            movement_bbox = []

        previous_frame = frame.copy()
        if movement_bbox is not None:
            frame = cv2.putText(frame, 'Movement detected', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                                cv2.LINE_AA)
            for bbox in movement_bbox:
                x, y, w, h = bbox
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(3) & 0xFF == ord('q'):
            break



if __name__ == "__main__":
    main()
