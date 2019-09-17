

import numpy as np
import cv2

cap = cv2.VideoCapture("udp://@192.168.1.58:5001?overrun_nonfatal=1&fifo_size=5000000")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()  # ret = 1 if the video is captured; frame is the image
    
    # Our operations on the frame come here    
    img = cv2.flip(frame,1)   # flip left-right  
    #img = cv2.flip(img,180)     # flip up-down
    
    # Display the resulting image
    cv2.imshow('Video Capture',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


