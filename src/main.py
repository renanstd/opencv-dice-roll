import cv2
import numpy as np
from sklearn import cluster


ip_webcam_url = "http://192.168.1.32:4747/video"
cap = cv2.VideoCapture(ip_webcam_url)

while(True):
    ret, frame = cap.read()
    # Cortar imagem para remover o header do DroidCam
    frame = frame[10:frame.shape[0], 0:frame.shape[1]]

    # blobs = get_blobs(frame)
    # dice = get_dice_from_blobs(blobs)
    # out_frame = overlay_info(frame, dice, blobs)

    cv2.imshow("frame", frame)

    res = cv2.waitKey(1)

    # Stop if the user presses "q"
    if res & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
