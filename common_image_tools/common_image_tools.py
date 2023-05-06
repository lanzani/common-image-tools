import cv2

def resize_image(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Resize image to a specific width and height.
    :param image: image to be resized
    :param width: desired width
    :param height: desired height
    :param inter: interpolation method
    :return: resized image
    """

    # Get image dimensions
    dim = None
    (h, w) = image.shape[:2]

    # If both width and height are None, return original image
    if width is None and height is None:
        return image

    # If width is None, calculate the ratio of the height and construct the dimensions
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    # If height is None, calculate the ratio of the width and construct the dimensions
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    # Resize image
    resized = cv2.resize(image, dim, interpolation=inter)

    # Return resized image
    return resized