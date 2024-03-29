import cv2
import numpy as np
from PIL import Image


def opencv_built_with_gstreamer() -> bool:
    """Check if OpenCV has been built with GStreamer support.

    Returns:
        bool: True if OpenCV has been built with GStreamer support, False otherwise.
    """
    # Get build information
    build_info = cv2.getBuildInformation()
    # Get the row with GStreamer information
    gstreamer_info = [x for x in build_info.split("\n") if "GStreamer" in x]
    # Check if "YES" is in the row
    return "YES" in gstreamer_info[0]


def movement_detection(image1: np.ndarray, image2: np.ndarray, area_threshold: int = 400, blur_size: int = 5,
                       threshold_sensitivity: int = 25) -> bool:
    """Detect if a difference is present between two images.

    Args:
        image1 (np.ndarray): Image in opencv format (BGR)
        image2 (np.ndarray): Image in opencv format (BGR)
        area_threshold (int, optional): Area threshold. Defaults to 400.
        blur_size (int, optional): Blur size. Defaults to 5.
        threshold_sensitivity (int, optional): Threshold of a pixel to be considered different. Defaults to 25.

    Returns:
        bool: True if there is movement, False otherwise
    """

    delta_frame = cv2.absdiff(image1, image2)

    gray = cv2.cvtColor(delta_frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (blur_size, blur_size), 0)
    _, th = cv2.threshold(blur, threshold_sensitivity, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(th, np.ones((3, 3), np.uint8), iterations=3)

    c, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    difference = np.sum([cv2.contourArea(contour) for contour in c])

    # === DEBUG ===
    # try:
    #     cv2.imshow("Frame1", img1)
    #     cv2.imshow("Frame2", img2)
    #     cv2.imshow("Blur", blur)
    #     if difference > threshold:
    #         font = cv2.FONT_HERSHEY_SIMPLEX
    #         cv2.putText(dilated, 'Movimento Rilevato', (10, 50), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
    #     else:
    #         pass
    #     cv2.imshow("Differenza", dilated)
    #     cv2.imshow("C", c)
    # except:
    #     pass
    # === END DEBUG===

    return difference > area_threshold


def merge_color(image: np.ndarray, mask: np.ndarray, target_color_rgb: tuple) -> np.ndarray:
    """Merge the target color with the image using the mask using hsv color space.ù

    Args:
        image (np.ndarray): Image in opencv format (BGR)
        mask (np.ndarray): Mask in opencv format one channel
        target_color_rgb (tuple): Target color in RGB format

    Returns:
        np.ndarray: Image with merged color in opencv format (BGR)

    """
    hsv_image = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv_image)

    color_to_merge = np.uint8([[target_color_rgb[:: -1]]])
    hsv_color = cv2.cvtColor(color_to_merge, cv2.COLOR_BGR2HSV)

    h.fill(hsv_color[0][0][0])
    s.fill(hsv_color[0][0][1])

    new_hsv_image = cv2.merge([h, s, v])

    new_hsv_image = cv2.cvtColor(new_hsv_image, cv2.COLOR_HSV2BGR)

    colored_image = cv2.bitwise_and(new_hsv_image, new_hsv_image, mask=mask)
    original_image = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
    final_img = cv2.bitwise_xor(colored_image, original_image)

    return final_img


def merge_texture(image, mask, texture, alpha=0.3):
    """Merge the texture with the image using the mask using hsv color space."""

    # if texture is smaller than image, resize it
    # if texture.shape[0] < image.shape[0] or texture.shape[1] < image.shape[1]:
    pattern = cv2.resize(texture, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_AREA)
    # pattern = pil_image_to_cv2(resize_image(cv2_image_to_pil(texture), image.shape[1]))
    # pattern = texture[0:image.shape[0], 0:image.shape[1]]

    # crop texture to image size

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)

    hsv_pattern = cv2.cvtColor(pattern, cv2.COLOR_BGR2HSV)
    hp, sp, vp = cv2.split(hsv_pattern)

    # new_h = cv2.add(hp, h)
    # new_s = cv2.add(sp, s)
    # new_v = cv2.add(vp, vp)

    beta = (1.0 - alpha)
    new_v = cv2.addWeighted(v, alpha, vp, beta, 0)

    new_hsv_image = cv2.merge([hp, sp, new_v])
    # new_hsv_image = cv2.merge([new_h, new_s, v])

    new_hsv_image = cv2.cvtColor(new_hsv_image, cv2.COLOR_HSV2BGR)

    colored_image = cv2.bitwise_and(new_hsv_image, new_hsv_image, mask=mask)
    original_image = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
    final_img = cv2.bitwise_xor(colored_image, original_image)

    return final_img


def create_pil_image(size: tuple, color: tuple) -> Image:
    """Create a PIL image with the specified color and size.

    Args:
        size (tuple): Size of the image
        color (tuple): Color of the image in RGB format

    Returns:
        PIL.Image: Image in PIL format (RGB)
    """
    from PIL import Image

    return Image.new("RGB", size, color)


def create_cv2_image(size: tuple, color: tuple) -> np.ndarray:
    """Create a cv2 image with the specified color and size.

    Args:
        size (tuple): Size of the image
        color (tuple): Color of the image in BGR format

    Returns:
        np.ndarray: Image in opencv format (BGR)
    """
    img = np.zeros((size[0], size[1], 3), np.uint8)
    img[:] = color
    return img
