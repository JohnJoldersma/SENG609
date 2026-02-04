import tkinter as tk
import window
import normalization
import regression
import decision_tree3


def run():
    # load window
    root = window.runWindow()
    root.mainloop()
    
    # prepare data
    df = normalization.normalizeData()

    # Create the X and y arrays
    X = df[["ODO", "CHRONO1", "MILES"]]
    y = df["QTY"]

    # run regression model
    regression.runRegression(X, y)

    # run decision tree
    decision_tree3.runTree(X, y)


if __name__ == '__main__':
    run()
