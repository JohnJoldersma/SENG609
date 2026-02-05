import tkinter as tk
from tkinter import StringVar
import numpy as np
import normalization
import regression
import decision_tree3


def calculate_value(userInput):
    result = float(userInput) / 4.5
    return result


def button_command(userInput1, userInput2, userInput3, result_var):

    # return_value = calculate_value(userInput)
    # result_var.set(return_value)

    df, scaler = normalization.normalizeData()

    # Create the X and y arrays
    X = df[["ODO", "CHRONO1", "MILES"]]
    y = df["QTY"]

    # new_instance = np.array([[361000, 26830, 250]])
    new_instance = np.array([[float(userInput1), float(userInput2), float(userInput3)]])
    input_array = new_instance.reshape(1, -1)

    # run regression model
    result = regression.runRegression(X, y, input_array, scaler)

    # run decision tree
    decision_tree3.runTree(X, y)

    result_var.set(result)


def runWindow():
    # --- Main Tkinter setup ---
    custom_font = ("Helvetica", 18, "bold")
    root = tk.Tk()
    root.title("Enter the transaction:")

    entry1_var = StringVar()
    entry2_var = StringVar()
    entry3_var = StringVar()

    frame1 = tk.Frame(root, bg="lightgray", bd=2, relief="sunken")
    frame1.pack(padx=10, pady=10, fill="both", expand=True)
    label1 = tk.Label(frame1, font=custom_font, justify="center", anchor="center",
                      text="Enter ODO:", padx=10, pady=10)
    label1.pack()
    entry1 = tk.Entry(frame1, fg="yellow", bg="blue", width=50, font=custom_font,
                      textvariable=entry1_var)
    entry1.pack()

    label2 = tk.Label(frame1, font=custom_font, justify="center", anchor="center",
                      text="Enter CHRONO1:", padx=10, pady=10)
    label2.pack()
    entry2 = tk.Entry(frame1, fg="yellow", bg="blue", width=50, font=custom_font,
                      textvariable=entry2_var)
    entry2.pack()

    label3 = tk.Label(frame1, font=custom_font, justify="center", anchor="center",
                      text="Enter MILES:", padx=10, pady=10)
    label3.pack()
    entry3 = tk.Entry(frame1, fg="yellow", bg="blue", width=50, font=custom_font,
                      textvariable=entry3_var)
    entry3.pack()

    info_frame = tk.LabelFrame(root, text="Return Data:", padx=10, pady=10)
    info_frame.pack(padx=20, pady=20, fill="both", expand=True)
    result_text = tk.StringVar()
    result_text.set("Click to calculate fuel.")

    result_label = tk.Label(info_frame, font=custom_font,
                            textvariable=result_text, padx=10, pady=10)
    result_label.pack()

    action_button = tk.Button(info_frame, font=custom_font, text="Get Return Value",
                              command=lambda: button_command(entry1.get(),
                                                             entry2.get(),
                                                             entry3.get(),
                                                             result_text))
    action_button.pack(pady=10)
    # Start the Tkinter event loop
    root.mainloop()


runWindow()
