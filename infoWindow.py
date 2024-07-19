import tkinter as tk
# from tkinter import ttk


class InfoWindow:
    _root = tk.Tk()
    _root.title("Data Entry Form")

    _user_info_frame = tk.LabelFrame(_root, text="Books Name", bg="lightblue")
    _user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    _first_name = tk.Label(_user_info_frame, text="First Book", bg="lightgrey")
    _first_name.grid(row=1, column=0, padx=5, pady=5)
    _first_entry = tk.Entry(_user_info_frame)
    _first_entry.grid(row=1, column=1, padx=5, pady=5)

    _second_label = tk.Label(_user_info_frame, text="Second", bg="lightgrey")
    _second_label.grid(row=2, column=0, padx=5, pady=5)
    _second_entry = tk.Entry(_user_info_frame)
    _second_entry.grid(row=2, column=1, padx=5, pady=5)

    _third_label = tk.Label(_user_info_frame, text="Third", bg="lightgrey")
    _third_label.grid(row=3, column=0, padx=5, pady=5)
    _third_entry = tk.Entry(_user_info_frame)
    _third_entry.grid(row=3, column=1, padx=5, pady=5)

    _name_list = []

    @classmethod
    def loop(cls):
        cls.submit_button = tk.Button(
            cls._root, text="Enter data", command=cls.submit_data, bg="lightcoral"
        )
        cls.submit_button.grid(row=3, column=0, padx=20, pady=10)
        cls._root.mainloop()
        return cls._name_list

    @classmethod
    def submit_data(cls):
        cls._name_list.append(cls._first_entry.get())
        cls._name_list.append(cls._second_entry.get())
        cls._name_list.append(cls._third_entry.get())
        cls._name_list = [x for x in cls._name_list if x != ""]
        cls._root.quit()
