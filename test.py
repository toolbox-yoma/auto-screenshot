import cv2
import numpy as np
import pyautogui
from enum import Enum

# import infoWindow
# nameList = infoWindow.submit_data()
# if nameList.__len__() == 0:
# 	print("No data entered!")
# 	exit(0)


class Pos(Enum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    WIDTH = 4
    HEIGHT = 5

threshold = 0.98
coordinate = [0, 70, 1079, 1850, 0, 0]

niddle_img = cv2.imread('last_page_alert.png', cv2.IMREAD_UNCHANGED)
# print(np.array(last_img))
print(niddle_img.shape)

w = niddle_img.shape[1]
h = niddle_img.shape[0]


# screenshot to cv2
screenshot = pyautogui.screenshot()
test = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
print(test.shape)

# test image
test_1 = cv2.imread('test-1.png', cv2.IMREAD_UNCHANGED)
test_2 = cv2.imread('test-last-1.png', cv2.IMREAD_UNCHANGED)

def showImage(img):
	cv2.imshow('test', img)
	cv2.waitKey()
	cv2.destroyAllWindows()

def showRect(img):
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print('-----------------')
    print('min_val:', min_val)
    print('max_val:', max_val)
    print('min_loc:', min_loc)
    print('max_loc:', max_loc)
    cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 220, 220), 2)
    showImage(img)

def showThreshold(img):
	yloc, xloc = np.where(img >= threshold)
	print('-----------------')
	print("yloc - ", len(yloc))
	print("xloc - ", len(xloc))

	# multiple rectangles
	# renctalge = []
	# for (x, y) in zip(xloc, yloc):
	# 	rectangles.append([int(x), int(y), int(w), int(h)])
	#	# cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	# rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
	# for (x, y, w, h) in rectangles:
	# 	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 220, 220), 2)
	# showImage(img)

result = cv2.matchTemplate(test_1, niddle_img, cv2. TM_CCOEFF_NORMED)
# showImage(result)
showThreshold(result)
# showRect(result)

result = cv2.matchTemplate(test_2, niddle_img, cv2. TM_CCOEFF_NORMED)
# showImage(re/ult)
showThreshold(result)
# showRect(result)


