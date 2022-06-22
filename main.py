import cv2
import time
from datetime import datetime
import getpass

imagesFolder = "./imagens"
#cap = cv2.VideoCapture("rtsp://username:password@cameraIP/axis-media/media.amp")

# Use public RTSP Streaming for testing:
cap = cv2.VideoCapture("rtmp://179.106.215.39/live/camera1")

#cap = cv2.VideoCapture("test2.mp4")
frameRate = cap.get(5) #frame rate

cur_time = time.time()  # Get current time

# start_time_24h measures 24 hours
start_time_24h = cur_time

# start_time_1min measures 1 minute
start_time_1min = cur_time - 59  # Subtract 59 seconds for start grabbing first frame after one second (instead of waiting a minute for the first frame).

while cap.isOpened():
    frameId = cap.get(1)  # current frame number
    ret, frame = cap.read()

    if (ret != True):
        break

    cur_time = time.time()  # Get current time
    elapsed_time_1min = cur_time - start_time_1min  # Time elapsed from previous image saving.

    # If 60 seconds were passed, reset timer, and store image.
    if elapsed_time_1min >= 180:
        # Reset the timer that is used for measuring 60 seconds
        start_time_1min = cur_time

        image_name = "image_" + str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))  + ".jpg"

        print(f'Imagem {image_name} salva com sucesso!')

        filename = imagesFolder + '/' + image_name
        #filename = "image_" + str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))  + ".jpg"
        cv2.imwrite(filename, frame)

    elapsed_time_24h = time.time() - start_time_24h

    #Break loop after 24*60*60 seconds
    if elapsed_time_24h > 96*60*60:
        break

    #time.sleep(60 - elapsed_time) # Sleeping is a bad idea - we need to grab all the frames.


cap.release()
print ("Captura Concluida!")

cv2.destroyAllWindows()