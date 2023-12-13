import pyautogui
import os
import time
from pynput import mouse
import math
from enum import Enum
import tkinter as tk
import tkinter.messagebox as mx
import sys



class Pos(Enum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    WIDTH = 4
    HEIGHT = 5

coordinate = [0, 70, 1079, 1850, 0, 0]

count = 0

# mx.showinfo("알림", "mouse position을 클릭해주세요! \n 좌상, 우하")
# def show_alert():
#     global coordinate
#     mx.showinfo("알림", "좌상: {}, {} \n 우하: {}, {}".format(coordinate[Pos.LEFT.value], coordinate[Pos.TOP.value], coordinate[Pos.RIGHT.value], coordinate[Pos.BOTTOM.value]))


def on_click(x, y, button, pressed):
    global count
    global coordinate
    if pressed:
        print(f'마우스가 ({math.trunc(x)}, {math.trunc(y)}) 위치에서 {button} 버튼이 클릭되었습니다.')
        count += 1
    if (count == 1):
        coordinate[Pos.LEFT.value] = math.trunc(x)
        coordinate[Pos.TOP.value] = math.trunc(y)
    elif (count == 2):
        coordinate[Pos.RIGHT.value] = math.trunc(x)
        coordinate[Pos.BOTTOM.value] = math.trunc(y)
        coordinate[Pos.WIDTH.value] = coordinate[Pos.RIGHT.value] - coordinate[Pos.LEFT.value]
        coordinate[Pos.HEIGHT.value] = coordinate[Pos.BOTTOM.value] - coordinate[Pos.TOP.value]
        if (coordinate[Pos.LEFT.value] > coordinate[Pos.RIGHT.value] or coordinate[Pos.TOP.value] > coordinate[Pos.BOTTOM.value]):
            # mx.showinfo("에러", "좌상, 우하를 다시 설정해주세요!")
            count = 0
        else:
            click_listener.stop()
        # show_alert()


click_listener = mouse.Listener(on_click=on_click)
click_listener.start()
click_listener.join()

def act():
    global coordinate
    page = int(page_number.get())
    book = book_name.get()
    file = file_name.get()
    temp_path = save_path.get() + file
    real_path = os.path.expanduser(temp_path)
    real_page = page + 1
    if is_pdf.get() == 1:
        real_page = page

    # crete directory
    if not os.path.exists(real_path):
        os.mkdir(real_path)
        print("Directory:", temp_path, " Created ")
    else:
        print("Directory:", temp_path, " already exists")
    print("책 이름: {}".format(book))
    print("파일 이름: {}".format(file))
    print("페이지 수: {}".format(page))
    print("경로: {}".format(real_path))

    # 화면 전환 대기 시간
    time.sleep(5)

    for i in range(1, real_page):
        screenshot = pyautogui.screenshot(region=(coordinate[Pos.LEFT.value], coordinate[Pos.TOP.value], coordinate[Pos.WIDTH.value], coordinate[Pos.HEIGHT.value]))
        # "{}/{}_{}.jpg".format(real_path, file, i)
        # file_save_path = "{}/{}_{}.png".format(real_path, file, i)
        screenshot.save("{}/{}_{}.png".format(real_path, file, i))
        pyautogui.press('right')
        print("page: {}/{}".format(i, page))
        time.sleep(1)

    if is_pdf.get() == 1:
        # 마지막 페이지 팝업 닫기
        pyautogui.click(676, 898)
        time.sleep(2)
        screenshot = pyautogui.screenshot(region=(coordinate[Pos.LEFT.value], coordinate[Pos.TOP.value], coordinate[Pos.WIDTH.value], coordinate[Pos.HEIGHT.value]))
        screenshot.save("{}/{}_{}.png".format(real_path, file, real_page))
        print("last page: {}/{}".format(real_page, real_page))


    root.quit()



root = tk.Tk()
entry = tk.Entry(root)

tk.Tk.title(root, "Auto Screenshot")
is_pdf = tk.IntVar()
R1 = tk.Radiobutton(root, text="pdf", variable=is_pdf, value=1)
R2 = tk.Radiobutton(root, text="epub", variable=is_pdf, value=0)
R1.grid(row=0, column=0)
R2.grid(row=0, column=1)
is_pdf.set(1)

tk.Label(root, text = "책 이름:").grid(row=1)
tk.Label(root, text = "파일 이름(약어) :").grid(row=2)
tk.Label(root, text = "페이지 수:").grid(row=3)
tk.Label(root, text = "좌상   : {}, {}".format(coordinate[Pos.LEFT.value], coordinate[Pos.TOP.value])).grid(row=5)
tk.Label(root, text = "우하   : {}, {}".format(coordinate[Pos.RIGHT.value], coordinate[Pos.BOTTOM.value])).grid(row=6)
tk.Label(root, text = "width : {}".format(coordinate[Pos.RIGHT.value] - coordinate[Pos.LEFT.value])).grid(row=7)
tk.Label(root, text = "height: {}".format(coordinate[Pos.BOTTOM.value] - coordinate[Pos.TOP.value])).grid(row=8)
tk.Label(root, text = "save path: ").grid(row=9)

book_name = tk.Entry(root)
file_name = tk.Entry(root)
page_number = tk.Entry(root)
save_path = tk.Entry(root)

book_name.grid(row=1, column=1)
book_name.insert(1, "book_name")
file_name.grid(row=2, column=1)
file_name.insert(2, "file_name")
page_number.grid(row=3, column=1)
page_number.insert(3, "0")
save_path.grid(row=9, column=1)
save_path.insert(9, "~/Downloads/screenshots/")

tk.Button(root, text='Quit', command=root.quit).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='confirm', command=act).grid(row=4, column=1, sticky=tk.W, pady=4)

tk.mainloop()

print("End")
os.system("afplay /System/Library/Sounds/Blow.aiff")
os.system("afplay /System/Library/Sounds/Blow.aiff")
os.system("afplay /System/Library/Sounds/Blow.aiff")
