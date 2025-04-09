import pyautogui
import math
import screeninfo
from enum import Enum


class Pos(Enum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    WIDTH = 4
    HEIGHT = 5


class Seq(Enum):
    EXIT = 0
    FIRST = 1
    SECOND = 2
    THIRD = 3


class Interact:
    # home 16:9
    # _coordinate = [[680, 1010], [190, 460], [600, 500], [1000, 500]]
    _coordinate = [[680, 1010], [100, 250], [300, 250], [500, 250]]
    # home 16:9 epub mode
    # _coordinate = [[], [], [], []]
    # work 16:10 normal
    # _coordinate = [[679, 1015], [154, 343], [460, 343], [752, 343]]
    # work 16:10 small
    # _coordinate = [[673, 1009], [103, 241], [300, 241], [500, 241]]

    # click_listener = mouse.Listener(on_click=set_click_position)
    # click_listener.start()
    # click_listener.join()
    _count = 0

    @classmethod
    def is_rotated_status(cls):
        print("is_rotated_status")
        monitor = screeninfo.get_monitors()
        if monitor[0].height > monitor[0].width:
            return True
        return False

    @classmethod
    def rotate_screen(cls):
        if cls.is_rotated_status():
            pyautogui.keyDown("command")
            pyautogui.press("f5")
            pyautogui.keyUp("command")

    @classmethod
    def move_to_next_page(cls):
        pyautogui.press("right")

    @classmethod
    def click_exit(cls):
        pyautogui.click(
            cls._coordinate[0][0],
            cls._coordinate[0][1],
        )

    @classmethod
    def click_item(cls, index):
        pyautogui.click(
            cls._coordinate[index][0],
            cls._coordinate[index][1],
        )

    @classmethod
    def set_click_position(cls, x, y, button, pressed):
        if pressed:
            cls._count += 1
            print(
                f"{cls._count}: 마우스가 ({math.trunc(x)}, {math.trunc(y)}) 위치에서 {button} 버튼이 클릭되었습니다."
            )
            cls._coordinate.append([math.trunc(x), math.trunc(y)])

        # if _count == 4:
        #     click_listener.stop()
        #     print(_coordinate)

    @classmethod
    def get_screenshot(cls):
        return pyautogui.screenshot()
