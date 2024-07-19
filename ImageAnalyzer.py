import cv2
import numpy as np
from Interact import Interact


class ImageAnalyzer:
    _root = "./nidlde_images/"
    # _niddle_img = cv2.imread('last_page_alert.png', cv2.IMREAD_UNCHANGED)
    # _button_img = cv2.imread('move_button.png', cv2.IMREAD_UNCHANGED)
    _niddle_img = cv2.imread(_root + "last_page_alert_rotate.png", cv2.IMREAD_UNCHANGED)
    _button_img = cv2.imread(_root + "move_button_rotate.png", cv2.IMREAD_UNCHANGED)
    _w = _niddle_img.shape[1]
    _h = _niddle_img.shape[0]
    _threshold = 0.90
    _threshold_2 = 0.80
    _pre_screenshot_list = ["", "", "", "", "", "", ""]
    _max_available_dup_item = 7
    _current_dup_count = 0
    _prev_screenshot = ""

    @classmethod
    def show_image(cls, img):
        cv2.imshow("test", img)
        cv2.waitKey()
        cv2.destroyAllWindows()

    @classmethod
    def show_rect(cls, img, show=True):
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)
        print("-----------------")
        print("min_val:", min_val)
        print("max_val:", max_val)
        print("min_loc:", min_loc)
        print("max_loc:", max_loc)

        if show:
            cv2.rectangle(
                img,
                max_loc,
                (max_loc[0] + cls._w, max_loc[1] + cls._h),
                (0, 220, 220),
                2,
            )
            cls.show_image(img)

    @classmethod
    def show_threshold(cls, img, th=None):
        if th is None:
            th = cls._threshold

        yloc, xloc = np.where(img >= th)
        print("-----------------")
        print("threshold - ", th)
        print("yloc - ", len(yloc))
        print("xloc - ", len(xloc))

        # multiple rectangles
        # rectangle = []
        # for (x, y) in zip(xloc, yloc):
        # 	rectangles.append([int(x), int(y), int(w), int(h)])
        # # cv2.rectangle(img, (x, y), (x +_w, y +_h), (0, 255, 0), 2)
        # rectangles,_weights = cv2.groupRectangles(rectangles, 1, 0.2)
        # for (x, y,_w,_h) in rectangles:
        # 	cv2.rectangle(img, (x, y), (x +_w, y +_h), (0, 220, 220), 2)
        # showImage(img)

    @classmethod
    def check_threshold(cls, img, th=None):
        if th is None:
            th = cls._threshold

        yloc, xloc = np.where(img >= th)

        if (len(yloc) + len(xloc)) > 0:
            return True

        return False

    @classmethod
    def match_image(cls, screenshot, _niddle_img):
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGBA2BGRA)

        return cv2.matchTemplate(img, _niddle_img, cv2.TM_CCOEFF_NORMED)

    @classmethod
    def is_last_page(cls, screenshot):
        result = cls.match_image(screenshot, cls._niddle_img)
        # return cls.check_threshold(result)

        if cls.check_threshold(result):
            result_2 = cls.match_image(screenshot, cls._button_img)
            cls.show_threshold(result)
            cls.show_threshold(result_2, cls._threshold_2)
            return cls.check_threshold(result_2, cls._threshold_2)

        return False

    @classmethod
    def is_same_page_as_before(cls, screenshot):
        if cls._prev_screenshot == screenshot:
            cls._current_dup_count += 1

            if cls._current_dup_count > cls._max_available_dup_item:
                return True
        else:
            cls._current_dup_count = 0

        cls._prev_screenshot = screenshot

        return False

    @classmethod
    def test(cls):
        # screenshot to cv2
        screenshot = Interact.get_screenshot()
        test = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGBA2BGRA)

        # showImage(test)
        result = cv2.matchTemplate(test, cls._niddle_img, cv2.TM_CCOEFF_NORMED)

        if cls.check_threshold(result):
            temp = cv2.matchTemplate(test, cls._button_img, cv2.TM_CCOEFF_NORMED)
            cls.show_threshold(temp, cls._threshold_2)
            cls.showRect(temp)

    @classmethod
    def test_2(cls):
        # test image
        # test_1 = cv2.imread('test-1.png', cv2.IMREAD_UNCHANGED)
        test_2 = cv2.imread("test-last-1.png", cv2.IMREAD_UNCHANGED)

        # showImage(test_1)
        # result = cv2.matchTemplate(test_1, _niddle_img, cv2.TM_CCOEFF_NORMED)
        # showImage(result)
        # show_threshold(result)
        # showRect(result)

        result = cv2.matchTemplate(test_2, cls._niddle_img, cv2.TM_CCOEFF_NORMED)
        cls.showImage(result)
        cls.show_threshold(result)
        cls.showRect(result)
