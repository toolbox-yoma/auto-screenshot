import tkinter as tk
# from tkinter import ttk


class InfoWindow:
    _root = tk.Tk()
    _root.title("Data Entry Form")

    _user_info_frame = tk.LabelFrame(_root, text="Books Name")
    _user_info_frame.grid(row=0, column=0, padx=20, pady=20)

    _user_setting_frame = tk.LabelFrame(_root, text="Settings")
    _user_setting_frame.grid(row=1, column=0, padx=20, pady=20)

    _first_is_pdf = tk.BooleanVar()
    _first_is_pdf.set(True)
    _second_is_pdf = tk.BooleanVar()
    _second_is_pdf.set(True)
    _third_is_pdf = tk.BooleanVar()
    _third_is_pdf.set(True)

    _first_name = tk.Label(_user_info_frame, text="First Book")
    _first_name.grid(row=1, column=0, padx=5, pady=5)
    _first_entry = tk.Entry(
        _user_info_frame,
        width=20,
        bd=2,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        bg="white",
        fg="black"
    )
    _first_entry.grid(row=1, column=1, padx=5, pady=5)
    _first_entry.focus()
    _first_radio_pdf = tk.Radiobutton(
        _user_info_frame, text="pdf", variable=_first_is_pdf, value=True
    )
    _first_radio_epub = tk.Radiobutton(
        _user_info_frame, text="epub", variable=_first_is_pdf, value=False
    )
    _first_radio_pdf.grid(row=1, column=2, padx=5, pady=5)
    _first_radio_epub.grid(row=1, column=3, padx=5, pady=5)

    _second_label = tk.Label(_user_info_frame, text="Second")
    _second_label.grid(row=2, column=0, padx=5, pady=5)
    _second_entry = tk.Entry(_user_info_frame)
    _second_entry.grid(row=2, column=1, padx=5, pady=5)
    _second_radio_pdf = tk.Radiobutton(
        _user_info_frame, text="pdf", variable=_second_is_pdf, value=True
    )
    _second_radio_pdf.grid(row=2, column=2, padx=5, pady=5)
    _second_radio_epub = tk.Radiobutton(
        _user_info_frame, text="epub", variable=_second_is_pdf, value=False
    )
    _second_radio_epub.grid(row=2, column=3, padx=5, pady=5)

    _third_label = tk.Label(_user_info_frame, text="Third")
    _third_label.grid(row=3, column=0, padx=5, pady=5)
    _third_entry = tk.Entry(_user_info_frame)
    _third_entry.grid(row=3, column=1, padx=5, pady=5)
    _third_radio_pdf = tk.Radiobutton(
        _user_info_frame, text="pdf", variable=_third_is_pdf, value=True
    )
    _third_radio_epub = tk.Radiobutton(
        _user_info_frame, text="epub", variable=_third_is_pdf, value=False
    )
    _third_radio_pdf.grid(row=3, column=2, padx=5, pady=5)
    _third_radio_epub.grid(row=3, column=3, padx=5, pady=5)

    _is_testing = tk.BooleanVar()
    _test_button = tk.Checkbutton(
        _user_setting_frame, text="Test", variable=_is_testing
    )
    _test_button.grid(row=1, column=0, padx=5, pady=5)
    _name_list = []

    _time_label = tk.Label(_user_setting_frame, text="Time per page")
    _time_label.grid(row=2, column=0, padx=5, pady=5)
    _time_value = tk.DoubleVar()
    _time_slider = tk.Scale(
        _user_setting_frame,
        # label="time per page",
        variable=_time_value,
        from_=0.1,
        to=1.0,
        length=300,
        orient=tk.HORIZONTAL,
        digits=2,
        resolution=0.1,
    )
    _time_slider.grid(row=2, column=1, padx=5, pady=5)
    _time_value.set(0.4)

    @classmethod
    def loop(cls):
        cls.submit_button = tk.Button(
            cls._root, text="Enter data", command=cls.submit_data, bg="lightcoral"
        )
        cls.submit_button.grid(row=3, column=0, padx=20, pady=10)
        cls._root.mainloop()
        return (
            cls._name_list,
            cls._is_testing.get(),
            [
                cls._first_is_pdf.get(),
                cls._second_is_pdf.get(),
                cls._third_is_pdf.get(),
            ],
            cls._time_value.get(),
        )

    @classmethod
    def submit_data(cls):
        cls._name_list.append(cls._first_entry.get())
        cls._name_list.append(cls._second_entry.get())
        cls._name_list.append(cls._third_entry.get())
        cls._name_list = [x for x in cls._name_list if x != "black"]
        cls._root.quit()
