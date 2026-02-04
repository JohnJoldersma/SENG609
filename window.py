import tkinter as tk
from tkinter import StringVar

user_entries_list = []


def calculate_value(userInput):
    result = float(userInput) / 4.5
    return result


def button_command(userInput1, userInput2, userInput3, result_var):

    global user_entries_list
    user_entries_list = [userInput1, userInput2, userInput3]
    # return_value = calculate_value(userInput)
    # result_var.set(return_value)
    return user_entries_list


def runWindow():
    # --- Main Tkinter setup ---
    custom_font = ("Helvetica", 18, "bold")
    root = tk.Tk()
    root.title("Enter the transaction:")
    user_entries_list = []
    entry1_var = StringVar()
    entry2_var = StringVar()
    entry3_var = StringVar()

    frame1 = tk.Frame(relief=tk.RAISED, master=root)
    frame1.pack()
    label1 = tk.Label(root, font=custom_font,
                      text="Enter ODO:", padx=10, pady=10)
    label1.pack()
    entry1 = tk.Entry(fg="yellow", bg="blue", width=50, master=root, font=custom_font,
                      textvariable=entry1_var)
    entry1.pack()

    label2 = tk.Label(root, font=custom_font,
                      text="Enter CHRONO1:", padx=10, pady=10)
    label2.pack()
    entry2 = tk.Entry(fg="yellow", bg="blue", width=50, master=root, font=custom_font,
                      textvariable=entry2_var)
    entry2.pack()

    label3 = tk.Label(root, font=custom_font,
                      text="Enter MILES:", padx=10, pady=10)
    label3.pack()
    entry3 = tk.Entry(fg="yellow", bg="blue", width=50, master=root, font=custom_font,
                      textvariable=entry3_var)
    entry3.pack()

    result_text = tk.StringVar()
    result_text.set("Click to calculate fuel.")

    result_label = tk.Label(root, font=custom_font,
                            textvariable=result_text, padx=10, pady=10)
    result_label.pack()

    action_button = tk.Button(root, font=custom_font, text="Get Return Value",
                              command=lambda: button_command(entry1.get(),
                                                             entry2.get(),
                                                             entry3.get(),
                                                             result_text))
    action_button.pack(pady=10)
    # Start the Tkinter event loop
    # root.mainloop()
    return root


# runWindow()
