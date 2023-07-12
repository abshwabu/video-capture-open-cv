import cv2, time



video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    cv2.imshow('frame',gray)

    key=cv2.waitKey(1000)
    
    if key== ord('Q') or key== ord('q'):
        break



    

video.release()

cv2.destroyAllWindows()