# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

# Author: Eric Arndt
# Class: CSE 111 W05 Team Project
# Base code copied from lesson as instructed and changed as required to make new project.
# Created an Earth to Moon Weight Calculator that includes the GUI function from the base code.

# CREATIVITY: 
# Included the status bar label and the clear button as part of the Stretch Challange


import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Moon Weight Calc")
    frm_main.pack(padx=8, pady=6, fill=tk.BOTH, expand=2)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Weight:"
    lbl_wgt = Label(frm_main, text="Weight (10 - 500):")

    # Create an integer entry box where the user will enter their weight on Earth.
    ent_wgt = IntEntry(frm_main, width=4, lower_bound=10, upper_bound=500)

    # Create a label that displays "pounds"
    lbl_wgt_units = Label(frm_main, text="pounds")

    # Create labels that display "Earth" and "Moon"
    lbl_local1 = Label(frm_main, text="Earth")
    lbl_local2 = Label(frm_main, text="Moon")

    # Create labels that will display the results.
    lbl_earth = Label(frm_main, width=3)
    lbl_moon = Label(frm_main, width=3)
    lbl_location = Label(frm_main, text="Weight On:")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_wgt.grid(      row=0, column=0, padx=3, pady=3)
    ent_wgt.grid(      row=0, column=1, padx=3, pady=3)
    lbl_wgt_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_local1.grid(     row=2, column=1, padx=(3,3), pady=3)
    lbl_local2.grid(    row=2, column=2, padx=(3,3), pady=3)
    lbl_earth.grid(      row=1, column=1, padx=3, pady=3)
    lbl_moon.grid(      row=1, column=2, padx=3, pady=3)
    lbl_location.grid(row=2, column=0, padx=0, pady=3)

    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's earthest
        and moonest beneficial heart rates.
        """
        try:
            # Get the user's weight.
            wgt = ent_wgt.get()


            # Compute the user's weight on the moon
            # based on their weight on Earth
            earth = wgt
            moon = (wgt / (9.81)) * 1.622

            # Display the earth weight and moon weight for the user to see.
            lbl_earth.config(text=f"{earth:.0f}")
            lbl_moon.config(text=f"{moon:.0f}")

        except ValueError:
            # When the user deletes all the digits in the wgt
            # entry box, clear the earth and moon labels.
            lbl_earth.config(text="")
            lbl_moon.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_wgt.clear()
        lbl_earth.config(text="")
        lbl_moon.config(text="")
        ent_wgt.focus()

    # Bind the calculate function to the wgt entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_wgt.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the wgt entry box.
    ent_wgt.focus()


def center_window(width=300, height=125):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x+150, y-150))


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    # Create the Tk root object.
    root = tk.Tk()
    center_window()
    main()
