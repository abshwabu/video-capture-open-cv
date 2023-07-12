import cv2, time

first_frame = None

video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray,(21,21),0)


    if first_frame is  None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    treshold_delta = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]

    cv2.imshow('gray',gray)
    cv2.imshow('delata',delta_frame)
    cv2.imshow('treshold',treshold_delta)

    

    key=cv2.waitKey(1000)
    
    if key== ord('Q') or key== ord('q'):
        break



    

video.release()

cv2.destroyAllWindows()