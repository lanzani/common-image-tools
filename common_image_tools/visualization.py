# -*- coding: utf-8 -*-
from __future__ import annotations
import cv2
import numpy as np


def draw_points_shape(img, roi_points, color):
    for v in range(1, len(roi_points)):
        cv2.line(img, roi_points[v], roi_points[v - 1], color, 2)

    cv2.line(img, roi_points[0], roi_points[-1], color, 2)

    return img


def draw_contour(image: np.ndarray, points, fill: bool):
    points = np.array(points, dtype=np.int32)
    points = points.reshape((-1, 1, 2))

    if fill:
        cv2.fillPoly(image, [points], color=(255, 255, 255))
    else:
        cv2.polylines(image, [points], isClosed=True, color=(255, 255, 255), thickness=3)

    return image


def draw_point_or_contour(image: np.ndarray, points: list[tuple[float, float]], fill: bool = False) -> np.ndarray:
    points = np.array(points, dtype=np.int32)
    overlay = image.copy()

    points = points.reshape((-1, 1, 2))
    if len(points) > 3:
        if fill:
            cv2.fillPoly(image, [points], color=(255, 255, 255))
        else:
            # Create fully opaque fill
            cv2.fillPoly(overlay, [points], color=(255, 255, 255))  # White fill
            # Blend the overlay with original image for semi-transparent fill
            image = cv2.addWeighted(overlay, 0.3, image, 0.7, 0)
            # Add solid white contour on top
            cv2.polylines(image, [points], isClosed=True, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
    else:
        # For lines with less than 4 points - solid line
        cv2.polylines(image, [points], isClosed=False, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)

    return image
