import time
import os
from InfoWindow import InfoWindow
from Interact import Interact
from Telebot import Telebot
from ImageAnalyzer import ImageAnalyzer


class EbookCrawler:
    _root_path = "~/Downloads/screenshots/"
    _check_name_dup = False
    _name_list = []
    _is_pdf = []
    _current_name = ""
    _tele = None
    _testing = None
    _time_per_page = 0.6

    def __init__(self):
        # win = InfoWindow()
        self._name_list, self._testing, self._is_pdf, self._time_per_page = (
            InfoWindow.loop()
        )

        if self._testing:
            print("-------Testing mode-------")

        self._name_list = [
            s if s else time.strftime("%m%d_%H%M%S") + f"_{i}"
            for i, s in enumerate(self._name_list)
        ]
        print(self._name_list)
        if self.check_dup_in_namelist(self._name_list):
            print("Duplicate names entered!")
            exit(9)

        for name in self._name_list:
            if name:
                self.check_dup_in_path(name)

        if self._check_name_dup:
            print("choose another name!")
            exit(9)
        self._tele = Telebot()

    def check_dup_in_namelist(self, lst):
        return len(lst) != len(set(lst))

    def check_dup_in_path(self, name, create=False):
        temp_path = self._root_path + name
        real_path = os.path.expanduser(temp_path)
        print(real_path)

        if os.path.exists(real_path):
            print("File '{}' already exists!".format(name))
            self._check_name_dup = True
        elif create:
            os.mkdir(real_path)
            return real_path

    def clean_up(self):
        self._tele.send_message("all done - " + self._name_list.__str__())
        # Interact.rotate_screen()

    def start_capture(self, name, index):
        self._current_name = name
        save_path = ""
        if not self._testing:
            save_path = self.check_dup_in_path(name, True)
        page = 1
        Interact.click_item(index)
        if not self._testing:
            time.sleep(7)
        else:
            time.sleep(3)

        while True:
            screenshot = Interact.get_screenshot()
            if not self._testing:
                screenshot.save("{}/{}_{}.png".format(save_path, name, page))
                time.sleep(0.1)
            Interact.move_to_next_page()

            if ImageAnalyzer.is_last_page(screenshot):
                Interact.click_exit()
                print("{} - Page: {}".format(name, page - 1))
                # self._tele.send_message(
                #     "({}/{}) - {} - p.{}".format(
                #         index, self._name_list.__len__(), name, page - 1
                #     )
                # )
                time.sleep(5)
                break

            if ImageAnalyzer.is_same_page_as_before(screenshot):
                print("Stop Error: {} - Page: {}".format(name, page))
                self._tele.send_error(
                    "Stop Error: {} - Page: {}".format(name, page))
                break

            time.sleep(self._time_per_page)
            page += 1

    def run(self):
        try:
            if (self._name_list.__len__() == 0) or (self._name_list[0] == ""):
                print("No data entered!")
                exit(9)
            # self._tele.send_message("start - " + self._name_list.__str__())
            if not self._testing:
                time.sleep(5)
            else:
                time.sleep(2)

            for index, name in enumerate(self._name_list, start=1):
                if not name:
                    print("Empty name, skipping...")
                    continue
                print("\n----", name)
                self.start_capture(name, index)

            self.clean_up()

        except Exception as e:
            print("--- Exception Error ---")
            print(e)
            self._tele.send_message(self._current_name, True)
            self._tele.send_error(e)
            exit(9)

        finally:
            time.sleep(7)
            exit(0)


def main():
    app = EbookCrawler()
    app.run()


if __name__ == "__main__":
    main()
