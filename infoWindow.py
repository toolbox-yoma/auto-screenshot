import tkinter as tk
# from tkinter import ttk


class InfoWindow:
    _root = tk.Tk()
    _root.title("Data Entry Form")

    _user_info_frame = tk.LabelFrame(_root, text="Book count")
    _user_info_frame.grid(row=0, column=0, padx=20, pady=20)

    _user_setting_frame = tk.LabelFrame(_root, text="Settings")
    _user_setting_frame.grid(row=1, column=0, padx=20, pady=20)

    _book_count = tk.Label(_user_info_frame, text="Count")
    _book_count.grid(row=1, column=0, padx=5, pady=5)
    _book_count_entry = tk.Entry(
        _user_info_frame,
        width=20,
        bd=2,
        relief="solid",
        highlightthickness=1,
        highlightcolor="black",
        bg="white",
        fg="black",
    )
    _book_count_entry.grid(row=1, column=1, padx=5, pady=5)
    _book_count_entry.focus()
    _book_count_entry.insert(0, "3")

    _is_testing = tk.BooleanVar()
    _test_button = tk.Checkbutton(
        _user_setting_frame, text="Test", variable=_is_testing
    )
    _test_button.grid(row=1, column=0, padx=5, pady=5)

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
            cls._book_count_entry.get(),
            cls._is_testing.get(),
            cls._time_value.get(),
        )

    @classmethod
    def submit_data(cls):
        cls._root.quit()
