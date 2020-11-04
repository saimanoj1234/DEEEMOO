import cv2
video = cv2.VideoCapture(0);
while(True):
    ret,frame = video.read()
    cv2.imshow('fram',frame)

    if cv2.waitKey(1) == ord('m'):
        break
video.release()
cv2.destroyAllWindows()
