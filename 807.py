import cv2


capture = cv2.VideoCapture(0)
while (capture.isOpened()):
    retval, image = capture.read()
    cv2.imshow("Video", image)
    # 窗口的图像刷新时间为1毫秒
    key = cv2.waitKey(1)
    if key == 32:
        break
capture.release()
cv2.destroyAllWindows()


# 打开摄像头