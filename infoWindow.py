import tkinter as tk
from tkinter import ttk


def submit_data():
    nameList = []
    nameList.append(first_entry.get())
    nameList.append(second_entry.get())
    nameList.append(third_entry.get())
    nameList = [x for x in nameList if x != '']
    root.quit()
    return nameList

root = tk.Tk()
root.title("Data Entry Form")

user_info_frame = tk.LabelFrame(root, text="Books Name", bg="lightblue")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name = tk.Label(user_info_frame, text="First Book", bg="lightgrey")
first_name.grid(row=1, column=0, padx=5, pady=5)
first_entry = tk.Entry(user_info_frame)
first_entry.grid(row=1, column=1, padx=5, pady=5)

second_label = tk.Label(user_info_frame, text="Second", bg="lightgrey")
second_label.grid(row=2, column=0, padx=5, pady=5)
second_entry = tk.Entry(user_info_frame)
second_entry.grid(row=2, column=1, padx=5, pady=5)

third_label = tk.Label(user_info_frame, text="Third", bg="lightgrey")
third_label.grid(row=3, column=0, padx=5, pady=5)
third_entry = tk.Entry(user_info_frame)
third_entry.grid(row=3, column=1, padx=5, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Enter data", command=submit_data, bg="lightcoral")
submit_button.grid(row=3, column=0, padx=20, pady=10)

root.mainloop()
