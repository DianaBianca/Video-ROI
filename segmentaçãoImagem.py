import cv2

points = []
cropping = False


def click_and_drop(event, x, y, flags, param):
    global points, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        points = [[x, y]]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        points.append([x, y])
        cropping = False
        

video = cv2.VideoCapture("olhos.mp4")
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", click_and_drop)

while (True):
    
    retval, frame = video.read()
    
    # checando se o frame é válido
    if not retval:
        # Restart video.
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    cv2.imshow("frame", frame)

    #se existir os dois pontos selecionados no video
    if len(points) == 2:
        roi = frame[points[0][1]:points[1][1], points[0][0]:points[1][0]]
        cv2.imshow("roi", roi)
        
    cv2.waitKey(33)
    
cv2.destroyAllWindows()
