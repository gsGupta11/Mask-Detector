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
            text = predict.mask(croppedimg)
            for (x, y, w, h) in coor:
                if len(text) == 6:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                else:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            
            font = cv2.FONT_HERSHEY_SIMPLEX 
            if len(text) == 6:
                cv2.putText(frame, text, (20,35),font, 1, (0, 255, 0),2, cv2.LINE_AA)
            else:
                cv2.putText(frame, text, (20,35),font, 1, (0, 0, 255),2, cv2.LINE_AA)

            cv2.imshow('Frame',frame)
            # cv2.imshow('Cropped',croppedimg)
            if cv2.waitKey(20) & 0xFF == 27:
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()