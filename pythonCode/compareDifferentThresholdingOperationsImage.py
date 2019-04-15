import cv2

thresholdType = 1
thresholdValue = 150
maxType = 4
maxValue = 255

def onTrackbarTypeChange(*args):
    global thresholdType
    thresholdType = args[0]
    th, result = cv2.threshold(image, thresholdValue, maxValue, thresholdType)
    cv2.imshow("image", result)

def onTrackbarValueChange(*args):
    global thresholdValue
    thresholdValue = args[0]
    th, result = cv2.threshold(image, thresholdValue, maxValue, thresholdType)
    cv2.imshow("image", result)


image = cv2.imread("../assets/putin.jpg", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)

cv2.createTrackbar("Type", "image", thresholdType, maxType, onTrackbarTypeChange)

cv2.createTrackbar("Value", "image", thresholdValue, maxValue, onTrackbarValueChange)

onTrackbarTypeChange(1)
onTrackbarValueChange(150)

while(True):
    k=cv2.waitKey(10)
    if(k == 27):
        break


cv2.destroyAllWindows()