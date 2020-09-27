import cv2
import predict


def vedioPredict(inputtype):        
    cap = cv2.VideoCapture(inputtype)
    if cap.isOpened() == False:
        print("Error in opening video stream or file")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cascade = cv2.CascadeClassifier('face.xml')
            coor = cascade.detectMultiScale(grayimg, 1.3, 5)
            try:
                croppedimg = frame[coor[0][1]:coor[0][1]+coor[0][3],coor[0][0]:coor[0][0]+coor[0][2]]
            except:
                croppedimg = frame
            for (x, y, w, h) in coor:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow('Frame',frame)
            cv2.imshow('Cropped',croppedimg)
            if cv2.waitKey(20) & 0xFF == 27:
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()