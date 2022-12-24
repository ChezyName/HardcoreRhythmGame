import tkinter as tk

#Consts
window_width = 780
window_height = 500


#Create Main Window
main = tk.Tk()

#Center Windowd
global screen_height, screen_width, x_cordinate, y_cordinate

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
    # Coordinates of the upper left corner of the window to make the window appear in the center
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#Finish Init Window
main.focus_force()
main.mainloop()

#File Pick State