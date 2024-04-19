# -*- coding: utf-8 -*-
import cv2
import numpy as np


def is_inside(point, shape) -> bool:
    ctn = np.array(shape)
    ctn = ctn.reshape((-1, 1, 2))

    # When measureDist=false , the return value is +1, -1, and 0, respectively. Otherwise, the return value is a
    # signed distance between the point and the nearest contour edge.
    result = cv2.pointPolygonTest(ctn, point, measureDist=False)

    return result >= 0
