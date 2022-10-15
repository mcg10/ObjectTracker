import cv2
import numpy as np

KERNEL_SIZE = (30, 30)
MEDIAN_BLUR = 5
GRAYSCALE_LOW = 127
GRAYSCALE_HIGH = 255
PURPLE = (255, 0, 255)
THICKNESS = 4
OFFSET = 10
ESCAPE = 27


def main():

    camera = cv2.VideoCapture(0)
    background = cv2.createBackgroundSubtractorMOG2(
        history=1000, varThreshold=25, detectShadows=True)
    kernel = np.ones(KERNEL_SIZE, np.uint8)

    while True:

        can_read, frame = camera.read()
        if not can_read:
            print("Unable to read from camera")
            break

        foreground_mask = create_foreground(frame, background, kernel)
        contours, _ = cv2.findContours(foreground_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        areas = [cv2.contourArea(c) for c in contours]

        if len(areas) >= 1:
            largest_object = np.argmax(areas)
            draw_borders(contours, largest_object, frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(5) == ESCAPE:
            break

    camera.release()
    cv2.destroyAllWindows()


def create_foreground(frame, background, kernel):
    foreground_mask = background.apply(frame)
    # calculate foreground mask, remove noise, and make it black and white
    foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_CLOSE, kernel)
    foreground_mask = cv2.medianBlur(foreground_mask, MEDIAN_BLUR)
    _, foreground_mask = cv2.threshold(
        foreground_mask, GRAYSCALE_LOW, GRAYSCALE_HIGH, cv2.THRESH_BINARY)
    return foreground_mask


def draw_borders(contours, largest_object, frame):
    max_object = contours[largest_object]
    x, y, width, height = cv2.boundingRect(max_object)
    cv2.rectangle(frame, (x, y), (x + width, y + height), PURPLE, THICKNESS)

    x, y = x + width // 2, y + height // 2
    cv2.circle(frame, (x, y), THICKNESS, PURPLE, -1)
    label = 'x: {}, y: {}'.format(x, y)
    cv2.putText(frame, label, (x - OFFSET, y - OFFSET),
                cv2.FONT_HERSHEY_SIMPLEX, 1, PURPLE, THICKNESS)


if __name__ == '__main__':
    main()
